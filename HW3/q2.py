def fun(n,cnt):
    if n<=1:
        cnt+=1
        print(cnt)
    else:
        for _ in range(1,n):
            cnt= fun(int(n/2),cnt)
    return cnt

# print(fun(16,0))    

for _ in range(1,4):
    print("fok")