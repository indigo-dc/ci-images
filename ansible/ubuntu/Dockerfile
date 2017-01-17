FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update
RUN apt-get -y install git python-pip python-apt python-dev
RUN apt-get -y install libffi-dev 

RUN sed -i '/Defaults *requiretty/s/^/#/' /etc/sudoers
RUN sed -i '/root\tALL=/a jenkins ALL=(ALL) NOPASSWD: ALL' /etc/sudoers

RUN pip install ansible==2.1
