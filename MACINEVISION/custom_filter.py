import cv2
import numpy as np

# 이미지 로드
image = cv2.imread("Lenna.png")

# 이미지 크기 추출
height, width = image.shape[:2]

# 웨이브 효과 파라미터 설정
amplitude = 10  # 웨이브의 진폭
frequency = 0.05  # 웨이브의 주기

# 세로로 웨이브 효과 적용
for y in range(height):
    wave = int(amplitude * np.sin(frequency * y))  # 해당 행의 웨이브 위치 계산
    image[y,:] = np.roll(image[y,:], wave, axis=0)  # 웨이브 효과 적용

# 결과 출력
cv2.imshow("Custom Wave Filter", image)
cv2.waitKey(0)
cv2.destroyAllWindows()