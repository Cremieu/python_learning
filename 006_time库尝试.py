import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))
print(time.strptime(time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()),'%Y-%m-%d %H:%M:%S'))