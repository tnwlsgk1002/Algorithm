def solution(n, words):
    added_words = set()
    for i, word in enumerate(words):        
        if word in added_words or (i > 0 and words[i - 1][-1] != word[0]) :
            number = (i + 1) % n if (i + 1) % n != 0 else n
            order = (i + 1) // n if (i + 1) % n == 0 else (i + 1) // n + 1
            return [number, order]
        added_words.add(word)
    return [0, 0]