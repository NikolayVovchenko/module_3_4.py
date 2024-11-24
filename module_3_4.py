import re

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i in other_words:
            re.search(root_word, i)
            same_words.append(i)

    return same_words
result = single_root_words('rich', 'richies', 'cheers', 'olichalcum', 'richiest')
print(result)
result2 = single_root_words('Disablement', 'Mable', 'Able', 'Disable', 'Bagel')
print(result2)


