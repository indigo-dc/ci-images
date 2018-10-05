FROM ubuntu:xenial
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

USER root

RUN apt-get update \
    && apt-get install --no-install-recommends -y openssh-server \
                                                  sudo \
                                                  openjdk-8-jdk \
    && rm -rf /var/lib/apt/lists/*

# Jenkins sshd
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins
RUN mkdir /home/jenkins/.ssh &&\
    chmod 0700 /home/jenkins/.ssh &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDse2yhEHShVq8PiTddtKcsOYuuxHrFJH0mBdPfA5pplGqFfgGC55nA81NCgTIBuKiTKWOp9jgPfDnM/GXvPE+lWqPNJZzgx4hpbDhkFfXjFNryTSVTjQUa3qCSA4DIWrX3uVSkLd52a1li1UH6F/NohYhiE77Y5Jd27W3U6yh6alQhRopH54CuAjb3F8tGRAjz4/65TUkWjdnnr/dX+hgoBkTgo55DFMcSQ7p17lcRULscSY8oEpmi6x4ReKQuXa+79PZD2hbT4CS/A/OpCj3CVpnhuDrvBAIbIiQipknrRnQuW3kD23/oHocadnFJEaV913QuRlmqL8LbjOkmrWm5 jenkins@indigo-jenkins.cern.ch" > /home/jenkins/.ssh/authorized_keys &&\
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
