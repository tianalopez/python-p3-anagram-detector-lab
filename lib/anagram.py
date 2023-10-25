
class Anagram:

  def __init__(self, word):
    self.word = word

  def match(self, word_list):
    anagram_list = []
    match_list = list(self.word)
    for el in word_list:
      potential_match = list(el)
      match_list.sort()
      potential_match.sort()
      if match_list == potential_match:
        anagram_list.append(el)
      else:
        return anagram_list

#refactored solution for the definition

  # def match(self, word_list):
  #   anagram_list=[]
  #   match_list=sorted(self.word) #returns a new sorted list, not modified
  #   for el in word_list:
  #     if sorted(el) == match_list:
  #       anagram_list.append(el)

  #   return anagram_list
