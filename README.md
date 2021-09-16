ireaders
====

Features
--------
* package.sh 的内容应该放到jenkins中实现

Build image:
----
1. 运行sh package.sh 生成whl包
2. 运行 docker build -t ireaders:0.2 . 来生成镜像，版本号应该由versioneer生成

Run:
---
* gunicorn -b 0.0.0.0:11294 -k uvicorn.workers.UvicornWorker -w 1 ireaders.main:app --access-logfile -
