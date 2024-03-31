### 1주차 과제

----
### 소스코드 :
1. main.cpp :
```cpp
#include <iostream>
#include <map>
#include <string>

using namespace std;

map<char, int> countAlphabet(string my_string);

int main(void) {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		// 입력을 받을 string 객체들입니다
		string left_string, right_string;

		// 출현 빈도 비교 결과에 따라 다른 출력을 저장할 string 객체입니다
		string additional_string;

		// left_string과 right_string에 입력을 받습니다
		cin >> left_string;
		cin >> right_string;

		// 두 문자열을 비교하여 "NOT "을 붙일지 말지 결정합니다
		if (countAlphabet(left_string) != countAlphabet(right_string)) {
			additional_string = "NOT ";
		} 

		// 결과를 출력합니다
		cout << left_string
			<< " & "
			<< right_string
			<< " are "
			<< additional_string
			<< "anagrams."
			<< endl;
	}
	return 0;
}

/**
* @details 문자열의 알파벳 빈도를 구합니다
* @param[in] my_string 알파벳 빈도를 구할 string 객체입니다
* @return <알파벳: 출현횟수>를 <key : value>로 갖는 <char : int> 쌍의 map 객체를 반환합니다
*/
map<char, int> countAlphabet(string my_string) {
	// <char, int> 형의 <key, value> 쌍을 갖는 my_dict 라는 이름의 map 객체를 생성합니다
	map<char, int> my_dict;

	// my_string을 순회하며 출현 횟수를 my_dict에 저장합니다
	for (int i = 0; i < my_string.length(); i++) {
		if (my_dict.find(my_string[i]) != my_dict.end()) {
			my_dict[my_string[i]] += 1;
		} else {
			my_dict[my_string[i]] = 1;
		}
	}
	return my_dict;
}
```

2. main.py :
```python
import sys
read = sys.stdin.readline


def count_alphabet(my_string: str) -> dict:
    """
    문자열을 구성하는 문자들의 빈도를 세어 딕셔너리로 반환하는 함수
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
```
