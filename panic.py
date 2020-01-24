phrase = "Don't panic!"

plist = list(phrase)

print(phrase)
print(plist)

''' Remove char D >> on't panic! '''
plist.pop(0)

''' Remove ' >> ont panic! '''
plist.remove("'")

''' Remove last 4 chars >> ont pa '''
for i in range(4):
    plist.pop()

''' Switch last 2 chars >> ont ap '''
plist.extend([plist.pop(), plist.pop()])

''' Remove/insert space >> on tap '''
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)

print(plist)
print(new_phrase)
