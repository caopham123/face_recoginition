from api.schema import Image, Member, UpdateMember
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .services.service import service_post_member, service_embedding_face, service_add_face

router = APIRouter(
    prefix="/api/v1",
    tags=['FACE DETECTION'],
    responses={}
)

@router.get("/ping")
async def ping():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello World123"})

@router.post("/detect_image")
async def post_image(image: Image):
    try:
        # return service_detect_face(image.image)
        return service_embedding_face(image.image)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"msg": f"Unexpected error: {str(e)}"}
        )

@router.post("/add_member")
async def post_member(member: Member):
    return service_post_member(member.email, member.name)

@router.put("/update_member")
async def update_member(member: UpdateMember, img_str: str):
    return service_add_face(member.member_id, img_str)