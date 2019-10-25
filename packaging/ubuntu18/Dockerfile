FROM indigodatacloud/ci-images:base-u18

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y git debhelper dpkg-dev\
                                                  maven \
                                                  build-essential \
                                                  devscripts fakeroot\
                                                  dh-python devscripts debhelper python-all-dev python-pbr python-setuptools \
    && rm -rf /var/lib/apt/lists/*

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
