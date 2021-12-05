#!/bin/bash

curl "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&license_key=$1&suffix=zip" \
  -o "../resources/temp.zip"

# create temp directory and extract it
cd ../resources/ || exit
mkdir temp && mv temp.zip temp && cd temp && unzip temp.zip

# extract useful files
cd Geo* || exit
mv GeoLite2-Country-Blocks-* GeoLite2-Country-Locations-en.csv ../../
cd ../../
rm -rf temp