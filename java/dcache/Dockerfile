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
                      unzip \
                      git\
    && yum -y clean all 
    
ENV JAVA_HOME /usr/bin/java/java-1.8.0-openjdk.x86_64
RUN export JAVA_HOME

# dcache maven specific
RUN wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
RUN yum -y update && yum install -y apache-maven


EXPOSE 22 

CMD ["/usr/sbin/sshd", "-D"]

