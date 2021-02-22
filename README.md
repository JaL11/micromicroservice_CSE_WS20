# micromicroservice_CSE_WS20
WS20 CSE microservice implimentation with the GCP/microservices-demo

### Installation
This repository is based on a [fork](https://github.com/JaL11/microservices-demo) and in order to fully test it's functionality it needs to be run using the install script install.sh

This project was created to run on a Linux operating system and [Arch Linux](archlinux.org) was used for testing purposes.

Chatbot can be run using [Docker] within the projects root directory using:
(-t is optional but useful for keeping track of docker containers)
```
docker build -t chatbot_image .
```
Then run with:
```
docker run -d --name chatbot chatbot_image:latest
```
Using `docker ps` it is then possible to view the running container.

For further evaluation of the running container run:
```
docker exec chatbot cat logs.txt
```
to see that status of the chatbot engine
```
docker exec chatbot /bin/grpc_health_probe -addr=:9090
```
can also be used to check the containers health using the [grpc-health-probe](https://github.com/grpc-ecosystem/grpc-health-probe)

### Technology decisions:

#### Communication:
Weekly social distanced meetings per Video calls: [Jitsi](https://www.jitsi.org)

Communication: [Telegram](https://www.telegram.org)


#### Project development:
Kanban: [clubhouse.io](https://www.clubhouse.io)



#### Roles:
Developer-Backend: Oliver

Developer-Frontend: Florian

DevOps: James


(Scrum Master / Product Owner: Florian)
