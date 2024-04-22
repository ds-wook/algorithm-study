def solution(words, queries):
    
    answer = []
#     for i in range(len(queries)):        
#         cnt=0
#         start=queries[i].index("?")
    
#         for j in range(start+1, len(queries[i])):
#             if queries[i][j] != 'j':
#                 print(j, "@@@")
#                 break
            
#         # start~j 까지 ? 존재
#         if start==0:
#             for word in words:
#                 if word[j:]==queries[i][j:]:
#                     cnt+=1
#         else:
#             for word in words:
#                 if word[:start]==queries[i][:start]:
#                     cnt+=1
#         print(cnt)
#         answer.append(cnt)  
        
    for i in range(len(queries)):        
        cnt=0
        # ? 위치 파악
        start=queries[i].index("?")
        leng=queries[i].count("?")
        
        if start==0:
            for word in words:
                # print(word[start+leng:],queries[i][start+leng:])
                if len(word)==len(queries[i]) and word[start+leng:]==queries[i][start+leng:]:
                    cnt+=1
        else:
            for word in words:
                # print(word[:start],queries[i][:start])
                if len(word)==len(queries[i]) and word[:start]==queries[i][:start]:
                    cnt+=1
        answer.append(cnt)
            
    

    return answer