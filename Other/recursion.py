def check_sorted(arr):
    if not arr or len(arr) < 2:
        return True
    return arr[0] <= arr[1] and check_sorted(arr[1:])

if __name__ == '__main__':
    res = check_sorted([1, 2, 3, 4, 5, 6])
    print(res)
    r2 = check_sorted([1, 2, 9, 6])
    print(r2)