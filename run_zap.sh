trap 'echo "Interrupted! Exiting...";revert_placeholders;exit' INT

revert_placeholders(){
    crntip=$(cat config.json | grep target | awk -F"//" '{print $2}' | tr -d "\",")
    sed -i "/$crntip/ s/$crntip/IP/" /home/secops/automation_tools/PathTraversal_and_SensitiveFileChecker/ip.config
}

for ip in "$@"
do
        sed -i "/IP/ s/IP/$ip/" /home/secops/automation_tools/zap_automation/config.json
        python3 launchSpider.py
        python3 activeScan.py
        sed -i "/$ip/ s/$ip/IP/" /home/secops/automation_tools/zap_automation/config.json
done
rm *.html
./getReport.sh > web_application_scanner_report.html
cp web_application_scanner_report.html old_reports/webapp_$(date +"%d_%m_%y").html