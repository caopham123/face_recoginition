import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis

image = cv2.imread('pic/sontung01.jpg')

def show_image(image_file):
    cv2.imshow("origin", image_file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def crop_image(rec_image, ymin, ymax, xmin, xmax,):
    crop_image = rec_image[ ymin:ymax, xmin: xmax, :]
    return crop_image

model_path = "buffalo_l"
app = FaceAnalysis(name=model_path, providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

if app is None:
    print("Not found model")



faces_detected = app.get(image)
bbox = faces_detected[0]['bbox'].astype(np.int32) # [269 125 592 520]
print(f"bbox {bbox}")
# print(f"len of faces {len(faces_detected)}")

rec_image = app.draw_on(image, faces_detected)
cropped_image = crop_image(rec_image, bbox[1], bbox[3], bbox[0], bbox[2])
show_image(cropped_image)





