from wordfrequencies import read_file, word_frequency
from wordcount import word_count
from uniquewords import unique_word
from vocabularyrichness import vocabulary_richness
from longestword import longest_word
from averagewordlength import average_word_length
from mostcommonword import most_common_word
from filteredtop20 import filtered
from sentence import sentence_lst, sentence_count, avg_sentence_count

filename = input('give file name: ')

while True:
    filename = input('give file name: ')
    try:
        words = read_file(filename)
        break
    except FileNotFoundError:
        print('File not found, please try again.')

d = word_frequency(words)
sents = sentence_lst(filename)

total = word_count(words)
unique = unique_word(d)
richness = vocabulary_richness(total, unique)
avg_len = average_word_length(words)
longest = longest_word(words)
sent_count = sentence_count(sents)
avg_sent = avg_sentence_count(sents)
top = most_common_word(d)
top_filtered = filtered(d)


report = 'Total words: ' + str(total) + '\n'
report += 'Unique words: ' + str(unique) + '\n'
report += 'Vocabulary richness: ' + str(round(richness, 3)) + '\n'
report += 'Average word length: ' + str(round(avg_len, 2)) + '\n'
report += 'Longest word: ' + longest + '\n'
report += 'Sentence count: ' + str(sent_count) + '\n'
report += 'Average sentence length: ' + str(round(avg_sent, 2)) + '\n'

report += '\nTop 20 words:\n'
for word, count in top.items():
    report += word + ': ' + str(count) + '\n'

report += '\nTop 20 words without filler words:\n'
for word, count in top_filtered.items():
    report += word + ': ' + str(count) + '\n'

print()
print(report)

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(report)
print('Report saved to report.txt')