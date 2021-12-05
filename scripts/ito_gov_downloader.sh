#!/bin/bash

curl 'https://eservices.ito.gov.ir/Page/GetIPList' \
  -H 'Connection: keep-alive' \
  -H 'Cache-Control: max-age=0' \
  -H 'Origin: https://eservices.ito.gov.ir' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Referer: https://eservices.ito.gov.ir/page/iplist' \
  -H 'Cookie: __RequestVerificationToken=28Ler0j0Udsc1-A5gpuq2ODdS9qbv7NHP1MaI40R7NvUC2fxIu5L6ynPRPl68jwZQhBb7ktjitJnoIh_Jr97cYse2MvVW7xh_55WSQflekU1; ASP.NET_SessionId=kjn05bvrle2ulrchfvx1tjpa' \
  --data-raw '__RequestVerificationToken=duB0tkYUqhE6tkRpAl2Py5n7A8TgiG5gvw6aJOkccAmOdT72ONRHgmKxLbT0Pd_J2cQTRACu7OHJB1ofYqCkr4wwF3KoIC7EYUpLvaeIWvU1&ExportExcel=true' \
  --compressed \
  -o "../resources/ito_gov.html"