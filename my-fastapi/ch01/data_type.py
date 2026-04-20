from typing import *


def add(a: int, b: int) -> int:
    return a + b

def all_square(a: list) -> list:
    for i in a:
        s = i**2
        a.append(s)
    return a

def get_student_score() -> dict[str, int]:
    return {
        "A": 50,
        "B": 70,
    }

def get_student() -> tuple[str, int]:
    return ("A", 24)

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "A"
    elif user_id == 2:
        return "B"

def squre_or_length(num: Union[int, str]) -> int:
    if isinstance(num, int):
        return num**2
    else:
        return len(num)
if __name__ == '__main__':
    result = add(1, 2)
    result2 = add("1", "2")
    print(result)
    print(result2)

    score = get_student_score()
    print(score)

    print(find_user(2))
    print(find_user(3))

    print(squre_or_length(3))
    print(squre_or_length("10"))
    print(squre_or_length(10.1))