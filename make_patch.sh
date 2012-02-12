#!/bin/bash
XIRVIK_PATH="/home/orion/projects/rentacoder/xirvik"
ORIG_VERSION="deluge-1.3.5"
TO_VERSION="master"

git diff $ORIG_VERSION $TO_VERSION > ${XIRVIK_PATH}/patches-deluge/deluge.patch
rm -f deluge/ui/web/js/deluge-all/.build_data
rm -f deluge/ui/web/js/ext-extensions/.build_data
( cd deluge/ui/web; bash build js/deluge-all )
( cd deluge/ui/web; bash build js/ext-extensions )
tar -czvf ${XIRVIK_PATH}/js-deluge/deluge-all.tar.gz \
    deluge/ui/web/js/deluge-all.js \
    deluge/ui/web/js/deluge-all-debug.js \
    deluge/ui/web/js/ext-extensions.js \
    deluge/ui/web/js/ext-extensions-debug.js

git bundle create ${XIRVIK_PATH}/bundles/deluge.bundle $ORIG_VERSION..$TO_VERSION
