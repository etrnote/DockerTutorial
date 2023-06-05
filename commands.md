docker pull redis
docker pull postgres

docker images

docker run redis (start container)
docker ps = list running containers
docker ps -a (running and stopped containers)

docker run -d redis (ditached, background)
docker stop = stop the container
docker start id = starts stopped container

suppose you ened to redis version

docker run redis:4.0
but conflict!
container port vs host port
multiple containers can run on your host machine
we need to bind laptop port to container port
conflict when same port on host machine

before binding - they are unusable

**start with binding**
docker run -p6000:6379
(local:container)


docker run -d -p6001:6379 --name name redis:40
---


#### logs
docker logs <container id> / <name>.0

docker exec -it <id> /bin/bash