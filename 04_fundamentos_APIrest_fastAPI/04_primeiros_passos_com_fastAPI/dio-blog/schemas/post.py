from pydantic import BaseModel
from datetime import datetime, UTC


class PostIN(BaseModel):
    title: str
    data: datetime = datetime.now(UTC)
    published: bool = False
