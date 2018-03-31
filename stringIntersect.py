#Sam Krimmel
#3/29/18
#stringIntersect.py - makes string of letters that appear in both words

def stringIntersect(word1,word2):
    final = ' '
    for ch in word1:
        if ch.lower() in word2.lower() and ch.lower() not in final:
            final += ch.lower()
    return final
    
print(stringIntersect('Mississippi','Pennsylvania'))
