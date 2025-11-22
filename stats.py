def book_word_count(text):
        word_count = 0
        wc_text = text
        words = wc_text.split()
        for each in words:
                word_count +=1
        return word_count"

def character_count(text):
	character_dict ={}
	words = text.lower()
	for each in words:
		if each not in character_dict:
			character_dict[each] = 0
		if each in character_dict:
			character_dict[each] += 1
	return character_dict

"""Don't touch above this line"""

def create_sorted_list(character_dict)

