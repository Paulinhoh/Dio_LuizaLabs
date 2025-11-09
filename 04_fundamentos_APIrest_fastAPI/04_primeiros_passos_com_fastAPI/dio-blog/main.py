from fastapi import FastAPI
from pydantic import BaseModel

from controllers import post

app = FastAPI()
app.include_router(post.router)


# =-=-=-=-=-=-=-=-=-=-=-=-=-= Código de exemplo =-=-=-=-=-=-=-=-=-=-=-=-=-=
class Foo(BaseModel):
    bar: str
    message: str


# Foo tb pode ser passado na função, mas passando pelo response_model é melhor
# def minha_def() -> Foo:
@app.get("/foobar/", response_model=Foo)
def foobar() -> dict[str, str]:
    return {"bar": "foo", "message": "helo world"}
