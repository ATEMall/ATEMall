lines=[
'2026-03-25:15:14:59:520 [00/08/28,08:19:24.0702,0040]#11_CAN=1,STD,0X07FA,0X0296000000000000;',
'2026-03-25:15:14:59:725 [00/08/28,08:19:24.0946,0040]#11_CAN=3,STD,0X07FA,0X0300000000000000;'
]
canChannel='#11_CAN=1,STD,0X07FA'
filtered = lines[:]
cc = canChannel.lower()

print('cc', cc)
temp = [line for line in filtered if cc in line.lower()]
print('exact', len(temp))
if len(temp) == 0:
    searchTerms = [t for t in canChannel.replace(',', ' ').replace('_', ' ').split() if t]
    print('terms', searchTerms)
    temp = [line for line in filtered if all(term.lower() in line.lower() for term in searchTerms)]
    print('terms match', len(temp))

print('chosen', temp)
