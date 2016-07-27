FROM evarga/jenkins-slave
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

#RUN apt-get clean
RUN apt-get update
RUN apt-get -y install git python-pip

RUN pip install pytz
RUN git clone https://github.com/orviz/bashate -b find_files_in_directory /srv/bashate
WORKDIR /srv/bashate
RUN pip install .

# shunit, kcov
RUN apt-get -y install shunit2 jq cmake g++ pkg-config zlib1g zlib1g-dev libcurl3-dev libelf-dev elfutils libdw-dev python libstdc++6-4.7-dev binutils-dev ruby
WORKDIR /tmp
RUN git clone https://github.com/SimonKagstrom/kcov
RUN cd kcov && cmake . && make && make install

WORKDIR /root
