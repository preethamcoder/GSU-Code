import sys
def createdict1(fname):
    f = open(fname, "r")
    lines = f.readlines()
    pos_dict = {}
    pos = 1
    print("Map: ")
    for line in lines:
        words = (line.strip()).split()
        #print(words)
        for index, word in enumerate(words):
            word = word.upper()
            if(index == len(words)-1):
                pos2 = -pos
            else:
                pos2 = pos
            if word in pos_dict:
                pos_dict[word] = pos_dict[word] + [pos2]
            else:
                pos_dict[word] = [pos2]
            pos = pos + 1
            #print(pos_dict)
    return pos_dict
def main():
	d = createdict1(sys.argv[1])
	print(d)

main()
