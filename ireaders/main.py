#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author：Ginta
# time:2021/9/9
# email: 775650117@qq.com
import logging

import uvicorn

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

logging.basicConfig(format='%(asctime)s %(levelname)s %(process)d %(message)s')
logger = logging.getLogger("ireaders")

app = FastAPI(
    title='IREADERS',
    description='reader',
    default_response_class=ORJSONResponse)


@app.on_event("startup")
async def on_startup():
    logger.info('ireaders startup success!!')


@app.on_event("shutdown")
async def on_shutdown():
    logger.info('ireaders shutdown success!!')


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=11294)
