def book_word_count(text):
        word_count = 0
        wc_text = text
        words = wc_text.split()
        for each in words:
                word_count +=1
        return word_count

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

"""Okay, so let's break down the problem specifically.

We need to add a function that takes the key values of character_dict (letter: qty)
and adds them to a new dictionary.
That dictionary needs to be then added to a list.
All the letters need their own dictionary in the list.
That list needs to be called and printed as output to the terminal.
Output must be in alphabetical order and just as shown in the lesson."""

def create_sorted_list(character_dict):
	report_list = [] #Here's the list that all the dictionaries will save to.
	for entry in character_dict: #This iterates over the key/values in the dictionary
		if entry.isalpha(): #This triggers the if statement for only alphabetical characters
			report_list.append(character_dict) #This adds the dictionary entry to the list

	return report_list
