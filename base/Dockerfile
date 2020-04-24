FROM openjdk:8-jdk
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y openssh-server sudo \
    && rm -rf /var/lib/apt/lists/*

# openjdk in jenkins user path
RUN echo "export PATH=$JAVA_HOME/bin:$PATH" >> /etc/profile

# Jenkins sshd
RUN useradd -m -u 1001 -d /home/jenkins -s /bin/sh jenkins
RUN mkdir /home/jenkins/.ssh &&\
    chmod 0700 /home/jenkins/.ssh &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC031xiODGimXMUdXNlFcGR5/MqUfRN65Gkwt29gszi9GFraZd300Gbxfknru4VsDpk0ULTg1z0A+pxpWanFTCnYW9cR1LlC7Cpw3L+p9Lu/TsjBJC0OsxHEr6p5frb85ChHJv381Vr1OIWmnDGrdSbbNLM3+UqtVARDDExl4+dQIJzzPFZZMpB2wZqWcR5uftlrat/4Zrew+4fQHNMAbGfUaa5TD94cXFmuFro3lzpbMjfKB0FlIBYtkYXkYqoRI8ujzN02icE4c4CocdBEFt2FbaT/9EtFeAltCxprZt5566f9uJIpJ1FR8DOOdrxnQTkw+r7cLEgh3kBUnIet5JX jenkins@jenkins-indigo" > /home/jenkins/.ssh/authorized_keys &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4t0v8CTpyV4FzP2xKaPTQ/Y2yjKbLqelWhJ5ZNy2bw/N9zpQMl/1xKGTz9j8TtLyEfaEcODxjbXCsc7XUwxB5SRp1yAiw2ddeFvACj9/Oyr2SYpHSMz9W+p0Pa0Dzi4+pd+w7qc9lXm1Ei8fLrZf17uyFJyQliobHh3vbWcTauJLs68ym3niY52wTjXbWxXGmERGU1F+Baue/LFta2RIP5Z+m7zWzqbFpECgYMbPCKDq8QRA6649B6f0qLmJOF1yALlKr8yfzuo48eLp8hyYE4gV8CQxr4L/aQUEeirEywGipiKsOIgsJCu88wDMsQHlP32ERLQfsjpLDTKod6Q6z jenkins@jenkins-egi" >> /home/jenkins/.ssh/authorized_keys &&\
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

# locales
RUN apt-get update \
    && apt-get install --no-install-recommends -y locales \
    && rm -rf /var/lib/apt/lists/*
RUN locale-gen en_US.UTF-8 

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
