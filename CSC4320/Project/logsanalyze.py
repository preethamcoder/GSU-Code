import os
import sys

def parse_logs(file):
    f = open(file, "r")
    data = f.readlines()
    commands = {}
    for elem in data:
        com = elem.split()[0]
        if(com in commands):
            commands[com] += 1
        else:
            commands[com] = 1
    command_ext = {}
    for command in commands:
        command_ext[command] = []
    for ext in data:
        com = ext.split()[0]
        arg1 = ''
        try:
            arg1 = ext.split()[1]
        except:
            command_ext[com].append('')
        if(arg1 != ''):
            command_ext[com].append(arg1)
    command_ext_freq = {}
    for command in commands:
        for occur in command_ext[command]:
            command_ext_freq[command + ' ' + occur] = command_ext[command].count(occur)
    return command_ext_freq

def return_max_extention(command, commands_frequency):
    com = {}
    for comm in commands_frequency.keys():
        if command==comm[:len(command)]:
            com[comm[len(command)+1:]] = commands_frequency[comm]
    most_freq = ''
    try:
        most_freq = max(com, key = com.get)
    except:
        print("Command not used in the past. This is the first occurence of it!")
        return
    return(most_freq)

if __name__ == '__main__':
    result = parse_logs(sys.argv[1])
    res = 'y'
    while(res != 'no'):
        lookup = input("Enter your command: ")
        ext = return_max_extention(lookup, result)
        if(ext != None and 'history' not in lookup):
            print(f"Most used extention for {lookup} is", ext)
            print("Your command would be:", lookup+" "+ext)
            inp2 = input(f"Add extentions to {lookup} {ext} if needed: ")
            os.system(lookup+ " " + ext + inp2)
        if(ext != None and 'history' in lookup):
            print("Your command would be:", lookup+" "+ext)
            inp2 = input(f"Add extentions to {lookup} {ext} if needed: ")
            lookup = f'cat {sys.argv[1]} '
            os.system(lookup+ ext + inp2)
        res = input("Type 'no' if you don't wish to try any more commands. Hit enter if you want to continue:  ")
