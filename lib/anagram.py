# your code goes here!
class Anagram:
  def __init__(self, word):
    self.word = word.lower()  # Convert to lowercase for case-insensitive matching

  def match(self, possible_anagrams):
    anagrams = []
    for word in possible_anagrams:
      if sorted(list(self.word)) == sorted(list(word.lower())):
        anagrams.append(word)
    return anagrams

# Usage
listen = Anagram("listen")
matches = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(matches)  # Output: ['inlets']