FROM centos/python-38-centos7
USER root
WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
&&  rm -f /tmp/requirements.txt

COPY ./dist/* /tmp/build/

RUN pip install \
    /tmp/build/*  \
&&  rm -rf /tmp/build

# 默认暴露端口
EXPOSE 11294

# 启动命令
CMD ["gunicorn", "-b", "0.0.0.0:11294", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "ireaders.main:app", "--access-logfile", "-"]

