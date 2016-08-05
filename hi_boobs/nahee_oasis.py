import time

def translate_to_symbol(text):
    printed = ''
    for i in text:
        if((i == 'b') or (i == 'o') or (i == 'B') or (i == 'O')):
            printed+=i
        else:
            printed+=" "
    time.sleep(0.3)
    print printed

with open("hi_Boobs.txt") as file:
    lines = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        lines.append(line.rstrip().split(" "))
        translate_to_symbol(line)

for num in range(1,10):
    print "How do I report an abusive photo?"
    time.sleep(0.3)