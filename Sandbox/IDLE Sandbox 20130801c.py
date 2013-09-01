Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> inputFileName = "BriefcaseReport.txt"
>>> ordem = inputFileName[inputFileName.rfind('.')-3:
	      inputFileName.rfind('.')]
>>> ordem
'ort'
>>> ordem.isdigit()
False
>>> if ordem.isdigit():
	return int(ordem) + 1
SyntaxError: 'return' outside function
>>> if ordem.isdigit():
	print(int(ordem)+1)

	
>>> if ordem.isdigit():
	print(int(ordem)+1)
	else:
		
SyntaxError: invalid syntax
>>> if ordem.isdigit():
	print(int(ordem)+1)
else:
	print('001')

	
001
>>> inputFileName = "BriefcaseReport_012.txt"
>>> ordem
'ort'
>>> ordem = inputFileName[inputFileName.rfind('.')-3:
	      inputFileName.rfind('.')]
>>> ordem
'012'
>>> if ordem.isdigit():
	print(int(ordem)+1)
else:
	print('001')

	
13
>>> 
