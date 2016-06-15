#!/bin/sh

SECRET_KEY=$(pwgen -sy 60 1)

cat <<HERE > $(dirname $0)/xenim/settings/base_local.py
from .base import Base as DefaultBase

class Base(DefaultBase):
    SECRET_KEY = '$SECRET_KEY'
HERE
