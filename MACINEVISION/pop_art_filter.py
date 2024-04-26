import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('Lenna.png')

# 이미지 컬러 양자화
quantized_image = image // 64 * 64

# 대조를 높여 윤곽을 높임
contrast_image = cv2.convertScaleAbs(quantized_image, alpha=1.5, beta=50)

# 이미지를 움직여 겹치는 효과 생성
rows, cols = contrast_image.shape[:2]
shifted_image = np.roll(contrast_image, shift=(rows//10, cols//10), axis=(0, 1))

# 색상 히스토그램 균일화 적용
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
pop_art_image = cv2.cvtColor(shifted_image, cv2.COLOR_BGR2LAB)
pop_art_image[:,:,0] = clahe.apply(pop_art_image[:,:,0])
pop_art_image = cv2.cvtColor(pop_art_image, cv2.COLOR_LAB2BGR)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Pop Art Filter', pop_art_image)
cv2.waitKey(0)
cv2.destroyAllWindows()