#!/bin/bash
find '.' -type f -name '*.1.html' -exec rm {} \;
find '.' -type f -name '*.html' -exec python preprocess.py {} \;
