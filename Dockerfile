FROM python:3.12.3-alpine3.19

# Install OS level dependencies
RUN apk add --no-cache make

RUN mkdir /output
# Setup user
RUN /usr/sbin/adduser -g pelican -D pelican
RUN chown -R pelican:pelican /output
USER pelican
RUN /usr/local/bin/python -m venv /home/pelican/venv

ENV PATH="/home/pelican/venv/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE="1" \
    PYTHONUNBUFFERED="1"

# Setup python environment
COPY --chown=pelican:pelican requirements.in /home/pelican/janeway.systems/requirements.in
RUN /home/pelican/venv/bin/pip install --no-cache-dir pip-tools
RUN /home/pelican/venv/bin/pip-compile /home/pelican/janeway.systems/requirements.in
RUN /home/pelican/venv/bin/pip install --no-cache-dir --requirement /home/pelican/janeway.systems/requirements.txt

WORKDIR /app

ENTRYPOINT ["/home/pelican/venv/bin/pelican"]
