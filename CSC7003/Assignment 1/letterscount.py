import matplotlib.pyplot as plt
import string, sys
# this function takes the name of a file as input parameter, fname
# it then reads the file into a string variable
# then proceeds to process the string for the count of letters
# answer should be returned in a list of 26 numbers

def draw(counts):
    lett = list(string.ascii_lowercase)
    xaxis = range(len(lett))
    plt.figure(figsize=(12,8)) 
    plt.title("Letter Counts in " + sys.argv[1][2:])
    plt.xlabel("Letter")
    plt.ylabel("Occurences")
    plt.bar(xaxis, counts, width=0.5)
    plt.xticks(xaxis, lett)
    for a,b in zip(xaxis, counts):
        plt.text(a, b+8, str(b), horizontalalignment='center', verticalalignment='center')
    plt.show()

    
#main()
def get_count(fname):
    #print("In function")
    with open(fname, encoding='utf8') as f:
        data = f.read().lower()
        #return(data)
        letters = list(string.ascii_lowercase)
        numbers = []
        for i in letters:
            numbers.append(data.count(i))
        return numbers

def main():
    counts = get_count(sys.argv[1])
    draw(counts)
#print(counts)
main()
