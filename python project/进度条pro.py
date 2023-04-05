from dataclasses import replace
import time
scale = 28
print("下载开始".center(scale // 1,"="))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^2.0f}%{}{}".format(c,a,b,dur),end = "")
    time.sleep(0.1)
print("\n"+"下载完成".center(scale // 1,"="))
