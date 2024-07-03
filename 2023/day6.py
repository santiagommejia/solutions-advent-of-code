import math

# Part 1 
with open('input6.txt') as openfileobject:
    time = []
    record =[]
    total = 1
    for line in openfileobject:
        if line.startswith('Time:'):
            time = line.split(':')[1].strip().split(' ')
            time = [int(x) for x in time if x != ""]
        else:
            record = line.split(':')[1].strip().split(' ')
            record = [int(x) for x in record if x != ""]
    for i in range(len(time)):
        t = time[i]
        r = record[i]
        hs = int(math.ceil((t - math.sqrt(t*t - 4*r)) / 2))
        hf = int(math.floor((t + math.sqrt(t*t - 4*r)) / 2))
        hold_start = hs if -1*(hs*hs - hs*t + r) > 0 else hs + 1
        hold_finish = hf if -1*(hf*hf - hf*t + r) > 0 else hf - 1
        total *= (hold_finish - hold_start) + 1
    print('Part 1:', total)


# Part 2
with open('input6.txt') as openfileobject:
    time = []
    record =[]
    total = 0
    for line in openfileobject:
        if line.startswith('Time:'):
            time = line.split(':')[1].strip().split(' ')
            time = [x for x in time if x != ""]
        else:
            record = line.split(':')[1].strip().split(' ')
            record = [x for x in record if x != ""]
    t = int(''.join(time))
    r = int(''.join(record))
    hs = int(math.ceil((t - math.sqrt(t*t - 4*r)) / 2))
    hf = int(math.floor((t + math.sqrt(t*t - 4*r)) / 2))
    hold_start = hs if -1*(hs*hs - hs*t + r) > 0 else hs + 1
    hold_finish = hf if -1*(hf*hf - hf*t + r) > 0 else hf - 1
    total += (hold_finish - hold_start) + 1
    print('Part 2:', total)
