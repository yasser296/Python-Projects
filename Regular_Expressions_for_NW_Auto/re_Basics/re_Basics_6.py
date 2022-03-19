import re

print(re.findall('a[bc]', 'a, ab, ac, abc, acb, ad')) # find 'a' and ['b' or 'c']  

print(re.findall('a(b|c)', 'a, ab, ac, abc, acb, ad')) # find ('b' or 'c') after 'a' 
print(re.findall('(b|c)', 'a, ab, ac, abc, acb, ad'))

print(re.findall('3[a-f]', '3, 3a, 3c, 3f, 3g'))

print(re.findall('3(a|b|c|d|e|f)', '3, 3a, 3c, 3f, 3g'))

print(re.match('apple|raspberry', 'raspberry pie'))

print(re.findall('apple|raspberry', 'raspberry and apple pie'))
