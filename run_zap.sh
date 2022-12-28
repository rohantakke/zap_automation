python3 launchSpider.py
python3 activeScan.py
rm *.html
./getReport.sh > $(jq -r .target_url config.json | awk -F// '{print $2}')_$(date +"%d_%m_%y").html
cp *.html old_reports/