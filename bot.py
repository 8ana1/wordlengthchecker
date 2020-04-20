def main():
    sentence = input("Please, enter a sentence: ")
    longest_word = get_longest_word(sentence)
    shortest_word = get_shortest_word(sentence)
    longest_word_len = get_word_length(longest_word)
    shortest_word_len = get_word_length(shortest_word)
    print("Longest word is %s and its length is %s" % (longest_word, longest_word_len))
    print("Shortest word word is %s and its length is %s" % (shortest_word, shortest_word_len))


def get_longest_word(sentence):
    words = str(sentence).split()
    if words:
        longest_word = words[0]
    else:
        return None

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def get_shortest_word(sentence):
    words = str(sentence).split()
    if words:
        shortest_word = words[0]
    else:
        return None
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word


def get_word_length(word):
    return len(word)


if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            break
