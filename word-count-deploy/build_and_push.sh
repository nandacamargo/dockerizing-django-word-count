
#Build the application
docker-compose build

#Push the built image to dockerhub
#docker push ${REGISTRY_USER}/web_wordcount

#Starts application
docker-compose up
