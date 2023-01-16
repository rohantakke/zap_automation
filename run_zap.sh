python3 launchSpider.py
python3 activeScan.py
rm *.html
./getReport.sh > web_application_scanner_report.html
cp web_application_scanner_report.html old_reports/webapp_$(date +"%d_%m_%y").html