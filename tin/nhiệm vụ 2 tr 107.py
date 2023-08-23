n = int(input("Mời bạn nhập số tự nhiên: "))
c = 0
for i in range(1,n):
   if n%i == 0:
        print("Những số ",n,"chia hết là: ",i)
        c=c+1
print("Tổng số các ước là: ",c)