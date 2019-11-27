FROM indigodatacloud/ci-images:python3.6
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

ENV REQS_PATH /tmp/requirements.txt

RUN apt-get update \
    && apt-get install --no-install-recommends -y make \
                                                  git \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt $REQS_PATH
RUN pip install -r $REQS_PATH
RUN pip install git+https://github.com/deephdc/schema4apps

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]

