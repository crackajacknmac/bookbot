"""Okay, so I need to write a function that takes a filepath 
as input and returns a string of text instead."""

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
	x = get_book_text("books/frankenstein.txt")
	print(x)

main()
