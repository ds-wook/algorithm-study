N = 3
orders = [
    [4, 2, 5, 1, 7],
    [3, 1, 9, 4, 5],
    [9, 8, 1, 2, 3],
    [8, 1, 9, 3, 4],
    [7, 2, 3, 4, 8],
    [1, 9, 2, 5, 7],
    [6, 5, 2, 3, 4],
    [5, 1, 9, 2, 8],
    [2, 9, 3 ,1, 4],
]

N = 3
orders = [
    [4, 2, 5, 1, 7],
    [2, 1, 9, 4, 5],
    [5, 8, 1, 4, 3],
    [1, 2, 9, 3, 4],
    [7, 2, 3, 4, 8],
    [9, 8, 4, 5, 7],
    [6, 5, 2, 3 ,4],
    [8, 4, 9, 2 ,1],
    [3, 9, 2, 1 ,4],
]

# N = int(input())
# orders = []
# for _ in range(N**2):
#     orders.append(list(map(int,input().split())))
    

from collections import defaultdict

def search_seat(graph,favorite_student_numbers):
    global N
    max_value,max_blank = -1,-1
    seat_row,seat_column = None,None
    for row in range(N):
        for column in range(N):
            if graph[row][column]==0: #빈칸인 경우 상하좌우 좋아하는 학생이 있는지 탐색
                favorite_count, blank_count=0,0
                try: #위쪽방향 탐색
                    if row>0:
                        favorite_count+= (1 if graph[row-1][column] in favorite_student_numbers else 0)
                        blank_count+= (1 if graph[row-1][column]==0 else 0)
                except:
                    pass
                try: #아래쪽방향 탐색
                    favorite_count+= (1 if graph[row+1][column] in favorite_student_numbers else 0)
                    blank_count+= (1 if graph[row+1][column]==0 else 0)
                except:
                    pass
                try: #왼쪽방향 탐색
                    if column>0:
                        favorite_count+= (1 if graph[row][column-1] in favorite_student_numbers else 0)
                        blank_count+= (1 if graph[row][column-1]==0 else 0)
                except:
                    pass
                try: #오른쪽방향 탐색
                    favorite_count+= (1 if graph[row][column+1] in favorite_student_numbers else 0)
                    blank_count+= (1 if graph[row][column+1]==0 else 0)
                except:
                    pass
                
                #print(row,column,':',favorite_count, blank_count)
                if max_value < favorite_count: #1번 조건
                    max_value = favorite_count
                    max_blank = blank_count
                    seat_row,seat_column = row,column
                elif max_value==favorite_count and max_blank<blank_count: #1번 조건이 여러개라면 2번조건
                    max_blank = blank_count
                    seat_row,seat_column = row,column
                else: #3번조건. row,column을 작은순부터 탐색하고 같은경우에는 업데이트하지 않으므로 자동 만족
                    pass
                    
    return seat_row,seat_column

graph = [[0]*N for _ in range(N)]
seated_student_numbers = []
favorite_student_numbers_dict = defaultdict(list)
for order in orders:
    student_number, favorite_student_numbers = order[0], order[1:]
    favorite_student_numbers_dict[student_number]=favorite_student_numbers
    seat_row,seat_column = search_seat(graph,favorite_student_numbers)
    graph[seat_row][seat_column]=student_number

#print(favorite_student_numbers_dict)
# for row in graph:
#     print(row)

answer=0
#만족도 조사
for row in range(N):
    for column in range(N):
        count=0
        try: #위쪽 탐색
            if row>0:
                count+=(1 if graph[row-1][column] in favorite_student_numbers_dict[graph[row][column]] else 0)
        except:
            pass
        try: #아래쪽 탐색
            count+=(1 if graph[row+1][column] in favorite_student_numbers_dict[graph[row][column]] else 0)
        except:
            pass
        try: #왼쪽 탐색
            if column>0:
                count+=(1 if graph[row][column-1] in favorite_student_numbers_dict[graph[row][column]] else 0)
        except:
            pass
        try: #오른쪽 탐색
            count+=(1 if graph[row][column+1] in favorite_student_numbers_dict[graph[row][column]] else 0)
        except:
            pass
        #(graph[row][column],':',count)
        if count==0:
            continue
        elif count==1:
            answer+=1
        elif count==2:
            answer+=10
        elif count==3:
            answer+=100
        else:
            answer+=1000
            
print(answer)