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

def power(base, exp):
    if base == 0 or base == 1:
        return base
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp >= 0:
        return base * power(base, exp-1)
    else:
        return 1/base * power(base, exp+1)

def fast_power(base, exp):
    if base == 0 or base == 1:
        return base
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1/base
    tmp = fast_power(base, exp//2)
    return tmp * tmp * (base if exp % 2 == 1 else 1)

def get_tilings_possible(n):
    """Given a 4xn board, get the number of ways you can tile it with 4x1 tiles. They can be placed horizontally or vertically
    Args:
        n (int): Number of columns
    """
    # if n <= 3:
    #     return 1
    # return get_tilings_possible(n-1) + get_tilings_possible(n-4)
    res = [1, 1, 1, 1]
    for useless_var in range(4, n+1):
        res.append(res[-1]+res[-4])
    return res[-1]

if __name__ == '__main__':
    print(check_sorted([1, 2, 3, 4, 5, 6]))
    print(check_sorted([1, 2, 9, 6]))
    print(get_1_to_N_inc(100, 1, []))
    print(get_N_to_1_dec(100, []))
    print(power(2, 997))
    print(power(2, -997))
    print(fast_power(2, 997))
    print(fast_power(2, -997))
    print(get_tilings_possible(4))