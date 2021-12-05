#!/bin/bash

curl "https://www.ip2location.com/download/?token=$1&file=DB1LITECSV" \
  -o "../resources/temp.zip"

# create temp directory and extract it
cd ../resources/ || exit
mkdir temp && mv temp.zip temp && cd temp && unzip temp.zip

# convert it to correct format
git clone https://github.com/ip2location/ip2location-python-csv-converter.git
python3 ip2location-python-csv-converter/ip2location-csv-converter.py -cidr -replace IP2LOCATION-LITE-DB1.CSV ip2location.csv

# extract useful files
mv ip2location.csv ../
cd ../
rm -rf temp