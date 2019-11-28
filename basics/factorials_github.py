n=int(input('enter'))
f=1
print('factorial of ',n)
if n<0:
 print('not exit')
elif n==0:
 print('is 1')
else:
 while n>=1:
  f=f*(n)
  n=n-1
 print('is',f)