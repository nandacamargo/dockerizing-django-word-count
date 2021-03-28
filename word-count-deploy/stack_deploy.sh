#Initialize Swarm
docker swarm init 

#Create the stack
docker stack deploy --compose-file docker-compose.yml word-count-stack
