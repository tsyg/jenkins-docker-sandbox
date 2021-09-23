
# SandBox

## Intro

Use it on your computer to play with Docker, Jenkins - without any risk to impact client. A place to play safe.


## Setting up (Any OS)

1. Clone this repository into your directory for the SandBox , e.g.:
D:\YOUR\DIRECTORY> git clone https://github.com/tsyg/jenkins-docker-sandbox.git

### On Windows

1. Download docker - e.g. from https://www.docker.com/products/docker-desktop  and install it

1. in console 

D:\YOUR\DIRECTORY> cd jenkins-docker-sandbox\jenkins

D:\YOUR\DIRECTORY\jenkins-docker-sandbox> git checkout master

1. # Build the image and run 
jenkins> docker-compose up --build

##################  Alternative:

1. # Build image and tag it as docker-nice-sandbox with version 01

> docker build -t docker-nice-sandbox:01 .
 

D:\YOUR\DIRECTORY\jenkins-docker-sandbox> docker images
REPOSITORY            TAG       IMAGE ID       CREATED         SIZE
docker-nice-sandbox   01        5ff8c20d0ec0   2 minutes ago   1.11GB




1. # run Jenkins - it uses port 8080 - so specifying it to make available

docker run -p 8080:8080 --name jenkins-nice-container docker-nice-sandbox:01
 
############## End-Of-Alternative 
 
 
1. Unlock Jenkins - copy-paste password from console into
1. Customize Jenkins: - click "Install Suggested plugins"




******  Cleanup

In docker-Desktop
 - Stop and delete the container: Containers/Apps > Stop button;  wait, Delete button; 
 - Delete the image:    click "..." > Remove
 
 
  
