from ai_core.src.face_detection import FaceDetection
from api.helpers.commons import stringToRGB, RGB2String
from fastapi.responses import JSONResponse
from fastapi import FastAPI, status
import logging
## Create a Face Detection obj
face_detection = FaceDetection()
logger = logging.getLogger(__name__)

def service_detect_face(image: str):
    try:
        image = stringToRGB(image)
        print(f"type of img: {type(image)}") # OK
        ## Detect face
        crop_img = face_detection.detect_face(image) 
        if crop_img is None:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST, 
                content={"msg": "No data"})
        print(f"shape of crop img: {crop_img.shape}") #OK 
        
        data = RGB2String(crop_img)
        print(f"Type of data: {type(data)}") # OK
        data_str = str(data)
        print(f"type of str data: {type(data_str)}")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content= {
                "total_item": len(data),
                "data": data_str
            } )
    except ValueError as err:
        return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, 
        content={"msg": f"Invalid image {str(err)}"})
    
    except Exception as e:
        logger.exception(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"msg": f"Error during processing {str(e)}"})
    
def service_test_post(img: str):
    if len(img) != 0:
        response = {
            "http_code": status.HTTP_200_OK,
            "total_item": len(img),
            "data": img
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=response)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"msg": "Error, content no found"})