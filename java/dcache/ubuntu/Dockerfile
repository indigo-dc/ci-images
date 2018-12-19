FROM indigodatacloud/ci-images:base-u16
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  python-all python-all-dev python-pbr python-support \
                                                  python-pip \
						                                      python3-dev \
						                                      python-setuptools python-wheel \
						                                      devscripts build-essential debhelper \
                                                  libcurl4-gnutls-dev \
                                                  libffi-dev \
                                                  libssl-dev \
                                                  libxml2-dev \
                                                  libxslt1-dev \
						                                      libgnutls28-dev \
                                                  default-libmysqlclient-dev libsqlite3-dev \
						                                      curl \
                                                  wget \
                                                  maven dpkg-dev software-properties-common
      && rm -rf /var/lib/apt/lists/*
      
      
EXPOSE 22 

CMD ["/usr/sbin/sshd", "-D"]


