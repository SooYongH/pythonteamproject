def word_count(statement):
    words=statement.lower()
    words_list=words.split()
    words_dict={}
    for i in words_list:
        if i in words_dict.keys():
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return words_dict

statement= '''Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go, I don't know
She wouldn't say
I said something wrong
Now I long for yesterday'''

word_cnt=word_count(statement)
print('{:12s} {:>s}'.format('word','count'))
print('-'*20)
for word,cnt in word_cnt.items():
    print(f'{word:12s}{cnt:4d}')