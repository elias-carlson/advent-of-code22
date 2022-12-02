score = 0
resultPoints = {'WIN': 6, 'DRAW': 3, 'LOSS': 0}

for line in open('input.txt', 'r').read().splitlines():
    opponent, result = line.split()
    match result:
        case 'X':
            if (opponent == 'A'):
                score += 3
            elif (opponent == 'B'):
                score += 1
            elif (opponent == 'C'):
                score += 2
            score += resultPoints['LOSS']
        case 'Y':
            if (opponent == 'A'):
                score += 1
            elif (opponent == 'B'):
                score += 2
            elif (opponent == 'C'):
                score += 3
            score += resultPoints['DRAW']
        case 'Z':
            if (opponent == 'A'):
                score += 2
            elif (opponent == 'B'):
                score += 3
            elif (opponent == 'C'):
                score += 1
            score += resultPoints['WIN']
            
print(score)