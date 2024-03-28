import sys
read = sys.stdin.readline


def count_alphabet(my_string: str) -> dict:
    """
    문자열을 구성하는 문자들의 빈도를 세어 딕셔너리로 반환하는 함
    """
    my_dict = dict()
    for alphabet in my_string:
        if alphabet in my_dict:
            my_dict[alphabet] += 1
        else:
            my_dict[alphabet] = 1
    return my_dict


N = int(read())

for _ in range(N):
    # 비교할 두 문자열을 압력받아 각각 저장
    left_string, right_string = read().split()

    # 비교 결과에 따라 결과 출력
    if (count_alphabet(left_string) == count_alphabet(right_string)):
        additional_string = ""
    else:
        additional_string = "NOT "

    print(f"{left_string} & {right_string} are {additional_string}anagrams.")
