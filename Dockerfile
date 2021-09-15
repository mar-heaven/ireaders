FROM centos/python-38-centos7

ARG PKG
COPY requirements.txt /tmp
RUN pip3 install -i https://pypi.douban.com/simple -r /tmp/requirements.txt
COPY PKG /tmp
RUN pip3 install /tmp/${PKG}

RUN rm -rf /tmp/*
