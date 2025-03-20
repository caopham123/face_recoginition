from api.schema import Image, Test, Member
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .services.service import service_detect_face, service_test_post, service_post_member

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
    try:
        return service_detect_face(image.image)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"msg": f"Unexpected error: {str(e)}"}
        )

@router.post("/test")
async def test_post(img: Test):
    return service_test_post(img.img)

@router.post("/add_member")
async def post_member(member: Member):
    return service_post_member(member.email, member.name)