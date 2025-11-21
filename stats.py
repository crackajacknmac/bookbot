def book_word_count(text):
        word_count = 0
        wc_text = text
        words = wc_text.split()
        for each in words:
                word_count +=1
        return word_count
