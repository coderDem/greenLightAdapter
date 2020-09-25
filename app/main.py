#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# greenLightAdapter - automation tool for Greenlight
# copyright Ivan Demin 2020
#
# This file is part of greenLightAdapter
# greenLightAdapter is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# You should have received a copy of the GNU General Public License along with Foobar.  If not, see <https://www.gnu.org/licenses/>.
#
# example nginx config:
# location /greenLightAdapter {
# rewrite ^/app/(.*) /$1 break;
# proxy_pass http://127.0.0.1:8007
# proxy_set_header Host $host;
# proxy_set_header X-Real-IP ip_address;
# }

import uvicorn
from fastapi import FastAPI

from api.api import api_router
from core.config import PROJECT_NAME, API_PREFIX

app = FastAPI(title=PROJECT_NAME)

app.include_router(api_router, prefix=API_PREFIX)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8007, reload=True)

