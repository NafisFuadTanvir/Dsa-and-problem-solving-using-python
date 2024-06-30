"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

"""

def mostWordsFound( sentences):
        maxlength=0
        for sentence in sentences:
                split_sentence= sentence.split()
                split_sentence_length= len(split_sentence)
                if  split_sentence_length> maxlength:
                     maxlength= split_sentence_length
        return maxlength                


print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))