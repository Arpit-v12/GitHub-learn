for i in range(10):
	print('Done')

"""
For algorithm time
"""
import time
n=100
start=time.time()
sum=0
sum_1=0
for i in range(1):
	sum+=i
print(sum)
end=time.time()
print('Time-Taken: ', end-start)

start1=time.time()
sum_1=(n*(n-1)/2)
print(sum_1)
end1=time.time()
print('Time-Taken:',end1-start1)
