import cv2
import numpy as np
from .settings import MODEL_PATH
# from settings import MODEL_PATH
from insightface.app import FaceAnalysis

MODEL_LOAD = FaceAnalysis(name=MODEL_PATH, allowed_modules=None, providers=['CPUExecutionProvider'])
MODEL_LOAD.prepare(ctx_id=0, det_size=(640,640))

class FaceDetection:
    def __init__(self):
        self.model = MODEL_LOAD

    def detect_face(self, image: np.ndarray):
        faces_detect = self.model.get(image)
        face = faces_detect[0]

        if face:
            rec_image = self.model.draw_on(image, faces_detect)

            vector_embedding = face.normed_embedding
            print(f"leng {len(vector_embedding)}")

            bboxs = faces_detect[0].bbox.astype(np.int32)
            cropped_image = rec_image[bboxs[1]: bboxs[3], bboxs[0]: bboxs[2], :]
            print(f"embedding: {vector_embedding}")
            return cropped_image, vector_embedding
        return None

    
if __name__ == "__main__":
    face_detect = FaceDetection()
    import cv2
    image = cv2.imread("ai_core/src/pic/sontung01.jpg")

    crop_img, vector_embedding = face_detect.detect_face(image)
    print(f"Shape: {crop_img.shape}")
    print(f"Embedding (512D): {len(vector_embedding)}")

    cv2.imshow("Crop", crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
