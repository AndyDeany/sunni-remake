#!/bin/bash
pylint main.py lib
pycodestyle main.py lib
pydocstyle main.py lib
