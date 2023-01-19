import cv2

# Load image
img = cv2.imread("tenda.jpg", 0)

# Apply binary thresholding
ret, binary_threshold = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Apply truncate thresholding
ret, truncate_threshold = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

# Apply to zero thresholding
ret, tozero_threshold = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

# Apply to zero inverse thresholding
ret, tozeroinv_threshold = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# Show images
cv2.imshow("Binary Threshold", binary_threshold)
cv2.imshow("Truncate Threshold", truncate_threshold)
cv2.imshow("To Zero Threshold", tozero_threshold)
cv2.imshow("To Zero Inverse Threshold", tozeroinv_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
