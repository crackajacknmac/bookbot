import sys
from stats import book_word_count
from stats import character_count
from stats import create_sorted_list

def get_book_text(filepath):
	with open(sys.argv[1]) as f:
		book_string = f.read()
		return book_string

def main():
	if len(sys.argv) <= 1:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	text = get_book_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}")
	print("----------- Word Count ----------")
	num_words = book_word_count(text)
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	character_counter = character_count(text)
	final_result = create_sorted_list(character_counter)
	for entry in final_result:
		print(f"{entry["char"]}: {entry["num"]}")
	print("============= END ===============")

main()
