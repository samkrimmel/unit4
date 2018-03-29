#Sam Krimmel
#3/28/18
#stringUnion.py - uses all letters from two words only once

def stringUnion(word1,word2):
    final = str('')
    for ch in word1:
        if not ch in final:
            final += str(ch)
    for ch in word2:
        if not ch in final:
            final += str(ch)
            
        
stringUnion('Mississippi','Pennsylvania')