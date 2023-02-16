import cv2

image = cv2.imread("resources/01.jpeg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image

pencil_sketch = cv2.divide(gray_image, inverted_image, scale=256.0)
cv2.imwrite("resources/sketch.png", pencil_sketch)