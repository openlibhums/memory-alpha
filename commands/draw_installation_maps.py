import argparse
import csv
import json
import re
import requests
import subprocess

from diskcache import Cache
import geojson


parser = argparse.ArgumentParser(
    prog="draw_installation_map",
    description="Draws a map of Janeway installations",
)


INSTALLATION_CSV = "themes/alpha/static/data/janeway_installations.csv"
INSTALLATION_GEOJSON = "themes/alpha/static/data/janeway_installations.geojson"
API_BASE = "https://api.ror.org/v2/organizations/"
CACHE_DIR = ".cache/ror_api"
BASE_MAP_GEOJSON = "themes/alpha/static/data/ne_110m_admin_0_countries.json"
CACHE = Cache(CACHE_DIR)
ROR_REGEX = r"0[a-hj-km-np-tv-z|0-9]{6}[0-9]{2}"
ROR_PROG = re.compile(ROR_REGEX)


def clean_ror_id(ror_id):
    match = ROR_PROG.search(ror_id)
    return match.group(0)


def query_api(ror_id):
    url = f"{API_BASE}{ror_id}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.content


def get_ror_record(ror_id):
    try:
        return CACHE[ror_id]
    except KeyError:
        ror_record = json.loads(query_api(ror_id))
        CACHE[ror_id] = ror_record
        return ror_record


def get_features_by_id(feature_collection):
    features = {}
    for feature in feature_collection["features"]:

        # Make each installation a tuple for hashing
        installations = []
        for installation in feature["properties"]["installations"]:
            installations.append(tuple(installation))
        feature["properties"]["installations"] = installations

        # Put the id as the feature key
        features[feature["id"]] = feature

    return features


def create_feature(ror_id):
    ror_record = get_ror_record(ror_id)
    loc_details = ror_record["locations"][0]["geonames_details"]
    geonames_id = ror_record["locations"][0]["geonames_id"]
    point = geojson.Point((loc_details["lng"], loc_details["lat"]))
    city_name = loc_details["name"]
    continent = loc_details["continent_name"]
    properties = {
        "name": city_name,
        "continent": continent,
    }
    feature = geojson.Feature(
        geometry=point,
        id=geonames_id,
        properties=properties,
    )
    return feature


def open_feature_collection():
    try:
        with open(INSTALLATION_GEOJSON, "r") as ref:
            return geojson.loads(ref.read())
    except FileNotFoundError:
        return geojson.FeatureCollection([])


def close_feature_collection(feature_collection):
    dump = geojson.dumps(feature_collection, indent=2)
    with open(INSTALLATION_GEOJSON, "w") as ref:
        ref.write(dump)


def add_to_feature(feature, csv_row):
    name = csv_row["Name"]
    site = csv_row["Site"]
    ror_id = csv_row["ROR ID"]
    hosting = csv_row["Hosting"]
    installation = (name, site, ror_id, hosting)
    if "installations" not in feature["properties"]:
        feature["properties"]["installations"] = []
    if installation not in feature["properties"]["installations"]:
        feature["properties"]["installations"].append(installation)
    return feature


def add_to_feature_dict(feature_dict, csv_row):
    ror_id = clean_ror_id(csv_row["ROR ID"])
    ror_record = get_ror_record(ror_id)
    geonames_id = ror_record["locations"][0]["geonames_id"]
    if geonames_id in feature_dict:
        created = False
        feature = feature_dict[geonames_id]
    else:
        created = True
        feature = create_feature(ror_id)
    feature = add_to_feature(feature, csv_row)
    if created:
        feature_dict[geonames_id] = feature
    return feature_dict


def update_geojson():
    feature_collection = open_feature_collection()
    feature_dict = get_features_by_id(feature_collection)
    with open(INSTALLATION_CSV, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for csv_row in reader:
            if not csv_row["ROR ID"]:
                continue
            feature_dict = add_to_feature_dict(feature_dict, csv_row)
    feature_collection = geojson.FeatureCollection(
        [feature for feature in feature_dict.values()]
    )
    close_feature_collection(feature_collection)


def draw_maps():
    common_args = [
        "svgis",
        "draw",
        BASE_MAP_GEOJSON,
        INSTALLATION_GEOJSON,
        "--viewbox",
        "--no-inline",
        "--scale",
        "5000",
        "--style",
        ""
    ]
    europe_output = "themes/alpha/templates/svg/europe_map.svg"
    europe_args = common_args + [
        "--bounds",
        "-10",
        "35",
        "25",
        "63",
        "--clip",
        "--output",
        europe_output
    ]
    subprocess.run(europe_args)
    north_america_output = "themes/alpha/templates/svg/north_america_map.svg"
    north_america_args = common_args + [
        "--bounds",
        "-122",
        "17",
        "-68",
        "57",
        "--clip",
        "--output",
        north_america_output
    ]
    subprocess.run(north_america_args)
    australia_output = "themes/alpha/templates/svg/australia_map.svg"
    australia_args = common_args + [
        "--bounds",
        "110",
        "-45",
        "160",
        "-9",
        "--clip",
        "--output",
        australia_output
    ]
    subprocess.run(australia_args)

    # Remove CSS styles inside SVGs
    subprocess.run(["svgis", "style", "--style", "", "--replace", europe_output, europe_output])
    subprocess.run(["svgis", "style", "--style", "", "--replace", north_america_output, north_america_output])
    subprocess.run(["svgis", "style", "--style", "", "--replace", australia_output, australia_output])

    html_id_re = re.compile(r'id=".*?"')
    for svg_path in [europe_output, north_america_output, australia_output]:
        with open(svg_path, "r") as ref:
            svg_str = ref.read()
            svg_str = re.sub(html_id_re, "", svg_str)
        with open(svg_path, "w") as ref:
            ref.write(svg_str)

def run():
    update_geojson()
    draw_maps()


if __name__ == "__main__":
    run()
    CACHE.close()
