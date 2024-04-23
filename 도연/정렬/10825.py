N = int(input())
student = [list(input().split()) for _ in range(N)]
student.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for a in student:
    print(a[0])