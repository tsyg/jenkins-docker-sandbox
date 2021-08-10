FROM jenkins/jenkins:2.277.2-lts-jdk11
USER root
RUN apt-get update && apt-get install -y apt-transport-https \
       ca-certificates curl gnupg2 \
       software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88
RUN add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) stable"
RUN apt-get update && apt-get install -y docker-ce-cli
#USER jenkins
#RUN mkdir -p /tmp/rep ; chown -R jenkins:jenkins /tmp/rep ; chown -R jenkins:jenkins /var/run
VOLUME ["/tmp/rep"]
VOLUME ["/var/run"]
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
#USER jenkins
RUN jenkins-plugin-cli --plugins "blueocean:1.24.5 docker-workflow:1.26"
