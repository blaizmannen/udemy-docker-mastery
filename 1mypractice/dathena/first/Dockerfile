FROM centos:7
ENV container docker

RUN yum install openssh-server -y
RUN yum install sudo -y
RUN yum install python-setuptools -y
RUN yum install gcc -y
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
RUN useradd -ms /bin/bash dathena
RUN echo "dathena:dathena" | chpasswd
RUN usermod -aG wheel dathena
RUN echo 'root:toor' | chpasswd
CMD ["/usr/sbin/init"]