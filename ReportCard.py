# 학생 클래스
class Student:
    def __init__(self, name, student_id):
        self.name = name          # 학생 이름
        self.student_id = student_id  # 학번
        self.scores = []          # 학생의 점수 리스트, 초기에는 비어 있음

    # 점수를 추가하는 메서드
    def add_score(self, score):
        self.scores.append(score)

    # 평균 점수를 계산하는 메서드
    def calculate_average(self):
        if not self.scores:  # 점수 리스트가 비어 있는 경우
            return 0
        return sum(self.scores) / len(self.scores)


# 성적부 클래스
class GradeBook:
    def __init__(self):
        self.students = []         # 학생 객체들을 저장하는 리스트
        self.student_ids = set()    # 중복 학번을 방지하기 위한 집합

    # 학생을 추가하는 메서드 (중복 학번 체크)
    def add_student(self, name, student_id):
        if student_id not in self.student_ids:  # 중복 학번이 아닌 경우에만 추가
            new_student = Student(name, student_id)
            self.students.append(new_student)
            self.student_ids.add(student_id)

    # 특정 학번의 학생에게 점수를 추가하는 메서드
    def add_student_score(self, student_id, score):
        for student in self.students:
            if student.student_id == student_id:
                student.add_score(score)
                return
        print(f"에러: 학번 {student_id} 학생을 찾을 수 없습니다.")

    # 상위 N명의 학생을 평균 점수 기준으로 정렬하여 이름과 평균 점수를 반환하는 메서드
    def get_top_students(self, n):
        # 학생들을 평균 점수 기준으로 내림차순 정렬
        sorted_students = sorted(self.students, key=lambda s: s.calculate_average(), reverse=True)
        # 상위 N명의 학생 이름과 평균 점수를 리스트로 반환
        return [(student.name, student.calculate_average()) for student in sorted_students[:n]]


# 성적부 테스트
grade_book = GradeBook()

# 학생 추가
grade_book.add_student("김철수", 101)
grade_book.add_student("이영희", 102)
grade_book.add_student("박민수", 103)

# 학생 점수 추가
grade_book.add_student_score(101, 88)
grade_book.add_student_score(101, 92)
grade_book.add_student_score(102, 75)
grade_book.add_student_score(102, 80)
grade_book.add_student_score(103, 95)
grade_book.add_student_score(103, 90)

# 상위 2명의 학생 출력
top_students = grade_book.get_top_students(2)
print("상위 2명 학생의 성적:", top_students)
