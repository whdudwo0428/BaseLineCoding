# 영화 클래스
class Movie:
    def __init__(self, title, schedule):
        self.title = title  # 영화 제목
        self.schedule = schedule  # 상영 시간표
        # 각 상영 시간마다 10개의 좌석을 모두 빈 상태로 초기화
        self.seats = {time: [False] * 10 for time in schedule}

    # 특정 시간대에 좌석을 예약하는 메서드
    def reserve_seat(self, time, seat_number):
        if time not in self.seats:
            print(f"에러: '{self.title}' 영화에는 '{time}' 상영 시간이 없습니다.")
            return

        # 좌석이 예약 가능한지 확인
        if self.seats[time][seat_number] is False:
            self.seats[time][seat_number] = True  # 좌석 예약 완료
            print(f"'{self.title}' 영화의 '{time}'에 좌석 {seat_number}번이 예약되었습니다.")
        else:
            print(f"경고: '{self.title}' 영화의 '{time}'에 좌석 {seat_number}번은 이미 예약되었습니다.")

    # 특정 시간대의 예약 가능한 좌석 수를 반환하는 메서드
    def get_available_seats(self, time):
        if time not in self.seats:
            print(f"에러: '{self.title}' 영화에는 '{time}' 상영 시간이 없습니다.")
            return 0
        return self.seats[time].count(False)  # 예약되지 않은 좌석 수


# 영화관 클래스
class Theater:
    def __init__(self):
        self.movies = {}  # 영화 제목을 키로 하고 Movie 객체를 값으로 가지는 딕셔너리

    # 영화 추가 메서드
    def add_movie(self, title, schedule):
        if title not in self.movies:
            self.movies[title] = Movie(title, schedule)
            print(f"'{title}' 영화가 추가되었습니다.")
        else:
            print(f"경고: '{title}' 영화는 이미 추가되어 있습니다.")

    # 특정 영화의 특정 시간대에 좌석을 예약하는 메서드
    def reserve_movie_seat(self, title, time, seat_number):
        if title in self.movies:
            if 0 <= seat_number < 10:  # 유효한 좌석 번호 확인
                self.movies[title].reserve_seat(time, seat_number)
            else:
                print("에러: 유효하지 않은 좌석 번호입니다.")
        else:
            print(f"에러: '{title}' 영화가 없습니다.")

    # 특정 영화의 상영 시간표와 예약 가능한 좌석 수를 출력하는 메서드
    def get_movie_schedule(self, title):
        if title in self.movies:
            print(f"\n'{title}' 영화의 상영 시간표:")
            for time in self.movies[title].schedule:
                available_seats = self.movies[title].get_available_seats(time)
                print(f" - {time}: 예약 가능 좌석 수 = {available_seats}")
        else:
            print(f"에러: '{title}' 영화가 없습니다.")


# 영화관 시스템 테스트
theater = Theater()

# 영화 추가
theater.add_movie("인셉션", ["14:00", "17:00", "20:00"])
theater.add_movie("인터스텔라", ["13:00", "16:00", "19:00"])

# 좌석 예약
theater.reserve_movie_seat("인셉션", "14:00", 3)
theater.reserve_movie_seat("인셉션", "14:00", 3)  # 이미 예약된 좌석
theater.reserve_movie_seat("인터스텔라", "19:00", 5)

# 영화의 상영 시간표와 예약 가능한 좌석 수 확인
theater.get_movie_schedule("인셉션")
theater.get_movie_schedule("인터스텔라")
