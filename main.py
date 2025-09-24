from stats import *

def get_book_text(filepath: str) -> str: 
    with open(filepath) as f:
        return f.read()
    
def main() -> None:
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    wordCount = count_words(book_text)
    sorted_charCounts = sort_dict(count_characters(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")
    for item in sorted_charCounts:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
main()