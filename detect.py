from shlex import join
from PIL import Image
import pytesseract
import argparse
import cv2
import os

path = "/home/rin/Documents/Code/Craw/Linh.png"
# Đọc file ảnh và chuyển về ảnh xám
video = cv2.VideoCapture()
def detect_rin(path):
    image = cv2.imread(path,0)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("new2",image)
    # image = cv2.Canny(image,90,400)

    image1 = cv2.imread('/home/rin/Documents/Code/Craw/Linh.png')
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray1, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # cv2.imshow("new1",gray1)
    gray = cv2.medianBlur(gray1, 1)


    # filename = "{}.png".format(os.getpid())
    # cv2.imwrite(filename, gray1)
    text = pytesseract.image_to_string(Image.open(path),lang='eng')

    # Xóa ảnh tạm sau khi nhận dạng
    # os.remove(filename)

    # In dòng chữ nhận dạng được
    # print(type(text))
    return (text.split())
def scanCamera():
    camera = cv2.VideoCapture(0)
    while True:
        ret,frame = camera.read()
        # image = cv2.rectangle(frame,(250,150),(450,350),(0,255,0),3)
        cv2.imshow('tesst',frame)
        cv2.imwrite("/home/rin/Documents/Code/Craw/Linh.png",frame)
        str = " ".join(detect_rin(path))
        # if str=="":
        #     break
        print(str)
        cv2.waitKey(1)

# Hiển thị các ảnh chúng ta đã xử lý.
# Đợi chúng ta gõ phím bất kỳ
scanCamera()
del(video)
# cv2.waitKey()
cv2.destroyAllWindows()