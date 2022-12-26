s_word = input()
t_word = input()

s_hashmap = {}
result = ''
for s_letter in s_word:
    s_hashmap[s_letter] = s_hashmap.get(s_letter, 0) + 1

for t_letter in t_word:
    s_hashmap[t_letter] = s_hashmap.get(t_letter, 0) - 1
    if s_hashmap[t_letter] < 0:
        result = t_letter
        break

print(result)