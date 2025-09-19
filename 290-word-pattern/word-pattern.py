class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word={}
        word_to_char={}
        word_list = s.split(" ")

        if len(pattern)!= len(word_list):
            return False
        else:
            for i in range(len(pattern)):
                char= pattern[i]
                word=word_list[i]

                if word in word_to_char:
                    if word_to_char[word]!= char:
                     return False
                else:
                        word_to_char[word]= char # keep the letter and word matching

                if char in char_to_word:
                    if word!= char_to_word[char]:
                        return False
                else: 
                        char_to_word[char]=word
               
            return True