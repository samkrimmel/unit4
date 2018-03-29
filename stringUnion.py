#Sam Krimmel
#3/28/18
#stringUnion.py - uses all letters from two words only once

def stringUnion(word1,word2):
    final = ''
    for ch in word1:
        if not ch.lower() in final.lower():
            final += ch.lower()
    for ch in word2:
        if not ch.lower() in final.lower():
            final += ch.lower()
    return final
            
        
print(stringUnion('concrete','buildingplace'))