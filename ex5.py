word = input().upper()
def score(word):
    score = 0
    for letter in word:
        if letter in 'AEILNORSTU ':
            score += 1
        elif letter in 'DGM':
            score += 2
        elif letter in 'BCP':
            score += 3
        elif letter in 'FHV':
            score += 4
        elif letter in 'JQ':
            score += 8
        elif letter in 'KWXYZ':
            score += 10
    return score
print(score(word))