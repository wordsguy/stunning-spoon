import time

start_time = time.time()
print("launch time : %s seconds" % (time.time() - start_time))

localtime = time.localtime()
result = time.strftime("current time: %I:%M:%S %p", localtime)
print(result)
