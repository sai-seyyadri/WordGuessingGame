def count_char(word, word_think):
    char_frequency=0
    for char in word:
        if word_think ==char:
             char_frequency = char_frequency + 1
    return char_frequency