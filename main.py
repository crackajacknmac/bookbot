"""Okay, so I need to write a function that takes a filepath 
as input and returns a string of text instead."""

"""Awesome! The code works! Now for part 2.
Create a function  that accepts the book text as a string
and returns the number of words in the string."""


def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def book_word_count(x):
	word_count = 0
	x = get_book_text("books/frankenstein.txt")
	words = x.split()
	for each in words:
		word_count +=1
	return word_count

def main():
	num_words = book_word_count(get_book_text)
	print(f"Found {num_words} total words")

main()
