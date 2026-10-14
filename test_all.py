import sys
from wordfrequencies import read_file, word_frequency
from wordcount import word_count
from uniquewords import unique_word
from vocabularyrichness import vocabulary_richness
from longestword import longest_word
from averagewordlength import average_word_length
from mostcommonword import most_common_word
from filteredtop20 import filtered
from sentence import sentence_lst, sentence_count, avg_sentence_count
F=sys.argv[1]
w=read_file(F); d=word_frequency(w); s=sentence_lst(F)
t=word_count(w); u=unique_word(d)
print(t,u,vocabulary_richness(t,u)); print(average_word_length(w),longest_word(w))
print(list(most_common_word(d).items())[:5]); print(list(filtered(d).items())[:5])
print(sentence_count(s),avg_sentence_count(s))
