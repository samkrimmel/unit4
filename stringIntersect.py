#Sam Krimmel
#3/29/18
#stringIntersect.py - makes string of letters that appear in both words

def stringIntersect(word1,word2):
    combword = word1 + word2
    final = ' '
    for ch in combword:
        if ch.lower() not in final.lower():
            final += ch.lower()
    return final
    
print(stringIntersect('Mississippi','Pennsylvania'))
