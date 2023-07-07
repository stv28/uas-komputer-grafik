import cv2

img = cv2.imread('images/waterfall.jpg')

print(img) # print (img.shape)

# x(500, 600) y(300, 400) color=black

for y in range(300, 400):
    for x in range(500, 600):
        img

cv2.imshow('image', img)

# cv2.waitkey(0)
# cv2.destroyAlwindow


