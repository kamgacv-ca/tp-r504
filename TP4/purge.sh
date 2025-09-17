docke stop 
docker rm $(docker ps -aq)

docker network prune 
docker volume prune 

#ou docker system prune
