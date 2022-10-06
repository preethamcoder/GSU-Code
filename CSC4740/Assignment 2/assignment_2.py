def edit_distance(s1: str, s2: str) -> int:
    l1 = len(s1)
    l2 = len(s2)
    if not s1:
        return l2
    if not s2:
        return l1
    dp = [[0 for x in range(l2 + 1)] for x in range(l1 + 1)]
    for ind in range(l1 + 1):
        for ind2 in range(l2 + 1):
            if ind == 0:
                dp[ind][ind2] = ind2
            elif ind2 == 0:
                dp[ind][ind2] = ind
            elif s1[ind-1] == s2[ind2-1]:
                dp[ind][ind2] = dp[ind-1][ind2-1]
            else:
                dp[ind][ind2] = 1 + min(dp[ind][ind2-1], dp[ind-1][ind2], dp[ind-1][ind2-1])
    return dp[l1][l2]

if __name__ == '__main__':
    print(edit_distance("kitten", "sitting"))
    print(edit_distance("GAMBOL", "GUMBO"))
    
