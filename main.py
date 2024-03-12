def main():
    path = "books/frankenstein.txt"
    split_book_text = text_splitter(get_book_text(path))
    count_list = []

    print(f"{word_count(split_book_text)} words found in the document.")
    
    char_counts = char_counter(split_book_text)

    for a in char_counts:
        if a.isalpha():
            # print(f"The key is {a} the count is {char_counts[a]}")
            count_list.append({"letter": a, "count": char_counts[a]})
    
    count_list.sort(key=sort_on)
    
    for b in count_list:
        print(f"The {b['letter']} was found {b['count']} times")



    



def get_book_text(path):
    with open (path) as f:
        return f.read()

def text_splitter(text):
    return text.split()

def word_count(text):
    return len(text)

def char_counter(text):
    char_count = dict()

    for word in text:
        word = word.lower()
        for letter in word:
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    return char_count

def sort_on(dict):
    return dict["letter"]



main()