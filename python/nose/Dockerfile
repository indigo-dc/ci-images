FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get clean
RUN apt-get update
RUN apt-get -y install wget git python python-dev python-pip libcurl4-gnutls-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev
RUN apt-get -y install libmysqlclient-dev libsqlite3-dev
RUN pip install tox flake8 pylint pydocstyle nose nosexcover mock
RUN pip install ply PyYAML cpyutils # clues
RUN pip install -egit+https://github.com/indigo-dc/tosca-parser@master#egg=tosca-parser netaddr requests backports.ssl_match_hostname # im
RUN wget https://raw.githubusercontent.com/openstack-infra/project-config/master/jenkins/scripts/run-pep8.sh -O /usr/bin/run-pep8.sh
RUN chmod +x /usr/bin/run-pep8.sh

# clues
RUN export DEBIAN_FRONTEND=noninteractive && apt-get -y install htcondor
