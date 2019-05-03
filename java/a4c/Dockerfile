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

RUN git clone https://github.com/indigo-dc/alien4cloud -b 2.1.0-UPV-1.0.0 /tmp/alien4cloud
WORKDIR /tmp/alien4cloud/
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN mvn clean install -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true

WORKDIR /root
# ugly
RUN cp -r .m2 /home/jenkins/ \
    && chown jenkins:jenkins /home/jenkins/.m2 -R 

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]

