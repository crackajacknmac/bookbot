from stats import book_word_count

def get_book_text(filepath):
	with open("books/frankenstein.txt") as f:
		book_string = f.read()
		return book_string

def main():
	text = get_book_text("books/frankenstein.txt")
	num_words = book_word_count(text)
	print(f"Found {num_words} total words")

main()
