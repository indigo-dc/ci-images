FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update
RUN apt-get -y install git python-pip

RUN git clone https://github.com/orviz/bashate -b find_files_in_directory /srv/bashate
WORKDIR /srv/bashate
RUN pip install .

WORKDIR /root
