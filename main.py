def find_anagram(word, anagram):
    # [assignment] Add your code here

    comparator = []
    index = 0  # created to be used to loop through the letters of the word
    is_anagram = True

# while length of word is same as anagram and the index is less than the length of the word
    while len(word) == len(anagram) and index < len(word):
        # converts every letter in the word to lowercase
        letter = word[index].lower()
        if not letter in anagram.lower():  # if a particular letter in word is not in anagram, is_anagram will be false
            is_anagram = False
        else:
            # else the letter is appended to the list
            comparator.append(letter)

        index += 1  # the index is incremented by 1

    # if length of the comparator is same as the anagram,since we appended words similar to both word and anagram into it
    if len(comparator) == len(anagram):

        # so if the lengths are the same , it means they are same and returns true
        return True

    else:
        return False


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
