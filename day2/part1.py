score = 0
resultPoints = {'WIN': 6, 'DRAW': 3, 'LOSS': 0}

for line in open('input.txt', 'r').read().splitlines():
    opponent, me = line.split()
    match me:
        case 'X':
            score += 1
            if (opponent == 'C'):
                score += resultPoints['WIN']
            elif (opponent == 'A'):
                score += resultPoints['DRAW']
        case 'Y':
            score += 2
            if (opponent == 'A'):
                score += resultPoints['WIN']
            elif (opponent == 'B'):
                score += resultPoints['DRAW']
        case 'Z':
            score += 3
            if (opponent == 'B'):
                score += resultPoints['WIN']
            elif (opponent == 'C'):
                score += resultPoints['DRAW']
            
print(score)