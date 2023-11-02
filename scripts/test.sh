#!/usr/bin/env bash

set -e
set -x

coverage run -m pytest tests
coverage report --show-missing
coverage html
