from api.schema import Image
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .services.service import service_detect_face

router = APIRouter(
    prefix="/api/v1",
    tags=['FACE DETECTION'],
    responses={}
)

@router.get("/ping")
async def ping():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello World"})

@router.post("/detect_image")
async def post_image(image: Image):
    return service_detect_face(image.image)