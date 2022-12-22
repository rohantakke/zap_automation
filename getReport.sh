apikey=$(jq -r .api_key config.json)
curl -X GET http://127.0.0.1:8082/OTHER/core/other/htmlreport/ \
  -H 'Accept: application/json' \
  -H 'X-ZAP-API-Key: '$apikey''