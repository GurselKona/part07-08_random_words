def words(n: int, beginning: str)-> list[str]:
    import random
    import string
    """Return a list of n random words that begin with beginning."""
    with open('words.txt') as f:
        words = f.readlines()
        words = [word.strip() for word in words]
    words_sublist = []
    for word in words:
        if word.startswith(beginning):
            words_sublist.append(word)
    if len(words_sublist) < n:
        raise ValueError("Not enough words in the list.")    
    return random.sample(words_sublist, n)


if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)