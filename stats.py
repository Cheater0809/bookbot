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

def sort_on(items):
    return items["num"]

def sort_dict(unsorted: dict):
    sorted_dicts = [{"char": key, "num": value} for key, value in unsorted.items()]
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts