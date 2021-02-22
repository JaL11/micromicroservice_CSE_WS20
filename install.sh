#!bin/bash

#creat chatbotservice directory
mkdir chatbotservice

#move root repository to chatbotservice
mv micromicroservice_CSE_WS20/* chatbotservice

#clone microservices-demo
echo "cloning microservices demo..."
git clone https://github.com/JaL11/microservices-demo

#move chatbotservice into microservices/src
echo "moving things around..."
mv chatbotservice microservices-demo/src/

#change directory to microservices-demo
echo "changing directory..."
cd microservices-demo
echo "to start cluster run 'skaffold run' but first make sure minikube is up and running with 'kubectl get nodes'!"

