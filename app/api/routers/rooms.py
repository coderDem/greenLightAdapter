import subprocess

from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

from core.config import LOG_PATH

router = APIRouter()


class Room(BaseModel):
    roomname: str
    email: str


class DeleteRoom(BaseModel):
    roomname: str


class ShareRoom(BaseModel):
    roomname: str
    useremail: str


@router.post("/delete/", status_code=status.HTTP_201_CREATED)
async def delete_room(deleteroom: DeleteRoom):
    command = '	docker exec greenlight-v2 bundle exec rake room:delete[\"' + deleteroom.roomname + '\"] /bin/bash',
    with open(LOG_PATH, "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@router.post("/share/", status_code=status.HTTP_201_CREATED)
async def share_room(shareroom: ShareRoom):
    command = '	docker exec greenlight-v2 bundle exec rake room:share[\"' + shareroom.roomname + '\",\"' \
              + shareroom.useremail + '\"] /bin/bash',
    with open(LOG_PATH, "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_room(room: Room):
    command = '	docker exec greenlight-v2 bundle exec rake room:create[\"' + room.roomname + '\",\"' \
              + room.email + '\"] /bin/bash',
    with open(LOG_PATH, "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return
