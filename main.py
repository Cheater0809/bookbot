from stats import count_words

def get_book_text(filepath: str) -> str: 
    with open(filepath) as f:
        return f.read()
    
def main() -> None:
    print (f"Found {count_words(get_book_text("books/frankenstein.txt"))} total words")
    
main()