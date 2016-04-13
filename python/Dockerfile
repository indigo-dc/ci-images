FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update
RUN apt-get -y install git python python-flake8 python-tox
RUN wget https://raw.githubusercontent.com/openstack-infra/project-config/master/jenkins/scripts/run-pep8.sh -O /usr/bin/run-pep8.sh
RUN chmod +x /usr/bin/run-pep8.sh
