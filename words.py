def print_upper_words(words):
    """Print each uppercase word on a separate line."""
    for word in words:
        print(word.upper())


print(print_upper_words(['hello', 'there', 'how', 'are', 'you']), "Should print 'HELLO THERE HOW ARE YOU'")


def print_upper_words_v2(words):
    """Only print uppercase if word starts with the letter E"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


print(print_upper_words_v2(['hello', 'everybody']), "Should print 'EVERYBODY'")


def print_upper_words_v3(words, start):
    """Print every letter uppercase, but only words starting with the letter given"""
    for word in words:
        for char in start:
            if word.startswith(char):
                print(word.upper())
                break


print(print_upper_words_v3(['hello', 'how', 'are', 'you'], 'y'), "Should return 'YOU'")
print(print_upper_words_v3(['hello', 'how', 'are', 'you'], 'h'), "Should return 'HELLO' and 'HOW'")
