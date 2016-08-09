import subprocess
import time

while True:
 f = open('.acronyms.txt')
 for line in f:
   text = line.strip()
   subprocess.call(['figlet',text])
   print("\n\n")
   time.sleep(1)