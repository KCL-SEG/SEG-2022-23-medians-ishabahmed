"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


def findMedian(nums):
    nums.sort()

    if len(nums) % 2:
        return nums[len(nums) // 2]
    else:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(findMedian(numbers))
