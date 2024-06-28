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
