# def two_num_sum(nums, target):
#     """ 两数之和 """
#
#     # 方式1
#     for i in range(len(nums)):
#         result = target - nums[i]
#         if result not in nums or i == nums.index(result):
#             continue
#         else:
#             return [i, nums.index(result)]
#
#     # 方式2
#     # for i in range(len(nums) - 1):
#     #     for j in range(i + 1, len(nums)):
#     #         if target - nums[i] == nums[j]:
#     #             return [i, j]
#
#
# num = [3, 2, 4]
# target_num = 6
# print(two_num_sum(num, target_num))


# def longest_consecutive(nums) -> int:
#     """
#     此函数用于求给定列表中的最长连续子串
#     例如:
#     输入：[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6] 返回: 7  因为最大的连续字串为 [3,4,5,6,7,8,9]
#     输入：[100, 4, 200, 1, 3, 2] 返回: 4  因为最大的连续字串为 [1,2,3,4]
#
#     """
#
#     # 方式一：先排除数据不合规的情况，再通过将数据排序，然后按照下标获取
#     # 能实现此功能，但是事件复杂度大
#
#     # if not nums:
#     #     return 0
#     #
#     # nums = list(set(nums))
#     # for i in range(len(nums) - 1):
#     #     for j in range(i + 1, len(nums)):
#     #         if nums[i] > nums[j]:
#     #             nums[i], nums[j] = nums[j], nums[i]
#     #
#     # print("列表: \n", nums)
#     # count = max_length = 1
#     # for index in range(0, len(nums)):
#     #     if nums[index] + 1 in nums:
#     #         count += 1
#     #         index = nums.index(nums[index] + 1)
#     #     else:
#     #         count = 1
#     #     if count > max_length:
#     #         max_length = count
#     #
#     # return max_length
#
#     # 方式2：解题思路：从当前值的最小边界开始查找，即：n - 1 不在列表中存在时，每次如果n+1在列表中存在，则计数加1，然后n=n+1，再继续查找n+1直到不在列表中存在
#     # tips: set的查找效率要比list高，所以下面将list转换为set
#     if not nums:
#         return 0
#
#     num_set = set(nums)
#     count = max_length = 1
#     for num in num_set:
#         if num - 1 not in num_set:
#             while num + 1 in num_set:
#                 count += 1
#                 num += 1
#
#             max_length = max(max_length, count)
#             count = 1
#
#     return max_length
#
#
# # nums_list = [100, 4, 200, 1, 3, 2]
# # nums_list = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
# # nums_list = [1, 2, 0, 1]
# nums_list = [1, 0, -1]
#
#
# print(longest_consecutive(nums_list))


# def move_zero(nums):
#     """
#     此函数用于编写移动0的算法
#     给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#     请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
#     示例 1:
#     输入: nums = [0,1,0,3,12]
#     输出: [1,3,12,0,0]
#
#     示例 2:
#     输入: nums = [0]
#     输出: [0]
#     """
#
#     # 方式1: 时间复杂度较高，O(N^2)
#     # 思路: 遍历列表的每一个元素，如果当前的数为0，则从当前数往后开始判断，与找到的第一个非零数交换位置，
#     # for index in range(len(nums) - 1):
#     #     if nums[index] == 0:
#     #         for j in range(index+1, len(nums)):
#     #             if nums[j] != 0:
#     #                 nums[index], nums[j] = nums[j], nums[index]
#     #                 break
#     #
#     # return nums
#
#     # 方式2: 时间复杂度低 O(N)
#     # 思路: 先遍历整个列表，将所有非零的数按照相对的顺序放到列表中，并记录下最后一个非零数的位置，
#     # 再使用循环从最后一个非零数的位置到列表的最后一个位置，将这些位置的值全部填充为0即可
#     nonzero_index = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[nonzero_index] = nums[i]
#             nonzero_index += 1
#
#     for j in range(nonzero_index, len(nums)):
#         nums[j] = 0
#
#     return nums
#
#
# nums = [0, 1, 0, 3, 12]
# # nums = [0, 0, 1]
# # nums = [0, 0, 0, 0, 0, 0, 1, 1, 1]
# print(move_zero(nums))


# def climb_stairs(n):
#     """
#     爬楼梯
#     每次可以爬1阶或者2阶，求爬n阶有多少种方法
#     f(n) = f(n-1) + f(n-2)
#     """
#     if n <= 2:
#         return n
#
#     before_one, before_two = 1, 2
#     current_num = 0
#     for i in range(2, n):
#         current_num = before_one + before_two
#         before_one = before_two
#         before_two = current_num
#     return current_num
#
#
# result = climb_stairs(45)
# print(result)

import time


# def pascal_triangle(num_rows):
#     """
#     杨辉三角
#     给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#     1 <= num_rows <= 30
#     """
#
#     # 方式一：暴力法，生成每一行的元素，时间复杂度O(n^2)
#     # final_list = []
#     #
#     # for i in range(num_rows):  # 循环所有行
#     #     final_list.append([1 for _ in range(0, i + 1)])
#     #     if i - 1 < 0:  # 如果是第一行，不需要计算
#     #         continue
#     #
#     #     for j in range(1, i):
#     #         final_list[i][j] = final_list[i-1][j-1] + final_list[i-1][j]
#     #
#     # return final_list
#
#     # 方式二：优化，只生成需要的元素，时间复杂度O(n^2)
#     final_list = [[1]]
#     if num_rows == 1:
#         return final_list
#
#     for i in range(1, num_rows):
#         row = [1]
#         for j in range(1, i):
#             row.append(final_list[i - 1][j - 1] + final_list[i - 1][j])
#         row.append(1)
#         final_list.append(row)
#
#     return final_list
#
#
# rows = 30
# result = pascal_triangle(rows)
# print(f"前{rows}行的杨辉三角:\n", result)


def water_container(heights):
    """
    力扣第 11 题: 盛水最多的容器
    给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    返回容器可以储存的最大水量。
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
    解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
    """

    # 方式一: 遍历每一个位置，计算以该位置为右下角的矩阵的最大容量，时间复杂度O(n^3)，数据量小的情况下可行，数据量过大时，时间复杂度过高，会超时
    # index_count = max_water_volume = 0
    #
    # for i in range(len(heights) - 1):
    #     for j in range(i + 1, len(heights)):
    #         index_count += 1
    #         if heights[i] > heights[j]:
    #             min_height = heights[j]
    #         else:
    #             min_height = heights[i]
    #         temporary_water_volume = min_height * index_count
    #         max_water_volume = max(max_water_volume, temporary_water_volume)
    #     index_count = 0

    # 方式二: 双指针
    max_water_volume, left_pointer, right_pointer = 0, 0, len(heights) - 1

    while left_pointer <= right_pointer:
        temporary_water_volume = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
        max_water_volume = max(max_water_volume, temporary_water_volume)
        if heights[left_pointer] < heights[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return max_water_volume


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
start_time = time.time()
result = water_container(height)
print("程序执行时间: ", time.time() - start_time)
print("容器最大可以存储的水量: ", result)


def flaccid_series(n):
    """
    斐波拉契数列
    求前n项斐波拉契数列
    """

    # 方式一: 迭代法，时间复杂度O(n)
    if n == 0:
        return []

    fib_list = []
    for i in range(n):
        if i == 0 or i == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list


n = 5
result = flaccid_series(n)
print(f"斐波拉契数列前{n}项: ", result)


def three_num_sum(nums):
    """
    力扣第 15 题：三数之和
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
    你返回所有和为 0 且不重复的三元组。
    注意：答案中不可以包含重复的三元组
    示例 1：

    输入：nums = [-1,0,1,2,-1,-4]
    输出：[[-1,-1,2],[-1,0,1]]
    解释：
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
    不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
    注意，输出的顺序和三元组的顺序并不重要。
    """

    # 方式1：时间复杂度过高，在力扣上提交不能通过
    # nums = sorted(nums)
    # print(nums)
    # if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
    #     return []
    #
    # result_list = []
    #
    # for i in range(len(nums)-1):
    #     left_pointer, right_pointer = i + 1, len(nums) - 1
    #     while left_pointer < right_pointer:
    #         current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
    #         print("当前: ", i, left_pointer, right_pointer, [nums[i], nums[left_pointer], nums[right_pointer]])
    #         if current_sum < 0:
    #             # while left_pointer < right_pointer:
    #             if i == left_pointer or i == right_pointer or left_pointer == right_pointer:
    #                 continue
    #             current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
    #             # print("小于: ", i, left_pointer, right_pointer, [nums[i], nums[left_pointer], nums[right_pointer]])
    #             if current_sum == 0:
    #                 current_list = sorted([nums[i], nums[left_pointer], nums[right_pointer]])
    #                 if current_list not in result_list:
    #                     result_list.append(current_list)
    #             left_pointer += 1
    #         elif current_sum > 0:
    #             # while left_pointer < right_pointer:
    #             if i == left_pointer or i == right_pointer or left_pointer == right_pointer:
    #                 continue
    #             current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
    #             # print("大于: ", i, left_pointer, right_pointer, [nums[i], nums[left_pointer], nums[right_pointer]])
    #             if current_sum == 0:
    #                 current_list = sorted([nums[i], nums[left_pointer], nums[right_pointer]])
    #                 if current_list not in result_list:
    #                     result_list.append(current_list)
    #             right_pointer -= 1
    #         else:
    #             # print("等于: ", i, left_pointer, right_pointer, [nums[i], nums[left_pointer], nums[right_pointer]])
    #             current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
    #             if current_sum == 0:
    #                 current_list = sorted([nums[i], nums[left_pointer], nums[right_pointer]])
    #                 if current_list not in result_list:
    #                     result_list.append(current_list)
    #                 left_pointer += 1
    #                 right_pointer -= 1
    #
    # return result_list

    # 方式2：优化时间复杂度
    nums.sort()  # 排序，为了后续去重和计算
    result_list = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:  # 去重，因为已经排序过，所以如果当前值和下一个值相等，则说明重复了，跳过
            continue

        left_pointer, right_pointer = i + 1, len(nums) - 1  # 做指针为当前位置后面的位置，右指针为最后一个位置
        while left_pointer < right_pointer:
            current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
            if left_pointer > i + 1 and nums[left_pointer] == nums[left_pointer - 1]:  # 去重
                left_pointer += 1
            elif right_pointer < len(nums) - 1 and nums[right_pointer] == nums[right_pointer + 1]:  # 去重
                right_pointer -= 1
            elif current_sum < 0:  # 左指针右移
                left_pointer += 1
            elif current_sum > 0:  # 右指针左移
                right_pointer -= 1
            else:  # 找到了，添加到结果列表，左右指针同时移动
                result_list.append([nums[i], nums[left_pointer], nums[right_pointer]])
                left_pointer += 1
                right_pointer -= 1

    return result_list


# nums_list = [-1, 0, 1, 2, -1, -4]
# nums_list = [-2, 0, 1, 1, 2]
# nums_list = [-1,0,1,2,-1,-4]
# nums_list = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
# nums_list = [-2,0,1,1,2]
# nums_list = [-4,-1,-4,0,2,-2,-4,-3,2,-3,2,3,3,-4]
nums_list = [-2, 0, 1, 1, 2]
result = three_num_sum(nums_list)
print(f"三元组: ", result)
