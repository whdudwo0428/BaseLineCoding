# 학생 클래스
class Student:
    def __init__(self, name, student_id):
        self.name = name  # 학생 이름
        self.student_id = student_id  # 학번
        self.attendance = False  # 초기 출석 여부는 False

    # 출석 여부를 True로 설정하는 메서드
    def mark_attendance(self):
        self.attendance = True


# 출석부 클래스
class AttendanceBook:
    def __init__(self):
        self.students = []  # 학생 객체들을 저장하는 리스트
        self.student_ids = set()  # 중복 학번을 방지하기 위한 집합

    # 학생을 추가하는 메서드 (중복 학번 체크)
    def add_student(self, name, student_id):
        if student_id not in self.student_ids:  # 중복 학번이 아닌 경우에만 추가
            new_student = Student(name, student_id)
            self.students.append(new_student)
            self.student_ids.add(student_id)

    # 특정 학번의 학생 출석 체크
    def mark_student_attendance(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.mark_attendance()
                break

    # 출석과 결석 인원 요약을 딕셔너리로 반환하는 메서드
    def get_attendance_summary(self):
        attendance_count = sum(student.attendance for student in self.students)  # 출석 인원 수
        absence_count = len(self.students) - attendance_count  # 결석 인원 수
        return {"출석": attendance_count, "결석": absence_count}

    # 출석한 학생들의 이름을 리스트로 반환하는 메서드
    def get_student_list(self):
        return [student.name for student in self.students if student.attendance]


# 출석부 테스트
attendance_book = AttendanceBook()

# 학생 추가
attendance_book.add_student("김철수", 101)
attendance_book.add_student("이영희", 102)
attendance_book.add_student("박민수", 103)
attendance_book.add_student("김철수", 101)  # 중복 학번

# 출석 체크
attendance_book.mark_student_attendance(101)
attendance_book.mark_student_attendance(103)

# 출석 요약 및 출석한 학생 목록 출력
print("출석 요약:", attendance_book.get_attendance_summary())
print("출석한 학생 목록:", attendance_book.get_student_list())
