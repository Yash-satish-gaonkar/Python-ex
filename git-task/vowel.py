def count(words):
    vowels = "aeiouAEIOU"
    return {word: sum(1 for ch in word if ch in vowels) for word in words}

print(count(["apple", "sky", "orange"]))
