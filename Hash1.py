def solution(participant, completion):
    # 해시값의 총 합을 저장할 변수
    tmp = 0

    # 해시값과 이름이 저장되는 키값 구조
    dic = {}

    # 참여자 전체 해시값 더라기 및 이름(해시값) 저장하기
    for p in participant:

        # 전체 참여자 이름과 해시값 저장하기
        dic[hash(p)] = p

        # 전체 해시값 저장하기
        tmp += int(hash(p))

    # 완주자 전체 해시값을 빼기
    for com in completion:

        # 최종 남은 값이 마지막 1명 남은 미완주자임
        tmp -= hash(com)

    # 해시값으로 미완주자 이름 가져오기
    return dic[tmp]