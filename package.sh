#!/bin/zsh

# 应该放到jenkins
python setup.py build
python setup.py bdist_wheel --skip-build


