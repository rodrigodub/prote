Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> inputFileName = "BriefcaseReport.txt"
>>> fileNameIncrement = 1
>>> stringIncrement = "000" + str(fileNameIncrement)
>>> stringIncrement
'0001'
>>> stringIncrement[:-3]
'0'
>>> stringIncrement[1:4]
'001'
>>> stringIncrement[:3]
'000'
>>> stringIncrement[:-2]
'00'
>>> stringIncrement[:-1]
'000'
>>> stringIncrement[-3:]
'001'
>>> stringIncrement = ("00" + str(fileNameIncrement))[-3:]
>>> stringIncrement
'001'
>>> fileNameIncrement++
SyntaxError: invalid syntax
>>> fileNameIncrement += 1
>>> fileNameIncrement
2
>>> fileNameIncrement += 1
>>> fileNameIncrement
3
>>> stringIncrement = ("00" + str(fileNameIncrement))[-3:]
>>> stringIncrement
'003'
>>> fileNameIncrement = 14
>>> stringIncrement = ("00" + str(fileNameIncrement))[-3:]
>>> stringIncrement
'014'
>>> fileNameIncrement = 1
>>> inputFileName[:-3]
'BriefcaseReport.'
>>> inputFileName[:-4]
'BriefcaseReport'
>>> inputFileName[-4:]
'.txt'
>>> outputFileName = inputFileName[:-4] + "_" + stringIncrement + inputFileName[-4:]
>>> outputFileName
'BriefcaseReport_014.txt'
>>> stringIncrement = ("00" + str(fileNameIncrement))[-3:]
>>> outputFileName = inputFileName[:-4] + "_" + stringIncrement + inputFileName[-4:]
>>> outputFileName
'BriefcaseReport_001.txt'
>>> 
