import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('Lenna.png')

# 가우시안 블러 적용
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 밝기와 채도 증가
dreamy_image = cv2.convertScaleAbs(blurred_image, alpha=1.2, beta=30)

# 라이트 누출 효과 추가
light_leak = np.zeros_like(image)
cv2.circle(light_leak, (image.shape[1]//2, image.shape[0]//2), 300, (30, 30, 255), -1)
light_leak = cv2.GaussianBlur(light_leak, (101, 101), 0)
dreamy_image = cv2.addWeighted(dreamy_image, 1, light_leak, 0.6, 0)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Dreamy Filter', dreamy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
