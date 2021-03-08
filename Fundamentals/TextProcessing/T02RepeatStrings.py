def repeat_strings_by_length(words):
    return words*len(words)
words=input().split()
print(''.join(map(repeat_strings_by_length,words)))
# todo lambda analog bez funkciq gore
#print(''.join(map(lambda word:word*len(word),words)))