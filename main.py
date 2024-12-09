def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(file_contents), "words found in the document", end="\n\n")
    num_of_chars = char_count(file_contents)
    sorted_chars = sort_dict(num_of_chars)
    for d in sorted_chars:
        character = d["char"]
        total = d["num"]
        print(f"The '{character}' character was found {total} times")
def word_count(s):
    """ 
    Counts the number of words in a string

    Args: 
        s (string): input text
    
    Returns:
        int: The Number of words
    """
    return len(s.split())

def char_count(s):
    """
        Counts the occurances of each char in a string

        Args:
            s (string): input string

        Returns:
            dict:
                key: character
                value: number of occurances
    """
    count = {}
    lower_string = s.lower()
    for c in lower_string:
        if c in count and c.isalpha():
            count[c] += 1
        elif c not in count and c.isalpha():
            count[c] = 1
    return count

def sort_on(d):
    return d["num"]
def sort_dict(d):
    list_to_sort = []
    for x,y in d.items():
        list_to_sort.append({"char":x, "num":y})
    list_to_sort.sort(reverse=True, key=sort_on)
    return list_to_sort
main()
