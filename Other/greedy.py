def activites(acts):
    res = 0
    dos = []
    acts.sort(key=lambda x: x[2])
    curr_end = 0
    for each in acts:
        if each[1] >= curr_end:
            res += 1
            curr_end = each[-1]
            dos.append(each[0])
    print(dos)
    return res

act = [["A1", 0, 6], ["A2", 3, 4], ["A3", 1, 2], ["A4", 5, 8], ["A5", 5, 7], ["A6", 8, 9]]
print(activites(act))

def coin_change(amount, coins):
    print("coins are:", coins)
    print("amount is:", amount)
    res = []
    while amount != 0:
        tmp = [each for each in coins if each <= amount]
        if tmp == []:
            return -1
        amt1 = max(tmp)
        res.append(amt1)
        amount -= amt1
    print("number of coins:", len(res))
    return res

#coins = [1, 5, 10, 25, 100]
coins=[1, 5, 10, 25, 100] 
print(coin_change(14, coins))

def fractional_knapsack(weights, values, limit):
    dens = {}
    res = 0
    length = len(weights)
    for each in range(length):
        dens[weights[each]] = [(values[each]/weights[each]), values[each]]
    dens = dict(sorted(dens.items(), key=lambda x:x[1], reverse=True))
    for each in dens:
        if limit > 0 and each <=limit:
            limit -= each
            res += dens[each][-1]
        elif each > limit:
            part = (limit/each)
            res += (part*dens[each][-1])
            limit -= part
    return res

weights = [20, 30, 10]
values = [100, 120, 80]
limit = 60
print(fractional_knapsack(weights, values, limit))