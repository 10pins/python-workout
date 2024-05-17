### Exercise 5 - Pig Latin ###

def pig_latin(word: str):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'


if __name__ == "__main__":
    print(pig_latin('computer'))