def solution(numbers):
    numbers = [str(n) for n in numbers]
    return str(int("".join(sorted(numbers, key=lambda x: x*3, reverse=True))))