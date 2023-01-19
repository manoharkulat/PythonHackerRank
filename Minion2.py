def minion_game(string):
    # your code goes here
       #---------------- need to analyse. v3 Important
    vowels = 'AEIOU'
    stuartScore = 0
    kevinScore = 0

    strLen = len(string)

    for idx in range(strLen):
        if(string[idx] in vowels):
            kevinScore += (strLen - idx)
        else:
            stuartScore += (strLen - idx)

    if stuartScore > kevinScore:
        print('Stuart', stuartScore)
    elif kevinScore > stuartScore:
        print('Kevin', kevinScore)
    elif kevinScore == stuartScore:
        print('Draw')
if __name__ == '__main__':
    s = "SACHIN"
    minion_game(s)