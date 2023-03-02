#!/usr/bin/env bash

if [[ $# -lt 2 ]]; then
  echo -e "Missing parameter\nCommand: $0 /path/to/python"
fi

PYTHON=$1

$PYTHON manage.py link_plugins
$PYTHON manage.py migrate
$PYTHON manage.py build_assets
$PYTHON manage.py collectstatic --noinput
