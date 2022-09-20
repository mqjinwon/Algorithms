# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# selection sort(선택 정렬)
# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]

# print(array)

# import time

# start = time.time()  # 시작 시간 저장
# # insertion sort(삽입 정렬)
# for i in range(1, len(array)):
#     for j in range(i):
#         if array[i] < array[j]:
#             data = array[i]
#             array.pop(i)
#             array.insert(j, data)
#             break
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

# quick sort(퀵 정렬)
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end

#     while left <= right:
#         while left <= right:
#             while left <= end and array[left] <= array[pivot]:
#                 left += 1
#             while right > start and array[right] >= array[pivot]:
#                 right -= 1

#             if left > right:
#                 array[right], array[pivot] = array[pivot], array[right]
#             else:
#                 array[left], array[right] = array[right], array[left]
#     quick_sort(array, start, right - 1)
#     quick_sort(array, right + 1, end)

# quick_sort(array, 0, len(array) - 1)
# print(array)

#Count sort(계수 정렬)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1

# for i in range(len(count)):
#     for j in range(count[i]):
#         print(i, end=" ")
