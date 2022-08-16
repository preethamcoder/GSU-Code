def binary_search(nums, tar):
  low = 0
  high = len(nums) - 1
  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == tar:
      return mid
    if nums[mid] < tar:
      low = mid + 1
    else:
      high = mid - 1
  return -1
