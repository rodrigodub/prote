Python 2.6.5 (r265:79096, Mar 19 2010, 21:48:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

    ****************************************************************
    Personal firewall software may warn about the connection IDLE
    makes to its subprocess using this computer's internal loopback
    interface.  This connection is not visible on any external
    interface and no data is sent to or received from the Internet.
    ****************************************************************
    
IDLE 2.6.5      
>>> class Prote:
	inputFileName = 'BriefcaseReport.txt'
	def outputFileName1(self):
		return Prote.inputFileName[:-4] + '_' + '000' + Prote.inputFileName[-4:]
	def outputFileName2(self):
		return self.inputFileName[:-4] + '_' + '000' + self.inputFileName[-4:]

	
>>> teste = Prote()
>>> teste.inputFileName
'BriefcaseReport.txt'
>>> teste.outputFileName1()
'BriefcaseReport_000.txt'
>>> teste.outputFileName2()
'BriefcaseReport_000.txt'
>>> teste.inputFileName = 'ImportReport.txt'
>>> teste.outputFileName1()
'BriefcaseReport_000.txt'
>>> teste.inputFileName
'ImportReport.txt'
>>> teste.outputFileName2()
'ImportReport_000.txt'
>>> 
