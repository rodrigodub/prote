Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:03:43) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> inputFileName = "BriefcaseReport.txt"
>>> 
>>> 
>>> 
>>> inputFileName
'BriefcaseReport.txt'
>>> inputFileName.rfind('.')
15
>>> inputFileName[inputFileName.rfind('.')-4:
	      inputFileName.rfind('.')]
'port'
>>> inputFileName[inputFileName.rfind('.')-3:
	      inputFileName.rfind('.')]
'ort'
>>> ordem = inputFileName[inputFileName.rfind('.')-3:
	      inputFileName.rfind('.')]
>>> ordem
'ort'
>>> int(ordem)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    int(ordem)
ValueError: invalid literal for int() with base 10: 'ort'
>>> ordem.isdigit()
False
>>> ordem = '12345'
>>> ordem.isdigit()
True
>>> ordem = 123
>>> ordem.isdigit()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ordem.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> ordem = '12345'
>>> ordem.isdigit()
True
>>> ordem = inputFileName[inputFileName.rfind('.')-3:
	      inputFileName.rfind('.')]
>>> ordem.isdigit()
False
>>> 
