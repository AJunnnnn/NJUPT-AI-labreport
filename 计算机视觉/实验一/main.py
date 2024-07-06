import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('123.jpg')
cv2.namedWindow('test', cv2.WINDOW_KEEPRATIO)
cv2.imshow('test', img)
cv2.waitKey(0)
cv2.imwrite("test1.jpg", img=img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Gray Img", imgGray)
cv2.imshow("Blur Img", imgBlur)
cv2.imshow("Canny Img", imgCanny)
cv2.imshow("Dilation Img", imgDilation)
cv2.imshow("Erode Img", imgErode)

cv2.waitKey(0)

print(img.shape)
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)
imgCropped = img[46:119, 352:495]
cv2.imshow('Resize Img', imgResize)
cv2.imshow('Cropped Img', imgCropped)
cv2.waitKey(0)

width, heigth = 250, 300
pts1 = np.float32([[111,219],[287,188],[151,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,heigth],[width,heigth]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, heigth))

cv2.imshow('Img', img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)

# import cv2
# import numpy as np
#
#
# class opcv_show(object):
#     def __init__(self,
#                  frame_width: int = 640,
#                  frame_height: int = 480,
#                  img_path=None,
#                  video_path=None):
#         self.img_path = img_path
#         self.video_path = video_path
#         self.frame_width = frame_width
#         self.frame_height = frame_height
#         self.original_img = None
#
#     def img_show(self):
#         img = cv2.imread(self.img_path)
#         self.original_img = img
#         cv2.imshow('lena original image', img)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#     def video_show(self):
#         cap = cv2.VideoCapture(self.video_path)
#         while True:
#             ret, frame = cap.read()
#             img = cv2.resize(frame, (self.frame_width, self.frame_height))
#             cv2.imshow('video', img)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         cv2.destroyAllWindows()
#
#
# class img_process(object):
#     def __init__(self,
#                  original_img: np.ndarray):
#         self.original_img = original_img
#         self.kernel = np.ones((5, 5), np.uint8)
#
#     def img_convert(self):
#         img_gray = cv2.cvtColor(self.original_img, cv2.COLOR_BGR2GRAY)
#         img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
#         img_canny = cv2.Canny(img_gray, 150, 200)
#         img_dilation = cv2.dilate(img_gray, self.kernel, iterations=1)
#         img_erosion = cv2.erode(img_gray, self.kernel, iterations=1)
#         cv2.imshow('img gray', img_gray)
#         cv2.imshow('img blur', img_blur)
#         cv2.imshow('img canny', img_canny)
#         cv2.imshow('img dilation', img_dilation)
#         cv2.imshow('img erosion', img_erosion)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#     def img_resize(self,
#                    width: int,
#                    height: int):
#         img_resized = cv2.resize(self.original_img, (height, width))
#         print(img_resized.shape)
#         cv2.imshow('img resized', img_resized)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#     def img_crop(self,
#                  width: list,
#                  height: list):
#         img_cropped = self.original_img[height[0]:height[1], width[0]:width[1]]
#         print(img_cropped.shape)
#         cv2.imshow('img cropped', img_cropped)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#
# class twist(object):
#     def __init__(self,
#                  original_img: np.ndarray,
#                  width: int,
#                  height: int):
#         self.original_img = original_img
#         self.width = width
#         self.height = height
#
#     def exe_twist(self):
#         pts1 = np.float32([[111, 219],
#                            [287, 188],
#                            [154, 482],
#                            [352, 440]])
#         pts2 = np.float32([[0, 0],
#                            [self.width, 0],
#                            [0, self.height],
#                            [self.width, self.height]])
#         matrix = cv2.getPerspectiveTransform(pts1, pts2)
#         img_twist = cv2.warpPerspective(self.original_img, matrix, (self.width, self.height))
#         cv2.imshow('img twist', img_twist)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#
#
# def main():
#     img_path = "test.jpg"
#
#     op_show = opcv_show(640, 480, img_path, 0)
#     op_show.video_show()
#     op_show.img_show()
#     original_img = op_show.original_img
#
#     process = img_process(original_img)
#     process.img_convert()
#     process.img_resize(1000, 500)
#     process.img_crop([46, 119], [352, 495])
#
#     my_twist = twist(original_img, 250, 350)
#     my_twist.exe_twist()
#
#
# if __name__ == '__main__':
#     main()