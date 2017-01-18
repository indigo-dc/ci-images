FROM orviz/umd-jenkins-slave:centos7
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

# hack
RUN rm -rf /usr/lib64/python2.7/site-packages/pycrypto-2.6.1-py2.7.egg-info
RUN yum -y install git python-pip python-dev

RUN pip install ansible==2.1
RUN pip uninstall requests
