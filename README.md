ireaders
====

Features
--------
* package.sh ������Ӧ�÷ŵ�jenkins��ʵ��

Build image:
----
1. ����sh package.sh ����whl��
2. ���� docker build -t ireaders:0.2 . �����ɾ��񣬰汾��Ӧ����versioneer����

Run:
---
* gunicorn -b 0.0.0.0:11294 -k uvicorn.workers.UvicornWorker -w 1 ireaders.main:app --access-logfile -
