FROM indigodatacloud/ci-images:base
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN apt-get update \
    && apt-get install --no-install-recommends -y wget \
                                                  git \
                                                  python python-dev python-pip \
						  build-essential \
                                                  libcurl4-gnutls-dev \
                                                  libffi-dev \
                                                  libssl-dev \
                                                  libxml2-dev \
                                                  libxslt1-dev \
                                                  default-libmysqlclient-dev libsqlite3-dev \
						  curl \
						  tox flake8 pylint pydocstyle pep8 bandit \
    && rm -rf /var/lib/apt/lists/*

# We need:
#
# tox>=2.7.0 to avoid errors when not including 'commands' in [testenv] section
#	https://github.com/tox-dev/tox/issues/454
# virtualenv>=16.0.0 to avoid failures when executing tox within an absolute path
#		     containing whitespaces
#	https://github.com/tox-dev/tox/issues/121
RUN pip install tox==2.7.0
# Add tox binary to $PATH
ENV PATH="${PATH}:/usr/local/bin"

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
