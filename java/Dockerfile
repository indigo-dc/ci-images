FROM indigodatacloud/ci-images:base
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y git \
                                                  maven \
						  checkstyle \
                                                  wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/checkstyle/checkstyle/releases/download/checkstyle-8.13/checkstyle-8.13-all.jar -P /var/tmp/
RUN wget https://raw.githubusercontent.com/checkstyle/checkstyle/master/src/main/resources/google_checks.xml -P /var/tmp/

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
