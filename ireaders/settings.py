#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author：Ginta
# time:2021/9/9
# email: 775650117@qq.com
from typing import Optional
from pydantic import BaseSettings
import logging


class AppSettings(BaseSettings):
    mongo_uri: str


settings = AppSettings()
logging.info('='*20)
logging.info(settings.dict())
