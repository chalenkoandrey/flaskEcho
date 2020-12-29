#!/bin/bash
kubectl apply -f flask-deployment.yml
kubectl expose deployment echoserver-deployment --port=5000 --type=LoadBalancer
minikube service list
