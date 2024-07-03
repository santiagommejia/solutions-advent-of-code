# Part 1
with open('input1.txt') as openfileobject:
    totalSum = 0
    for line in openfileobject:
        numbers = []
        line = line.strip()
        for char in line:
            if char.isnumeric():
                numbers.append(int(char))
        num = (numbers[0] * 10) + numbers[len(numbers) - 1]
        totalSum += num
    print(totalSum)

# Part 2
with open('input1.txt') as openfileobject:
    totalSum = 0
    nums = ['one','two','three','four','five','six','seven','eight','nine']
    for line in openfileobject:
        numbersStr = ''
        while len(line) > 0:
            char = line[0]
            if char.isnumeric():
                numbersStr += char
            else:
                for idx, numStr in enumerate(nums):
                    if line.startswith(numStr):
                        numbersStr += str(idx + 1)
                        break
            line = line[1:]
        totalSum += int(numbersStr[0] + numbersStr[-1])
    print(totalSum)
