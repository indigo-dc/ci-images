FROM indigodatacloud/ci-images:base-u16
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y vim git openjdk-8-jdk build-essential dpkg-dev maven wget \
       software-properties-common quilt debhelper dpkg-dev fakeroot \
      && rm -rf /var/lib/apt/lists/*
      
      
EXPOSE 22 

CMD ["/usr/sbin/sshd", "-D"]


