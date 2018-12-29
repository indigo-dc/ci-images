FROM indigodatacloud/ci-images:base-u16

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y git \
                                                  maven \
                                                  build-essential \
                                                  devscripts \
    && rm -rf /var/lib/apt/lists/*

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
