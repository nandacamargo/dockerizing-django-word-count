
#Save logs to a file
currTime=$(date +%Y%m%d%H%M%S)
logFile="docker_log_$currTime.log"
echo "File $logFile created"

docker-compose logs -f -t >> mywordcount/logs/$logFile
