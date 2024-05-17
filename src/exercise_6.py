### Exercise 6 - Pig Latin sentence ###

def pig_latin(word: str):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

def pl_scentence(scentence):
    new_scentence = ''
    for word in scentence.split():
        new_scentence += pig_latin(word) + ' '

    return new_scentence[:-1]

if __name__ == "__main__":
    print(pl_scentence('this is a test translation'))