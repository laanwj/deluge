#!/bin/bash
python setup.py build_plugins
cp deluge/plugins/*.egg /utorrentsessions/test_deluge/plugins/
