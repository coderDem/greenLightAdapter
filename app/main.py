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
import subprocess
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = 'user'
    provider: Optional[str] = 'greenlight'


class Room(BaseModel):
    roomname: str
    email: str


@app.post('/user-create')
def create_user(user: User):
    command = 'docker exec greenlight-v2 bundle exec rake user:create[\"' + user.name + '\",\"' + user.email \
              + '\",\"' + user.password + '\",\"' + user.role + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@app.post('/user-delete')
def delete_user(user: User):
    command = 'docker exec greenlight-v2 bundle exec rake user:delete[\"' + user.email + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@app.post('/room-create')
def create_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:create[\"' + room.roomname + '\",\"' \
              + room.email + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@app.post('/room-delete')
def delete_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:delete[\"' + room.roomname + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@app.post('/room-share')
def create_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:share[\"' + room.roomname + '\",\"' \
              + room.email + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8007, reload=True)
