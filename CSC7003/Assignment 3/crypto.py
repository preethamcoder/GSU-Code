import string
import re
alpset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(s):
		y = ""
		hour = int(s[:2])
		for x in s[6:]:
			if(x != " "):
				y += str((alpset.index(x) + hour) % 26) + ","
			else:
				y = y[:-1] + "_"
				#y += "_"
		#finalmessage = ""
		#for i in range(len(y)-1):
		#	if(y[i] == "," and y[i+1] == "_"):
		#		pass
		#	else:
		#		finalmessage += y[i]
		return(y[:-1])
def decrypt(s):
		decryptedmess = ""
		hour = int(s[:2])
		b = re.split(',', s[6:])
		for x in b:
			if("_" not in x):
				if(x != ","):
					if(int(x) - hour < 0):
							decryptedmess += alpset[int(x) + 26 - hour]
					else:
							decryptedmess += alpset[int(x) - hour]
			else:
				f = x.split("_")
				f.insert(1, "_")
				for g in f:
					if(g != "_"):
						if(int(g) - hour < 0):
							decryptedmess += alpset[int(g) + 26 - hour]
						else:
							decryptedmess += alpset[int(g) - hour]
					else:
						decryptedmess += " "
		return(decryptedmess)
			
def main():
		while True:
			s = str(input("\nEnter e plan-text or d coded-text or q: "))
			if(s[0] == "e"):
				print("Encrypted text is: " +encrypt(s[2:]))
			elif(s[0] == "d"):
				print("Decrypted text is: " +decrypt(s[2:]))
			elif(s[0] == "q"):
				break
			else:
				print("Invalid choice")

main()
