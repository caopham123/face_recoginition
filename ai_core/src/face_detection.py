from insightface.app import FaceAnalysis
import insightface, cv2
import numpy as np
from .settings import MODEL_LOAD, MODEL_PATH


class FaceDetection:
    def __init__(self):
        self.model = MODEL_LOAD

    def detect_face(self, image: np.ndarray):
        faces_detect = self.model.get(image)

        rec_image = self.model.draw_on(image, faces_detect)

        bboxs = faces_detect[0].bbox
        bboxs = bboxs.astype(np.int32)
        cropped_image = rec_image[bboxs[1]: bboxs[3], bboxs[0]: bboxs[2], :]
        return cropped_image
    
if __name__ == "__main__":
    face_detect = FaceDetection()
    import cv2
    image = cv2.imread("ai_core/src/pic/sontung01.jpg")
    rs = face_detect.detect_face(image)
    cv2.imshow("Crop", rs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
