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
from http.client import HTTPException

import uvicorn
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from starlette.responses import RedirectResponse, JSONResponse
from starlette.status import HTTP_403_FORBIDDEN

from api.api import api_router
from core.config import PROJECT_NAME, API_PREFIX, API_KEY_NAME, API_KEY, COOKIE_DOMAIN

app = FastAPI(title=PROJECT_NAME, docs_url=None, redoc_url=None)

app.include_router(api_router, prefix=API_PREFIX)

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_query: str = Security(api_key_query),
        api_key_header: str = Security(api_key_header),
        api_key_cookie: str = Security(api_key_cookie),
):
    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )


@app.get("/")
async def homepage():
    return "Welcome to the security test!"


@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = JSONResponse(
        get_openapi(title="FastAPI security test", version=1, routes=app.routes)
    )
    return response


@app.get("/documentation", tags=["documentation"])
async def get_documentation(api_key: APIKey = Depends(get_api_key)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")
    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response


@app.get("/logout")
async def route_logout_and_remove_cookie():
    response = RedirectResponse(url="/")
    response.delete_cookie(API_KEY_NAME, domain=COOKIE_DOMAIN)
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8007, reload=True)
