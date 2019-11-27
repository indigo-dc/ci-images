FROM indigodatacloud/ci-images:base-u18
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  python3.6 python3-dev python-pip \
						  python-setuptools python-wheel \
						  build-essential \
                                                  libcurl4-gnutls-dev \
                                                  libffi-dev \
                                                  libssl-dev \
                                                  libxml2-dev \
                                                  libxslt1-dev \
						  libgnutls28-dev \
                                                  default-libmysqlclient-dev libsqlite3-dev \
						  curl \
						  tox flake8 pylint pydocstyle pep8 bandit \
						  twine \
    && rm -rf /var/lib/apt/lists/*

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
