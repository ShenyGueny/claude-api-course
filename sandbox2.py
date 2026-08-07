def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in the given string."""
    return sum(1 for char in text if char.lower() in "aeiou")


if __name__ == "__main__":
    print(count_vowels("hello world"))  # 3
