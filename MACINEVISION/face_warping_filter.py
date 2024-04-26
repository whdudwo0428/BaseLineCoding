import dlib
import cv2
import numpy as np

def load_landmarks(image, predictor, detector):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) > 0:
        landmarks = predictor(gray, faces[0])
        return np.array([[p.x, p.y] for p in landmarks.parts()], dtype=np.int32)
    return None

# 이미지 로드
image = cv2.imread("Lenna.png")

# dlib 얼굴 디텍터와 특징점 예측 모델 로드
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 얼굴 특징점 추출
landmarks = load_landmarks(image, predictor, detector)

# 특징점 그리기
if landmarks is not None:
    for landmark in landmarks:
        cv2.circle(image, (landmark[0], landmark[1]), 1, (0, 255, 0), -1)

# 결과 출력
cv2.imshow("Facial Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()