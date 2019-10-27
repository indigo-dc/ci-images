FROM indigodatacloud/ci-images:base
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y git \
                                                  maven \
						  checkstyle \
                                                  wget \
						  openjdk-8-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/checkstyle/checkstyle/releases/download/checkstyle-8.13/checkstyle-8.13-all.jar -P /var/tmp/
RUN wget https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml -P /var/tmp/

COPY nexus-settings.xml /tmp/
RUN mkdir /home/jenkins/.m2 && mv /tmp/nexus-settings.xml /home/jenkins/.m2/settings.xml &&\
    chown -R jenkins:jenkins /home/jenkins/.m2

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
