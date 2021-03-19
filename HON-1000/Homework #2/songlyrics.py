import sys
print()
def get_key(val): 
    for key, value in pos_dict.items(): 
         if(val == value): 
             return(key)

f = open(sys.argv[1], "r")
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
x = pos_dict.keys()
print()
for i in x:
	print(str(i) + "\t" + "\t" + str(pos_dict[i]))

#print(x)
print()
print("Song: ")
print()
for i in lines:
	print(i.strip())

print()
print("The number of unique words in the lyric is: " + str(len(pos_dict)))

print()
y = pos_dict.values()
freq = 0
word = ""
for i in y:
	if(len(i) > freq):
		freq = len(i)
		word = get_key(i)
print("Most frequent word: " + word)
print()
