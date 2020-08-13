FROM indigodatacloud/ci-images:python


RUN pip install pygithub

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]

