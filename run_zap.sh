python3 launchSpider.py
python3 activeScan.py
./html.sh > $(jq -r .target_url config.json | awk -F// '{print $2}')_$(date +"%d_%m_%y_%T" | tr -d ':').html