#!/bin/bash
wget --header 'Accept-Encoding: deflate' --domains=keras.io -e robots=off --no-parent --adjust-extension -r 'https://keras.io/'

