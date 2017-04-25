#!/bin/bash
cp theme*.css keras.io/css/
find '.' -type f -name '*.1.html' -exec rm {} \;
cp dashing.json keras.io/
cd keras.io && dashing build
cd ..
