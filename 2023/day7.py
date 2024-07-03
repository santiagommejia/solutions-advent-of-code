def getType(hand):
    print('before', hand)
    hand = sorted(hand)
    print('after', hand)
    return 'dummy'
# Part 1 
with open('input7.txt') as openfileobject:
    for line in openfileobject:
        hand = line.split(' ')[0]
        bid = line.split(' ')[1]
        handType = getType(hand)


