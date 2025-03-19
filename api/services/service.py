from ai_core.src.face_detection import FaceDetection
from api.helpers.commons import stringToRGB, RGB2String
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status

## Create a Face Detection obj
face_detection = FaceDetection()

def service_detect_face(image: str):
    image = stringToRGB(image)
    data = face_detection.detect_face(image)
    data = RGB2String(data)

    if len(data) != 0:
        response = {
            "http_code": status.HTTP_200_OK,
            "total_item": len(data),
            "data": data
        } 
        return JSONResponse(status_code=status.HTTP_200_OK, content=response)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="No data")