import re 

print( re.findall('\dx\d+' , "Configuration register is 0x2102")[0] )

print('######################################################################################\n\n\n')


print( re.match('\d\w\d+' , "0x2142 Configuration register is 0x2102")[0] )

print( re.match('[a-z]+' , "abc register is 0x2102") )
print( re.match('[a-z]+' , "Abc register is 0x2102") )
print('######################################################################################\n\n\n')


print( re.search('[a-z]+' , "Abc register is 0x2102")[0] )
print('######################################################################################\n\n\n')

print( re.findall('[a-z]+' , "Abc register is 0x2102") )

print( re.findall('[a-z]+' , "ASDXCZCtCCSDZDDZCCCCCCCCCCDShDLS,L,CSL,CSAiD;S,D;,SD;,;sD,LDS,DAL,,F,FLE; LADLDLDLLFJGKV,,i,FLD,SF.V.AsDMKSMFKMDKMKDFDMKDFSK UEIIOFJLLLLAKsLDF,DLSMFLDS,eLMFDLMFMLDKJFKDSJJJcJSDJFHJSFHSJFHJFDBDFBrSNDJFJDFNSDNFJSNFDJSFVMCNKeKMAKFAMKMDKMKSDNFSDKHKFJtMKSDMFKMFDKNDFKNV,DSM,M MLDMFNFKGNKFNN MNFKNSGKJNSFKSND KNSFKNSGKNSKSNKNSKGSNK KDHM;GMLGMSDFGLD;GMAMGK/B ,N,CGIOOMFMGKA.DKL"))
print('######################################################################################\n\n\n')


print( re.finditer('[a-z]+' , "Abc register is 0x2102") )


iteration = re.finditer('[a-z]+' , "Abc register is 0x2102")
l = list()
for r in iteration: l = l + [r[0]]
print(l)



print('######################################################################################\n\n\n')




