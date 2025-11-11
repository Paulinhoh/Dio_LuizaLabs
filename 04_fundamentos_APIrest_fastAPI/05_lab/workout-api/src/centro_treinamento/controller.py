from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from sqlalchemy import select
from pydantic import UUID4
from contrib.repository.dependencies import DatabaseDependecy
from centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from centro_treinamento.models import CentroTreinamentoModel

router = APIRouter()


@router.post(
    "/",
    summary="Criar um novo Centro de treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(db_session: DatabaseDependecy, centro_treinamento_in: CentroTreinamentoIn = Body(...)) -> CentroTreinamentoOut:  # type: ignore
    centro_treinamento_out = CentroTreinamentoOut(
        id=uuid4(), **centro_treinamento_in.model_dump()
    )
    centro_treinamento_model = CentroTreinamentoModel(
        **centro_treinamento_out.model_dump()
    )

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out


@router.get(
    "/",
    summary="Consultar todos os Centros de treinamentos",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependecy) -> list[CentroTreinamentoOut]:  # type: ignore
    centros_treinamento: list[CentroTreinamentoOut] = (await db_session.execute(select(CentroTreinamentoModel))).scalars().all()  # type: ignore

    return centros_treinamento


@router.get(
    "/{id}",
    summary="Consultar um Centro de treinamento pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CentroTreinamentoOut,
)
async def query(id: UUID4, db_session: DatabaseDependecy) -> CentroTreinamentoOut:  # type: ignore
    centro_treinamento: CentroTreinamentoOut = (await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()  # type: ignore

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Centro de treinamento não encontrada no id {id}",
        )

    return centro_treinamento
