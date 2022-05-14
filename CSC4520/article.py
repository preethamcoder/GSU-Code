"""Given a string and an article cutting, return a boolean if you can create the string with letters from the article cutting"""

def poss(small, large):
    res = True
    freqs = {}
    for each in small:
        freqs[each] = small.count(each)
    for each in freqs:
        if freqs[each] <= large.count(each):
            res = True
        else:
            res = False
            break
    return res
 
if __name__ == '__main__':
  sm = "atlanta is a citaxey".replace(" ", "")
  lrg = "Come collaborate in the expo hall, connect at our networking reception, and deep dive into cloud computing technology with interactive workshops and sessions. Day 1 is perfect for those new to their cloud computing journey.".lower().replace(" ", "")
  print(poss(sm, lrg))
