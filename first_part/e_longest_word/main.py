n = int(input())
words = [word for word in input().split(' ')]
the_biggest_word = ''

for word in words:
    if len(word) > len(the_biggest_word):
        the_biggest_word = word


print(the_biggest_word, '\n', len(the_biggest_word))