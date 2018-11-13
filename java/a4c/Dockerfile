FROM indigodatacloud/ci-images:java
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y curl \
						  software-properties-common \
    && rm -rf /var/lib/apt/lists/*
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update \
    && apt-get install --no-install-recommends -y nodejs \
						  ruby \
						  ruby-dev \
						  gcc \
						  g++ \
						  make \
    && rm -rf /var/lib/apt/lists/*
RUN npm -g install bower
RUN npm -g install grunt-cli
RUN gem install compass
RUN npm install grunt-contrib-compass --save-dev

RUN git clone https://github.com/indigo-dc/alien4cloud-deep /tmp/alien4cloud-deep
WORKDIR /tmp/alien4cloud-deep/a4c
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN mvn clean install

WORKDIR /root
# ugly
RUN cp -r .m2 /home/jenkins/ \
    && chown jenkins:jenkins /home/jenkins/.m2 -R 

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]

