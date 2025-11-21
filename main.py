from stats import book_word_count

def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
		return text

def main():
	num_words = book_word_count(text)
	print(f"Found {num_words} total words")

main()
