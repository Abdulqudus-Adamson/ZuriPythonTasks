# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(f'{filename}', 'r') as file:
        texts = file.read()
        return texts


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counter_dictionary = {}
    symbols = [" ", ",", ".", "?", "\n"]

    for word in text:
        if word in symbols:
            continue
        counter_dictionary[word.lower()] = counter_dictionary.get(
            word.lower(), 0)+1

    return counter_dictionary


print(count_words())
