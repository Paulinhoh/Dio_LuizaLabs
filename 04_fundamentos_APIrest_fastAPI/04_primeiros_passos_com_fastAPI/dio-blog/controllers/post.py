from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Response, Cookie, status, Header
from schemas.post import PostIN
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {
        "title": f"criando uma aplicação com Django",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": f"internacionalizando um app FastAPI",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": f"criando uma aplicação com Flask",
        "date": datetime.now(UTC),
        "published": True,
    },
    {
        "title": f"internacionalizando um app Starlett",
        "date": datetime.now(UTC),
        "published": False,
    },
]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIN):
    fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response,
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    # def read_posts(published: bool, skip: int = 0, limit: int = len(fake_db)):
    response.set_cookie(
        key="user", value="email@example.com"
    )  # setando um Cookie caso precise
    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")
    return [
        post for post in fake_db[skip : skip + limit] if post["published"] is published
    ]  # código abaixo faz a mesma coisa
    # posts = []
    # for post in fake_db:
    #     if len(post) == limit:
    #         break
    #     if post["published"] is published:
    #         posts.append(post)

    # return posts


@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {
                "title": f"criando uma aplicação com {framework}",
                "date": datetime.now(UTC),
            },
            {
                "title": f"internacionalizando um app {framework}",
                "date": datetime.now(UTC),
            },
        ]
    }
