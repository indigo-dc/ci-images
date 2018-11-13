FROM indigodatacloud/ci-images:base
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y git \
                                                  wget \
    && rm -rf /var/lib/apt/lists/*

# Deploy go1.5
WORKDIR /tmp
RUN wget https://storage.googleapis.com/golang/go1.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xvf go1.5.linux-amd64.tar.gz
RUN echo "export PATH=\$PATH:/usr/local/go/bin" >> ~/.bashrc

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
