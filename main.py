def get_book_text(filepath: str) -> str: 
    with open(filepath) as f:
        return f.read()
    
def count_words(text: str) -> int:
    words = text.split()
    return len(words)
    
    
def main() -> None:
    print (f"Found {count_words(get_book_text("books/frankenstein.txt"))} total words")
    
main()