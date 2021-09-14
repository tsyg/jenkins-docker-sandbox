
# SandBox

## Intro

Use it on your computer to play with Docker, Jenkins - without any risk to impact client. A place to play safe.


## Setting up (Any OS)

1. Clone this repository into your directory for the SandBox , e.g.:
D:\YOUR\DIRECTORY> git clone https://github.com/tsyg/jenkins-docker-sandbox.git

### On Windows

1. Download docker - e.g. from https://www.docker.com/products/docker-desktop  and install it

1. in console 

D:\YOUR\DIRECTORY> cd jenkins-docker-sandbox

D:\YOUR\DIRECTORY\jenkins-docker-sandbox> git checkout master

 

1. # Build image:

 

> docker build .

 

1. tag it as docker-nice-sandbox01 with version 01

 

D:\YOUR\DIRECTORY\jenkins-docker-sandbox> docker images

REPOSITORY   TAG       IMAGE ID       CREATED          SIZE

<none>       <none>    a886d0ac9a3c   14 seconds ago   1.11GB

alpine/git   latest    b8f176fa3f0d   3 months ago     25.1MB

D:\YOUR\DIRECTORY\jenkins-docker-sandbox> docker tag a886d0ac9a3c docker-nice-sandbox01:01

 

1. # run Jenkins - it uses port 8080 - so specifying it to make available

docker run -p 8080:8080  --name jenkins-nice-sandbox-Container docker-nice-sandbox01:01

 
