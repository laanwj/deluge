#!/bin/bash
rm -f deluge/ui/web/js/deluge-all/.build_data
( cd deluge/ui/web; bash build js/deluge-all )
rm -f deluge/ui/web/js/ext-extensions/.build_data
( cd deluge/ui/web; bash build js/ext-extensions )
