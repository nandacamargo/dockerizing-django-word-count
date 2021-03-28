#Initialize Swarm
docker swarm init

#Create the stack
docker stack deploy --compose-file docker-compose-prod.yml word-count-stack
