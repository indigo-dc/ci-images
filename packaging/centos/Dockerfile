FROM centos:centos7

RUN yum makecache fast \
    && yum install -y openssh-server \
                      sudo \
                      findutils \
                      java-1.8.0-openjdk \
    && yum -y clean all 

# Jenkins sshd
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins
RUN mkdir /home/jenkins/.ssh &&\
    chmod 0700 /home/jenkins/.ssh &&\
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9Pyyw2riOeSUPiFwRfFUqRQCauQdcOXYGZkD7V05L4BNFRlmg1+BuiHgOZ64zMYDblRL2NZXgb1f+dddWn0jkUyzEbuNfmVDiodQ0lf/5d1zzzEs2cW5PNF4isp4S5cXaWb7XvtbXY44ry+Pux8YXHa+zSBC07bJ4FAZV/+Qg+3Mo7PfEJl+7n6BpSFd+oiAxeCGlrjjqTQrr/2Jo8Y3FG0ACAdwMKGs0dAA0+LMwgTJz5uTo5cFxICYFicQ6VpYf3r7xGYx3fW6LuWQmHv8WMktFqCwOYQsU1PfAZRwhLRGEOnSCFg/0MrKppuhOtmF/I79GSZ5E7A/ODW9Q+pbr root@enkins.indigo-datacloud.eu:8080" > /home/jenkins/.ssh/authorized_keys &&\
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

# build-environment
COPY build_env.txt /tmp/ 
RUN xargs yum -y install < /tmp/build_env.txt

EXPOSE 22 

CMD ["/usr/sbin/sshd", "-D"]
