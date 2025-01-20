import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('Lenna.png')

# 세피아 톤 매트릭스
sepia_filter = np.array([[0.272, 0.534, 0.131],
                         [0.349, 0.686, 0.168],
                         [0.393, 0.769, 0.189]])

# 빈티지 필터 함수 정의
def vintage_filter(image):
    # 세피아 톤 적용
    sepia_image = cv2.transform(image, sepia_filter)

    # 블러 효과 추가
    blurred_image = cv2.GaussianBlur(sepia_image, (15, 15), 0)

    # 노이즈 추가
    noise = np.random.normal(0, 10, sepia_image.shape).astype('uint8')
    vintage_image = cv2.add(sepia_image, noise)

    return vintage_image

# 빈티지 필터 적용
vintage_result = vintage_filter(image)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Vintage Filter', vintage_result)
cv2.waitKey(0)
cv2.destroyAllWindows()