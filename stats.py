def count_words(text: str) -> int:
    words = text.split()
    return len(words)
    
def count_characters(text: str) -> dict[str, int]:
    num_character = dict()
    for char in text.lower():
        if num_character.get(char) == None:
            num_character[char] = 1
        else:
            num_character[char] += 1
    return num_character