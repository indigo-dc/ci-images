FROM indigodatacloud/ci-images:base-c7
MAINTAINER Pablo Orviz <orviz@ifca.unican.es>

RUN yum makecache fast \
    && yum install -y findutils \
                      java-1.8.0-openjdk \
                      java-1.8.0-openjdk-devel \
                      openssh-clients \
                      httpd-tools \
                      tcpdump \
                      wget \
                      redhat-lsb-core \
    && yum -y clean all 

# build-environment
COPY build_env.txt /tmp/ 
RUN xargs yum -y install < /tmp/build_env.txt    

# dcache maven specific
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
RUN yum -y update && yum install -y apache-maven


EXPOSE 22 

CMD ["/usr/sbin/sshd", "-D"]

