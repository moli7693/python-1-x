import pandas as pd
import numpy as np
arrays = ['a', 'a', 'b', 'b'], [1, 2, 1, 2]
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=pd.MultiIndex.from_arrays(arrays),
                     columns=[['A', 'A', 'B'],
                              ['Green', 'Red', 'Green']])
print(frame)
print("第一种方法")
print((frame.loc["b", "B"]).loc[1, "Green"])
print("第二种方法")
print((frame["B"]["Green"])["b"][1])
print("第三种方法")
print((frame["B"]["Green"]).loc["b", 1])
print("第四种方法")
print((frame.loc["b", "B"]).at[1, "Green"])
print("第五种方法")
print(frame.loc["b", "B"]["Green"][1])
# 分层索引找出8
