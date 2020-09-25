import subprocess

from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

router = APIRouter()


class Room(BaseModel):
    roomname: str
    email: str


@router.post("/delete/", status_code=status.HTTP_201_CREATED)
async def delete_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:delete[\"' + room.roomname + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@router.post("/share/", status_code=status.HTTP_201_CREATED)
async def create_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:share[\"' + room.roomname + '\",\"' \
              + room.email + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:create[\"' + room.roomname + '\",\"' \
              + room.email + '\"] /bin/bash',
    with open("/tmp/output.log", "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return
