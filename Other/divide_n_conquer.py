# def num_factor(n):
#     if n <= 2:
#         return 1
#     if n == 3:
#         return 2
#     if n == 4:
#         return 4
#     return num_factor(n-1) + num_factor(n-3) + num_factor(n-4)

# print(num_factor(4))

# def house_robber_dp(houses):
#     length = len(houses)
#     # If one house, rob it
#     if length == 1:
#         return houses[0]
#     # If 2 hosues, then rob the one with more money
#     if length == 2:
#         return max(houses[0], houses[1])
#     money = [houses[0], max(houses[0], houses[1])]
#     # If more than 2 houses, then you intialize money to the money in first house and the second house if it is more, else just first house
#     for each in range(2, length):
#         # If the current house has more money than the previous house, then you rob it
#         money.append(max(houses[each]+money[each-2], money[each-1]))
#     return money[-1]

# print(house_robber_dp([6, 7, 1, 30, 8, 2, 4]))

# def house_robber(houses):
#     if houses == []:
#         return 0
#     opt1 = houses[0] + house_robber(houses[2:])
#     opt2 = 0 + house_robber(houses[1:])
#     return max(opt1, opt2)

# print(house_robber([6, 7, 1, 30, 90, 2]))

# def countZeroes(customList):
#     # TODO
#     length = len(customList)
#     def helper(arr, l):
#         left = 0
#         right = l-1
#         mid = (left+right)//2
#         while left <= right:
#             if arr[mid] == 0:
#                 right = mid-1
#             elif arr[mid] == 1:
#                 left = mid+1
#             mid = (left+right)//2
#         return left
#     return length-helper(customList, length)

# print(countZeroes([1, 1, 1, 0, 0, 0]))

# def sortedFrequency(arr, num):
#     length = len(arr)
#     def helper(array, number, l):
#         left = 0
#         right = l-1
#         mid = (left+right)//2
#         while left <= right:
#             if array[mid] == number:
#                 lc = mid
#                 rc = mid
#                 while array[lc] == number and lc >= 0:
#                     lc -= 1
#                 while rc < l and array[rc] == number:
#                     rc += 1
#                 return rc-lc-1
#             elif array[mid] < number:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#             mid = (left+right)//2
#         return -1
#     return helper(arr, num, length)

# print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 2))
# print(sortedFrequency([1, 1, 2, 2, 2, 2, 3, 3], 3))
# print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 4))
# print(sortedFrequency([1, 1, 2, 2, 2, 2, 3], 1))
# print(sortedFrequency([], 4))

# def edit_distance(s1, s2):
#     l1 = len(s1)
#     l2 = len(s2)
#     if not s1:
#         return l2
#     if not s2:
#         return l1
#     res = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
#     res[0] = list(range(l2+1))
#     for each in range(l1+1):
#         res[each][0] = each
#     for each in range(1, l1+1):
#         for otha in range(1, l2+1):
#             if s1[each-1] == s2[otha-1]:
#                 res[each][otha] = res[each-1][otha-1]
#             else:
#                 res[each][otha] = 1 + min(res[each-1][otha-1], res[each-1][otha], res[each][otha-1])
#     return res[l1][l2]
# print(edit_distance("punk", "pink"))

# def ed_r(s1, s2, ind1, ind2):
#     if ind1 == len(s1):
#         return len(s2)-ind2
#     if ind2 == len(s2):
#         return len(s1)-ind1
#     if s1[ind1] == s2[ind2]:
#         return ed_r(s1, s2, ind1+1, ind2+1)
#     else:
#         delete = 1 + ed_r(s1, s2, ind1, ind2+1)
#         insert = 1 + ed_r(s1, s2, ind1+1, ind2)
#         replace = 1 + ed_r(s1, s2, ind1+1, ind2+1)
#         return min(delete, insert, replace)
# print(ed_r("gambol", "gumbo", 0, 0))
# print(ed_r("table", "tble", 0, 0))

# def zero_one_knapsack_g(weights, values, limit):
#     dens = {}
#     res = 0
#     lim = limit
#     length = len(weights)
#     for each in range(length):
#         dens[weights[each]] = [values[each]/weights[each], values[each], weights[each]]
#     dens = dict(sorted(dens.items(), key=lambda x:x[1], reverse=True))
#     for each in dens:
#         if limit == 0:
#             return [res, lim-limit]
#         if dens[each][-1] <= limit:
#             res += dens[each][1]
#             limit -= dens[each][-1]
#     return ([res, lim-limit])

# weights = [3, 1, 2, 5, 4]
# values = [31, 26, 17, 72, 30]
# limit = 8
# print(zero_one_knapsack_g(weights, values, limit))

# def zero_one_knapsack_dnc(weights, values, limit):
#     if values == [] or weights == [] or weights[0] > limit:
#         return 0
#     elif weights[0] <= limit:
#         p1 = values[0] + zero_one_knapsack_dnc(weights[1:], values[1:], limit-weights[0])
#         p2 = 0+zero_one_knapsack_dnc(weights[1:], values[1:], limit)
#         return max(p1, p2)

# weights = [3, 1, 2, 5]
# values = [31, 26, 17, 72]
# limit = 7
# print(zero_one_knapsack_dnc(weights, values, limit))
import unicodedata, warnings

def _normalize(s):
    return unicodedata.normalize("NFKD", s)


def _check_type(s):
    # warn here since each function will call this
    warnings.warn(
        "The jellyfish._jellyfish module is deprecated and will be removed in jellyfish 1.0.",
        DeprecationWarning,
    )
    if not isinstance(s, str):
        raise TypeError("expected str or unicode, got %s" % type(s).__name__)

def soundex(s):
    _check_type(s)

    if not s:
        return ""

    s = _normalize(s)
    s = s.upper()

    replacements = (
        ("BFPV", "1"),
        ("CGJKQSXZ", "2"),
        ("DT", "3"),
        ("L", "4"),
        ("MN", "5"),
        ("R", "6"),
    )
    result = [s[0]]
    count = 1

    # find would-be replacement for first character
    for lset, sub in replacements:
        if s[0] in lset:
            last = sub
            break
    else:
        last = None

    for letter in s[1:]:
        for lset, sub in replacements:
            if letter in lset:
                if sub != last:
                    result.append(sub)
                    count += 1
                last = sub
                break
        else:
            if letter != "H" and letter != "W":
                # leave last alone if middle letter is H or W
                last = None
        if count == 4:
            break

    result += "0" * (4 - count)
    return "".join(result)

# print(soundex("n!gg@r"), soundex("nigger"))
def metaphone(s):
    _check_type(s)

    result = []

    s = _normalize(s.lower())

    # skip first character if s starts with these
    if s.startswith(("kn", "gn", "pn", "wr", "ae")):
        s = s[1:]

    i = 0

    while i < len(s):
        c = s[i]
        next = s[i + 1] if i < len(s) - 1 else "*****"
        nextnext = s[i + 2] if i < len(s) - 2 else "*****"

        # skip doubles except for cc
        if c == next and c != "c":
            i += 1
            continue

        if c in "aeiou":
            if i == 0 or s[i - 1] == " ":
                result.append(c)
        elif c == "b":
            if (not (i != 0 and s[i - 1] == "m")) or next:
                result.append("b")
        elif c == "c":
            if next == "i" and nextnext == "a" or next == "h":
                result.append("x")
                i += 1
            elif next in "iey":
                result.append("s")
                i += 1
            else:
                result.append("k")
        elif c == "d":
            if next == "g" and nextnext in "iey":
                result.append("j")
                i += 2
            else:
                result.append("t")
        elif c in "fjlmnr":
            result.append(c)
        elif c == "g":
            if next in "iey":
                result.append("j")
            elif next == "h" and nextnext and nextnext not in "aeiou":
                i += 1
            elif next == "n" and not nextnext:
                i += 1
            else:
                result.append("k")
        elif c == "h":
            if i == 0 or next in "aeiou" or s[i - 1] not in "aeiou":
                result.append("h")
        elif c == "k":
            if i == 0 or s[i - 1] != "c":
                result.append("k")
        elif c == "p":
            if next == "h":
                result.append("f")
                i += 1
            else:
                result.append("p")
        elif c == "q":
            result.append("k")
        elif c == "s":
            if next == "h":
                result.append("x")
                i += 1
            elif next == "i" and nextnext in "oa":
                result.append("x")
                i += 2
            else:
                result.append("s")
        elif c == "t":
            if next == "i" and nextnext in "oa":
                result.append("x")
            elif next == "h":
                result.append("0")
                i += 1
            elif next != "c" or nextnext != "h":
                result.append("t")
        elif c == "v":
            result.append("f")
        elif c == "w":
            if i == 0 and next == "h":
                i += 1
                result.append("w")
            elif next in "aeiou":
                result.append("w")
        elif c == "x":
            if i == 0:
                if next == "h" or (next == "i" and nextnext in "oa"):
                    result.append("x")
                else:
                    result.append("s")
            else:
                result.append("k")
                result.append("s")
        elif c == "y":
            if next in "aeiou":
                result.append("y")
        elif c == "z":
            result.append("s")
        elif c == " ":
            if len(result) > 0 and result[-1] != " ":
                result.append(" ")

        i += 1

    return "".join(result).upper()

#print(metaphone("nigger"), metaphone("nigga"))
def nysiis(s):
    _check_type(s)

    if not s:
        return ""

    s = s.upper()
    key = []

    if s.startswith("MAC"):
        s = "MCC" + s[3:]
    elif s.startswith("KN"):
        s = s[1:]
    elif s.startswith("K"):
        s = "C" + s[1:]
    elif s.startswith(("PH", "PF")):
        s = "FF" + s[2:]
    elif s.startswith("SCH"):
        s = "SSS" + s[3:]

    if s.endswith(("IE", "EE")):
        s = s[:-2] + "Y"
    elif s.endswith(("DT", "RT", "RD", "NT", "ND")):
        s = s[:-2] + "D"

    key.append(s[0])


    i = 1
    len_s = len(s)
    while i < len_s:
        ch = s[i]
        if ch == "E" and i + 1 < len_s and s[i + 1] == "V":
            ch = "AF"
            i += 1
        elif ch in "AEIOU":
            ch = "A"
        elif ch == "Q":
            ch = "G"
        elif ch == "Z":
            ch = "S"
        elif ch == "M":
            ch = "N"
        elif ch == "K":
            if i + 1 < len(s) and s[i + 1] == "N":
                ch = "N"
            else:
                ch = "C"
        elif ch == "S" and s[i + 1 : i + 3] == "CH":
            ch = "SS"
            i += 2
        elif ch == "P" and i + 1 < len(s) and s[i + 1] == "H":
            ch = "F"
            i += 1
        elif ch == "H" and (
            s[i - 1] not in "AEIOU"
            or (i + 1 < len(s) and s[i + 1] not in "AEIOU")
            or (i + 1 == len(s))
        ):
            if s[i - 1] in "AEIOU":
                ch = "A"
            else:
                ch = s[i - 1]
        elif ch == "W" and s[i - 1] in "AEIOU":
            ch = s[i - 1]

        if ch[-1] != key[-1][-1]:
            key.append(ch)

        i += 1

    key = "".join(key)

    if key.endswith("S") and key != "S":
        key = key[:-1]


    if key.endswith("AY"):
        key = key[:-2] + "Y"


    if key.endswith("A") and key != "A":
        key = key[:-1]

    return key

print(nysiis("nigga"), nysiis("nigger"))
print(nysiis("fuck"), nysiis("phuck"))