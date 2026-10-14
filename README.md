# Text Analyzer

A Python program that analyzes any plain-text book and prints a summary.

## What it does
- Total words, unique words, vocabulary richness
- Average word length and longest word
- Sentence count and average sentence length
- Top 20 most common words, with and without filler words
- Saves the results to `report.txt`

## How to run
1. Put a plain-text book (for example from gutenberg.org) in the project folder.
2. Run `python3 main.py`
3. Type the book's filename when asked.

## Files
- `main.py`: runs everything and prints the summary
- `wordfrequencies.py`: reads and cleans the text, counts words
- `sentence.py`: sentence statistics
- other files: one statistic per file

## Notes
Written from scratch with no external libraries.
Sorting is hand-written, so it takes a few seconds on large books.