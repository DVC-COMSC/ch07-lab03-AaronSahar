numbers = []
for i in range(5):
    numbers.append(int(input()))
average = sum(numbers) / len(numbers)
i=0
while i < len(numbers):
    if numbers[i] <= average:
        numbers.remove(numbers[i])
        i-=1
    i+=1
for i in range(len(numbers)):
    print (numbers[i], end=' ')