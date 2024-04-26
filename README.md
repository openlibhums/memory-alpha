# Memory Alpha
This repository is for the build of the janeway.systems site.

The website is built on top of the static-site generator
[Pelican](https://getpelican.com/) using [tailwind
CSS](https://tailwindcss.com/).

## Setting up the development environment

### Native install

Pelican is built for python (3.8.4+). In order to setup the project, you can
install your dependecies (including Pelican) with pip: `pip install -r
requirements.txt`.

Pelican's build system uses [GNU Make](https://www.gnu.org/software/make/) which comes pre-installed on most GNU Linux distributions.

You can refer to the guide on how to [install Pelican](https://docs.getpelican.com/en/latest/quickstart.html#installation) for more details.

The project also uses the official Tailwind CSS plugin for Pelican, which
should have been installed by the previous step, however you will still need to
install NodeJS as described in [their
README](https://github.com/pelican-plugins/tailwindcss).

Once the dependencies are installed you can run `make help` to see a list of
available build targets.

### Docker install

Our Makefile has two targets for working within a docker container:

- `make image` will create build a docker image on top of the official Python
  Alpine linux docker image, which you can use for all Pelican build processes

- `make shell` will create an ephemeral container and connect to it via tty. From
  here you can run `make help` to see a list of available build targerts
