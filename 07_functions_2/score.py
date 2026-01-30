def scoreToNumber(score):
    '''
    Returns a quantitative score based upon a qualitative score.

        Parameters:
            score (str): Qualitative score

        Returns:
            result (int): Integer score on a scale 0-10
    '''
    score = str.upper(score)
    result = 0
    first = score[0]
    if first == "G" :
        result = 10
    elif first == "O" :
        result = 5
    elif first == "P" :
        result = 3
    return result

def main():
    score1 = input('Enter score 1 as Great, Ok or Poor: ')
    score2 = input('Enter score 2 as Great, Ok or Poor: ')
    score3 = input('Enter score 3 as Great, Ok or Poor: ')
    x1 = scoreToNumber(score1)
    x2 = scoreToNumber(score2)
    x3 = scoreToNumber(score3)
    xmax = max(x1, x2, x3)
    some_avg = (x1 + x2 + x3) / 3
    print(f'The maximum score was {xmax}')
    print(f'The avg score on 1-10 scale would have been {round(some_avg, 2)}')

main()

