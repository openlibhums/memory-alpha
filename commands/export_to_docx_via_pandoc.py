import os

from tqdm import tqdm
import pandoc

IMPORT_DIR = "content/support"
EXPORT_DIR = "pandoc_output"


def get_old_and_new_paths(filepath):
    base_filename, ext = os.path.splitext(filepath)
    new_filepath = os.path.join(EXPORT_DIR, base_filename + ".docx")
    return filepath, new_filepath


def convert_md(old_path, new_path):
    new_dir, _tail = os.path.split(new_path)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    doc = pandoc.read(file=old_path)
    image_reference_point, _tail = os.path.split(old_path)
    options = ["--resource-path", image_reference_point]
    pandoc.write(doc, file=new_path, format="docx", options=options)


def convert_directory(directory):
    for dir_entry in tqdm(os.scandir(directory)):
        if dir_entry.name.startswith("."):
            continue

        if dir_entry.is_dir():
            convert_directory(dir_entry.path)
            continue

        old_path, new_path = get_old_and_new_paths(dir_entry.path)
        _path, ext = os.path.splitext(old_path)
        if ext in [".md"]:
            convert_md(old_path, new_path)


if __name__ == "__main__":
    convert_directory(IMPORT_DIR)
