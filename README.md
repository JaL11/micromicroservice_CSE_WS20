# micromicroservice_CSE_WS20
WS20 CSE microservice implimentation with the GCP/microservices-demo
This implementation offers a Chatbot written in Python using State of the art NLP library [spacy](https://github.com/explosion/spaCy)
and a custom from scratch trained language model.

## Features

- Chatbot that you can talk to!
- Supports the english language
- Server that runs over GRPC
- Custom pretrained Convolutional Neural Network Model for the online shop
- State-of-the-art speed
- Deployment ready
- Live updated monitoring for CPU, RAM and performance time
- Scalable, expandable

While we offer custom model that was specifically generated for this task, it is by no way perfect and is meant to be used as a base model that is supposed to be expanded and improved. All the necessary files to create and expand this model are found in `models\` where the chatette.txt can be expanded to generate better Training data for the machine learning model. As of the moment the model only supports the actions Help, Welcome(small talk) and Fun fact, while shopping recommendation is implemented, the trainingdata for the model must be adjusted for it to classify that correctly.

More information how the code itself works and runs can be seen inside the files as all have been documented with PEP8 in mind and Google style docstrings that describe their functionality.
If you want to manually start this application `chhatbot_server.py` is where the magic happens! However we do recommend using this in a kubernetes environments, as it was developed with that in mind, see below for further information for that.

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

## Running chatbot integrated in the kubernetes microservices demo

#### Install script
Installing the project to run using kubernetes together with the demo project 

Due to the use of two repositories the installation process is a bit unsual.
Before running the install script move the project repository (micromicroservice_CSE_WS20) to a new folder for example chatbot_demo
the command `mkdir ../chatbot_demo` could be used to creat such a folder and then copy the micromicroservice_CSE_WS20 to the new folder for example with 
```
cd ../ && mv micromicroservice_CSE_WS20 chatbot_demo/
```
At that point run:
```
./micromicroservice_CSE_WS20/install.sh
```

The install script clones the demo fork and moves this repository into the `microservices-demo/src/` folder


After minikube is installed and correctly configured, start a new minikube node with
```
minikube start --cpus=4 --memory=4096 --disk-size 32g
```
then start the local cluster using skaffold
```
skaffold run
```
### Troubleshooting
Sometimes when running skaffold run the message `13/13 deployments failed` will appear.
if this happens just rerun `skaffold run` and everything should be working after that.

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

