#!/bin/bash

VENV=$(which virtualenv)
echo Using $VENV
$VENV -p /usr/bin/python3.8 --prompt='(arms) ' .venv
