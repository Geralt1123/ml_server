from uuid import UUID

from fastapi import (
    APIRouter,
    Depends, Body, Query,
)
from dependency_injector.wiring import inject, Provide
from pydantic import RootModel

from interfaces import Service
from web.api.containers import PredictControllerContainer


class DataModel(RootModel):
    root: list[list[float]]


router = APIRouter(prefix="/predict", tags=["Predict"])


@router.post(path="/predict_image", summary="Распознавание изображения")
@inject
async def file_predict(
    file: DataModel = Body(),
    controller: Service = Depends(Provide[PredictControllerContainer.predict_file_controller])
):
    return await controller(file)


@router.post(path="/predict_image_2", summary="Распознавание изображения")
@inject
async def file_predict_2(
    file: DataModel = Body(),
    controller: Service = Depends(Provide[PredictControllerContainer.predict_file_controller_2])
):
    return await controller(file)
