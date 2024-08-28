import cv2

def thresher():
    img = cv2.imread("images.jpeg")
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    threshInv = cv2.GaussianBlur(gray_image, (9, 9), 0)
    (t,threshInv) = cv2.threshold(gray_image, 100, 255,cv2.THRESH_BINARY_INV)
    threshInv = cv2.bitwise_not(threshInv)
    cv2.imshow("thrsh",threshInv)
    cv2.imwrite("beauty.jpg", threshInv)

thresher()
matrix = cv2.imread("beauty.jpg")
otherm = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j][0] == 0:
            otherm.append((i,j))

f = open("coords.txt", "w")
for i in otherm:
    f.write("["+str(i[0])+","+str(i[1])+"], ")
f.close()
