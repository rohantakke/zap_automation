apikey=$(jq -r .api_key config.json)
zap_url=$(jq -r .listening_host config.json) 
zap_port=$(jq -r .listening_port config.json)
curl -X GET http://$zap_url:$zap_port/OTHER/core/other/htmlreport/ \
  -H 'Accept: application/json' \
  -H 'X-ZAP-API-Key: '$apikey''