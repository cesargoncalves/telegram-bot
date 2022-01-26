#!/usr/bin/env bash

function setup_dependencies() {
  [ ! -f "requirements.txt" ] && { echo -e "\033[31;5mrequirements.txt not found!\033[0m"; exit 1; }
  [ ! -d "venv" ] && mkdir venv
  [ -z "$(ls -A venv)" ] && { python3 -m virtualenv --python=python3 --system-site-packages venv && venv/bin/python3 -m pip install --upgrade pip; }
  ./venv/bin/pip3 install -r requirements.txt
  exit 0
}

[ "$1" == "--setup_dependencies" ] && setup_dependencies
[ ! -d "venv" ] && setup_dependencies

./venv/bin/python3 example.py "$@"
