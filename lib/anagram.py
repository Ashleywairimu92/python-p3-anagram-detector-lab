class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        """Returns a list of words that are anagrams of the initialized word."""
        def sorted_word(word):
            return ''.join(sorted(word))

        sorted_word_to_match = sorted_word(self.word)
        return [word for word in words if sorted_word(word) == sorted_word_to_match]

