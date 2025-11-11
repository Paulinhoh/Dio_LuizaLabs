from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from sqlalchemy.future import select
from pydantic import UUID4
from contrib.repository.dependencies import DatabaseDependecy
from categorias.schemas import CategoriaIn, CategoriaOut
from categorias.models import CategoriaModel

router = APIRouter()


@router.post(
    "/",
    summary="Criar uma nova Categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(db_session: DatabaseDependecy, categoria_in: CategoriaIn = Body(...)) -> CategoriaOut:  # type: ignore
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()

    return categoria_out


@router.get(
    "/",
    summary="Consultar todas as Categoria",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def query(db_session: DatabaseDependecy) -> list[CategoriaOut]:  # type: ignore
    categorias: list[CategoriaOut] = (await db_session.execute(select(CategoriaModel))).scalars().all()  # type: ignore

    return categorias


@router.get(
    "/{id}",
    summary="Consultar uma Categoria pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query(id: UUID4, db_session: DatabaseDependecy) -> CategoriaOut:  # type: ignore
    categoria: CategoriaOut = (await db_session.execute(select(CategoriaModel).filter_by(id=id))).scalars().first()  # type: ignore

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Categoria não encontrada no id {id}",
        )

    return categoria
