FROM indigodatacloud/ci-images:base-u18
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  python3.6 python3-dev python-pip \
						  python-setuptools python-wheel \
                                                  python3-wheel python3-pip python3-venv \
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
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 10
# otherwise issues with twine<=1.10.0 
RUN pip install twine==1.11.0 
RUN pip install -U wheel setuptools

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
