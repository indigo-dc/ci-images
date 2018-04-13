FROM indigodatacloud/ci-images:base

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  python python-dev python-pip \
                                                  libcurl4-gnutls-dev \
                                                  libffi-dev \
                                                  libssl-dev \
                                                  libxml2-dev \
                                                  libxslt1-dev \
                                                  default-libmysqlclient-dev libsqlite3-dev \
						  curl \
						  tox flake8 pylint pydocstyle pep8 bandit \
    && rm -rf /var/lib/apt/lists/*

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]


