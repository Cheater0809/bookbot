from stats import *

def get_book_text(filepath: str) -> str: 
    with open(filepath) as f:
        return f.read()
    
def main() -> None:
    wordCount = count_words(get_book_text("books/frankenstein.txt"))
    charCounts = count_characters(get_book_text("books/frankenstein.txt"))
    print (f"Found {wordCount} total words")
    print (charCounts)
    
main()