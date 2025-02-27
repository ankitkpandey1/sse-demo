from typing import Generator
import time

from litestar.response.sse import ServerSentEvent
from litestar import Litestar, get
from litestar.config.cors import CORSConfig


def read_file() -> Generator[str, None, None]:
    with open("file.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(1)


@get("/")
async def get_text() -> ServerSentEvent:
    return ServerSentEvent(content=read_file())

cors_config = CORSConfig(allow_origins=["http://localhost:5173"], allow_credentials=True)
app = Litestar([get_text], cors_config=cors_config)
