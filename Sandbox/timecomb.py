

from datetime import *

def timecomb():
	comb = str(datetime.now().year) + ('0' + str(datetime.now().month))[-2:] + ('0' + str(datetime.now().day))[-2:] + ('0' + str(datetime.now().hour))[-2:] + ('0' + str(datetime.now().minute))[-2:] + ('0' + str(datetime.now().second))[-2:]
	return comb

#print(timecomb())

file1 = r'C:\Users\rnobrega.METECH\Dropbox\Projetos Atuais\Prote\Sandbox\Briefcase_Rehab.txt'

file2 = file1[:-4] + '_temp'

file3 = file2[:-5] + '_' + timecomb() + file1[-4:]

print('file1 : ' + file1)
print('file2 : ' + file2)
print('file3 : ' + file3)

