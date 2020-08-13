FROM indigodatacloud/ci-images:python

LABEL maintainer="davrodgon@users.noreply.github.com"

RUN pip install PyGithub

COPY getRepoLicense.py /usr/local/bin/getRepoLicense.py 
RUN chmod +x /usr/local/bin/getRepoLicense.py  

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
