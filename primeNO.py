# python-Assignment-from-letsupgrade
#prime number between 1 to 200
num=200
print("prime numbers between",1,"and",num,"are:")
for i in range(1,num+1):
  if i>1:
    for j in range(2,i):
      if (i%j)==0:
        break
    else:
        print(i)
