import subprocess
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

from core.config import LOG_PATH

router = APIRouter()


class User(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = 'user'
    provider: Optional[str] = 'greenlight'


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    command = 'docker exec greenlight-v2 bundle exec rake user:create[\"' + user.name + '\",\"' + user.email \
              + '\",\"' + user.password + '\",\"' + user.role + '\"] /bin/bash',
    with open(LOG_PATH, "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return


@router.post("/delete/", status_code=status.HTTP_201_CREATED)
async def delete_user(useremail: str):
    command = 'docker exec greenlight-v2 bundle exec rake user:delete[\"' + useremail + '\"] /bin/bash',
    with open(LOG_PATH, "a") as output:
        subprocess.check_output(command, shell=True, stdin=output, stderr=output)
        return
