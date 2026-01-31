"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""


def two_sum(nums: list, target: int) -> list:
    """Функция возвращает индексы листа которые в сумме дают target"""
    total_len = len(nums)
    total_list = []

    for i in range(total_len):
        for j in range(i + 1, total_len):
            if nums[i] + nums[j] == target:
                total_list.append(i)
                total_list.append(j)
                return total_list

    return total_list


if __name__ == "__main__":
    print(two_sum([3, 2, 3], 6))