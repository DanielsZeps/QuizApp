from typing import List

def frequency_sorting(numbers: List[int]):
    z = numbers.copy()
    def funct1(item):
        return -z.count(item), item
    numbers.sort(key=funct1)
    return numbers
