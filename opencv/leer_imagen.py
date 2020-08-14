import cv2
img = cv2.imread('logo.png')
dimension = img.shape
print(len(img.shape))
print(type(dimension))
print(dimension[0:2])
