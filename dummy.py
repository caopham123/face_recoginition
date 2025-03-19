import cv2

bbox = [269, 125, 592, 520] # xmin, ymin, xmax, ymax
img = cv2.imread("pic/sontung01.jpg")
img = cv2.resize(img, (640,640))
def show_image(image_file):
    cv2.imshow("origin", image_file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

rec_img = cv2.rectangle(img, (125, 520), (269, 592), (255,100,254), 2)
show_image(rec_img)