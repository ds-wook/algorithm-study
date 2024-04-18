N = 4
houses = [5,1,7,9]

N = int(input())
houses = list(map(int, input().split()))

houses.sort()

if N%2==0:
    x1,x2 = houses[(N//2)-1],houses[(N//2)]
    answer1 = sum([abs(x1-i) for i in houses])
    answer2 = sum([abs(x2-i) for i in houses])
    if answer1<=answer2:
        print(x1)
    else:
        print(x2)
    answer = min(answer1, answer2)
else:
    x1 = houses[(N//2)]
    print(x1)
    answer = sum([abs(x1-i) for i in houses])

#print(answer)