def longest_word(word_lst):
    best=''

    for i in word_lst:
        if len(i)>len(best):
            best=i
    return best
