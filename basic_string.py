def Alphabet():
    word = str(input().upper())  # 입력받은 문자열을 대문자로 변환
    candidate = list(set(word))  # 중복된 문자를 제거하고 리스트로 변환
    count = [0] * len(candidate)  # 각 문자별로 카운트 리스트를 0으로 초기화

    # 각 문자의 빈도 계산
    for char in word:
        index = candidate.index(char)  # char의 candidate에서의 인덱스를 찾음
        count[index] += 1  # 해당 문자의 카운트를 증가시킴

    # 최대 빈도를 찾음
    max_count = max(count)  # count 리스트에서 가장 큰 값(최대 빈도)을 찾음
    max_candidates = [candidate[i] for i in range(len(count)) if count[i] == max_count]  # 최대값을 가진 문자들 리스트

    # 출력
    if len(max_candidates) > 1:  # 최대 빈도의 문자가 여러 개일 경우
        print("?")
    else:
        print(max_candidates[0])  # 최대 빈도의 문자가 하나일 경우 그 문자 출력


Alphabet()
