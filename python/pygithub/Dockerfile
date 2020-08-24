FROM indigodatacloud/ci-images:python

LABEL maintainer="davrodgon@users.noreply.github.com"

RUN pip install PyGithub

COPY *.py /usr/local/bin/
RUN chmod +x /usr/local/bin/*.py  

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
