def book_word_count(text):
        word_count = 0
        x = get_book_text(text)
        words = text.split()
        for each in words:
                word_count +=1
        return word_count
