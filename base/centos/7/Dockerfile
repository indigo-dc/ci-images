FROM centos:centos7
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN yum makecache fast \
    && yum install -y openssh-server \
                      sudo \
                      java-1.8.0-openjdk \
    && yum -y clean all 

# Jenkins sshd
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins
RUN mkdir /home/jenkins/.ssh &&\
    chmod 0700 /home/jenkins/.ssh &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC031xiODGimXMUdXNlFcGR5/MqUfRN65Gkwt29gszi9GFraZd300Gbxfknru4VsDpk0ULTg1z0A+pxpWanFTCnYW9cR1LlC7Cpw3L+p9Lu/TsjBJC0OsxHEr6p5frb85ChHJv381Vr1OIWmnDGrdSbbNLM3+UqtVARDDExl4+dQIJzzPFZZMpB2wZqWcR5uftlrat/4Zrew+4fQHNMAbGfUaa5TD94cXFmuFro3lzpbMjfKB0FlIBYtkYXkYqoRI8ujzN02icE4c4CocdBEFt2FbaT/9EtFeAltCxprZt5566f9uJIpJ1FR8DOOdrxnQTkw+r7cLEgh3kBUnIet5JX jenkins@jenkins-indigo" > /home/jenkins/.ssh/authorized_keys &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4t0v8CTpyV4FzP2xKaPTQ/Y2yjKbLqelWhJ5ZNy2bw/N9zpQMl/1xKGTz9j8TtLyEfaEcODxjbXCsc7XUwxB5SRp1yAiw2ddeFvACj9/Oyr2SYpHSMz9W+p0Pa0Dzi4+pd+w7qc9lXm1Ei8fLrZf17uyFJyQliobHh3vbWcTauJLs68ym3niY52wTjXbWxXGmERGU1F+Baue/LFta2RIP5Z+m7zWzqbFpECgYMbPCKDq8QRA6649B6f0qLmJOF1yALlKr8yfzuo48eLp8hyYE4gV8CQxr4L/aQUEeirEywGipiKsOIgsJCu88wDMsQHlP32ERLQfsjpLDTKod6Q6z jenkins@jenkins-egi" >> /home/jenkins/.ssh/authorized_keys &&\
    chown -R jenkins:jenkins /home/jenkins/.ssh
RUN echo "jenkins ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers

# sshd
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ecdsa_key -N ''
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N ''
RUN sed -i /etc/ssh/sshd_config \
        -e 's/#PermitRootLogin.*/PermitRootLogin no/' \
        -e 's/#RSAAuthentication.*/RSAAuthentication yes/'  \
        -e 's/#PasswordAuthentication.*/PasswordAuthentication no/' \
        -e 's/#SyslogFacility.*/SyslogFacility AUTH/' \
        -e 's/#LogLevel.*/LogLevel INFO/'
RUN mkdir -p /run/sshd

EXPOSE 22 

CMD ["/usr/sbin/sshd", "-D"]
