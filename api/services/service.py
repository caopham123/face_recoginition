from ai_core.src.face_detection import FaceDetection
from api.helpers.commons import stringToRGB, RGB2String
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
import logging, uuid
import json

## Create a Face Detection obj
face_detection = FaceDetection()
logger = logging.getLogger(__name__)


data = {}
# def service_detect_face(image: str):
#     try:
#         image = stringToRGB(image)
#         print(f"type of img: {type(image)}") # OK
#         ## Detect face
#         crop_img, vector_embedding = face_detection.detect_face(image) 
#         if crop_img is None and vector_embedding is None:
#             return JSONResponse(
#                 status_code=status.HTTP_400_BAD_REQUEST, 
#                 content={"msg": "No data"})
#         # print(f"shape of crop img: {crop_img.shape}") #OK 
        
#         ## Convert 
#         data = RGB2String(crop_img) # <class:bytes>
#         data_str = str(data)
#         return JSONResponse(
#             status_code=status.HTTP_200_OK,
#             content= {
#                 "total_item": len(data),
#                 "data": data_str
#             } )
    
#     except Exception as e:
#         logger.exception(e)
#         return JSONResponse(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             content={"msg": f"Error during processing {str(e)}"})

def service_embedding_face(img_base64: str):
    try:
        image = stringToRGB(img_base64)
        _, vector_embedding = face_detection.detect_face(image)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content= {
                "lenght": len(vector_embedding),
                "vector": str(vector_embedding)
            }
        )
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                             content={"msg": f"Error during embedding {str(e)}"})

def service_post_member(email: str, name: str ):
    try:
        member_id = str(uuid.uuid4())
        content = {
            "email": email, "name": name, "member_id": member_id
        }
        # content_email = content.get("email")
        # print(f"srv_post_mem: {content_email}")
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)
    
    except Exception as e:
        logger.exception(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"msg": f"Error during processing {str(e)}"})

def load_db():
    with open("db.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
def append_db():
    with open("db.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)