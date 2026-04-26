rearrange_by_frequency=[4, 5, 6, 5, 4, 3, 4]
from collections import Counter
def frequency_sort(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    return sorted(nums, key=lambda x: (-freq[x], x))
print(frequency_sort(rearrange_by_frequency))