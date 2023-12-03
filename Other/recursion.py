def check_sorted(arr):
    if not arr or len(arr) < 2:
        return True
    return arr[0] <= arr[1] and check_sorted(arr[1:])

def get_1_to_N_inc(N, s, r):
    r.append(s)
    if s == N:
        return 
    s += 1
    get_1_to_N_inc(N, s, r)
    return r

def get_N_to_1_dec(N, r):
    r.append(N)
    if N == 1:
        return
    N -= 1
    get_N_to_1_dec(N, r)
    return r

if __name__ == '__main__':
    res = check_sorted([1, 2, 3, 4, 5, 6])
    print(res)
    r2 = check_sorted([1, 2, 9, 6])
    print(r2)
    print(get_1_to_N_inc(100, 1, []))
    print(get_N_to_1_dec(100, []))