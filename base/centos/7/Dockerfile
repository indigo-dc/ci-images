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
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDse2yhEHShVq8PiTddtKcsOYuuxHrFJH0mBdPfA5pplGqFfgGC55nA81NCgTIBuKiTKWOp9jgPfDnM/GXvPE+lWqPNJZzgx4hpbDhkFfXjFNryTSVTjQUa3qCSA4DIWrX3uVSkLd52a1li1UH6F/NohYhiE77Y5Jd27W3U6yh6alQhRopH54CuAjb3F8tGRAjz4/65TUkWjdnnr/dX+hgoBkTgo55DFMcSQ7p17lcRULscSY8oEpmi6x4ReKQuXa+79PZD2hbT4CS/A/OpCj3CVpnhuDrvBAIbIiQipknrRnQuW3kD23/oHocadnFJEaV913QuRlmqL8LbjOkmrWm5 jenkins@indigo-jenkins.cern.ch" > /home/jenkins/.ssh/authorized_keys &&\
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
