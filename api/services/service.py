from ai_core.src.face_detection import FaceDetection
from api.helpers.commons import stringToRGB, strToList
from fastapi.responses import JSONResponse
from fastapi import status
import logging, uuid
from typing import Optional
import json

## Create a Face Detection obj
face_detection = FaceDetection()
logger = logging.getLogger(__name__)


DB_FILE = "db.json"
data = {}
with open(DB_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

def service_embedding_face(img_base64: str):
    try:
        image = stringToRGB(img_base64)
        _, vector_embedding = face_detection.detect_face(image)
        return vector_embedding 

    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                             content={"msg": f"Error during embedding {str(e)}"})

def service_post_member(email: Optional[str], name: Optional[str] ):
    try:
        member_id = str(uuid.uuid4())
        content = {
            "email": email, "name": name, 
            "embedding": None, "member_id": member_id 
        }

        append_db(content)
        return JSONResponse(status_code=status.HTTP_200_OK, content=content)
    
    except Exception as e:
        logger.exception(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"msg": f"Error during processing {str(e)}"})

def service_add_face(target_member_id: str, img_str: str):
    try:
        ## Find member by id
        if len(data["members"]) <= 0:
            print("No data")
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"msg": "No data"})
        _member_id = ""
        
        embedding = service_embedding_face(img_str) # [.5353 .0025 .9463]
        # embedding = str(embedding)            # "[.5353, .0025, .9463]"

        for member in data["members"]:
            if member["member_id"] == target_member_id:
                _member_id = target_member_id
                member['embedding'] = embedding
                member['image'] = img_str
                break
        
        content={
                "email": member["email"],
                "name": member["name"],
                "embedding": embedding,
                "image": img_str,
                "member_id": _member_id
            }
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content= content
        )
        
    except ValueError as e:
        logger.exception(e)
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"msg": f"Error: {str(e)}"}
        )

    
def append_db(content: json):
    data["members"].append(content)
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
