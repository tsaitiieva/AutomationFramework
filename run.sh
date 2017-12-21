#!/usr/bin/env bash
#py.test --alluredir=reports /test_api.py  --platform=api
py.test ./Tests/test_api.py  --platform=api --server=qa
#allure serve reports
