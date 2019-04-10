FROM openjdk:8-jdk
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y openssh-server sudo \
    && rm -rf /var/lib/apt/lists/*

# Jenkins sshd
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins
RUN mkdir /home/jenkins/.ssh &&\
    chmod 0700 /home/jenkins/.ssh &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC031xiODGimXMUdXNlFcGR5/MqUfRN65Gkwt29gszi9GFraZd300Gbxfknru4VsDpk0ULTg1z0A+pxpWanFTCnYW9cR1LlC7Cpw3L+p9Lu/TsjBJC0OsxHEr6p5frb85ChHJv381Vr1OIWmnDGrdSbbNLM3+UqtVARDDExl4+dQIJzzPFZZMpB2wZqWcR5uftlrat/4Zrew+4fQHNMAbGfUaa5TD94cXFmuFro3lzpbMjfKB0FlIBYtkYXkYqoRI8ujzN02icE4c4CocdBEFt2FbaT/9EtFeAltCxprZt5566f9uJIpJ1FR8DOOdrxnQTkw+r7cLEgh3kBUnIet5JX jenkins@jenkins-indigo" > /home/jenkins/.ssh/authorized_keys &&\
    chown -R jenkins:jenkins /home/jenkins/.ssh
RUN echo "jenkins ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers

# sshd
RUN sed -i /etc/ssh/sshd_config \
        -e 's/#PermitRootLogin.*/PermitRootLogin no/' \
        -e 's/#RSAAuthentication.*/RSAAuthentication yes/'  \
        -e 's/#PasswordAuthentication.*/PasswordAuthentication no/' \
        -e 's/#SyslogFacility.*/SyslogFacility AUTH/' \
        -e 's/#LogLevel.*/LogLevel INFO/'
RUN mkdir -p /run/sshd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
