DOCSET_NAME = Keras
SHELL = /bin/bash

all:
	echo "Nothing"

build:
	bash wget_html.sh
	bash build.sh
	cd keras.io && tar --exclude='.DS_Store' -cvzf ${DOCSET_NAME}.tgz ${DOCSET_NAME}.docset

clean:
	rm -rf keras.io


