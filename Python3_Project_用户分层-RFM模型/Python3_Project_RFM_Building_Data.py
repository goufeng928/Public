# Creat By GF 2023-07-15

# Python3_Project_RFM_Building_Data.py

# ----------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# ----------------------------------------------------------------------------------------------------
# 构建数据。

# 1. 构建数据 : 时间字段。

# 1.1 时间。
time_range = pd.date_range(start="1/1/2019", end="31/12/2021")

# Output:
#
#>>>time_range
#DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
#               '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08',
#               '2019-01-09', '2019-01-10',
#               ...
#               '2021-12-22', '2021-12-23', '2021-12-24', '2021-12-25',
#               '2021-12-26', '2021-12-27', '2021-12-28', '2021-12-29',
#               '2021-12-30', '2021-12-31'],
#              dtype='datetime64[ns]', length=1096, freq='D')
#
#>>>len(time_range)
#1096

# 2. 构建数据 : 水果和用户。

# 2.1 购买水果。
fruits = ["香蕉", "苹果", "葡萄", "橙子", "哈密瓜", "芭乐", "梨", "桃子"]
fruits_list = np.random.choice(fruits, size=len(time_range), replace=True)

# Output:
#
#>>>fruits_list
#array(['橙子', '桃子', '芭乐', ..., '梨', '葡萄', '桃子'], dtype='<U3')

# 2.2 客户。
names = ["Mike", "Jhon", "Tom", "Xiaoming", "Jimmy", "Lym", "Michk"]
names_list = np.random.choice(names, size=len(time_range), replace=True)

# Output:
#
#>>>names_list
#array(['Jhon', 'Xiaoming', 'Tom', ..., 'Tom', 'Michk', 'Xiaoming'],
#      dtype='<U8')

# 3. 生成订单数据。
order = pd.DataFrame({"time":time_range,  # -> 下单时间。
                      "fruit":fruits_list, # -> 水果名称。
                      "name":names_list,   # -> 顾客名。
                      "kilogram":np.random.choice(list(range(50,100)), size=len(time_range),replace=True)} # -> 购买量。
                     )

# Output:
#
#>>>order
#        time        fruit name     kilogram
#0       2019-01-01  橙子  Jhon     93
#1       2019-01-02  桃子  Xiaoming 93
#2       2019-01-03  芭乐  Tom      69
#3       2019-01-04  香蕉  Jimmy    87
#4       2019-01-05  桃子  Tom      68
#...     ...         ...   ...      ...
#1091    2021-12-27  葡萄  Lym      74
#1092    2021-12-28  葡萄  Tom      51
#1093    2021-12-29  梨    Tom      78
#1094    2021-12-30  葡萄  Michk    66
#1095    2021-12-31  桃子  Xiaoming 76
#1096 rows × 4 columns

# 4. 生成水果的信息数据。
infortmation = pd.DataFrame({"fruit":fruits,
                             "price":[3.8, 8.9, 12.8, 6.8, 15.8, 4.9, 5.8, 7],
                             "region":["华南","华北","西北","华中","西北","华南","华北","华中"]}
                            )

# Output:
#
#>>>infortmation
#     fruit  price region
#0    香蕉   3.8   华南
#1    苹果   8.9   华北
#2    葡萄   12.8  西北
#3    橙子   6.8   华中
#4    哈密瓜 15.8  西北
#5    芭乐   4.9   华南
#6    梨     5.8   华北
#7    桃子   7.0   华中

# 5. 数据合并。
# 将订单信息和水果信息直接合并成一个完整的 DataFrame，这个 df 就是接下来处理的数据。
df = pd.merge(order, infortmation, how="outer").sort_values("time").reset_index(drop=True)

# Output:
#
#>>>df
#        time        fruit name     kilogram price region
#0       2019-01-01  橙子  Jhon     93       6.8   华中
#1       2019-01-02  桃子  Xiaoming 93       7.0   华中
#2       2019-01-03  芭乐  Tom      69       4.9   华南
#3       2019-01-04  香蕉  Jimmy    87       3.8   华南
#4       2019-01-05  桃子  Tom      68       7.0   华中
#...     ...         ...   ...      ...      ...   ...
#1091    2021-12-27  葡萄  Lym      74       12.8  西北
#1092    2021-12-28  葡萄  Tom      51       12.8  西北
#1093    2021-12-29  梨    Tom      78       5.8   华北
#1094    2021-12-30  葡萄  Michk    66       12.8  西北
#1095    2021-12-31  桃子  Xiaoming 76       7.0   华中
#1096 rows × 6 columns

# 6. 生成新的字段 : 订单金额。
df["amount"] = df["kilogram"] * df["price"]

# Output:
#
#>>>df.head()
#     time       fruit name     kilogram price region amount
#0    2019-01-01 橙子  Jhon     93       6.8   华中   632.4
#1    2019-01-02 桃子  Xiaoming 93       7.0   华中   651.0
#2    2019-01-03 芭乐  Tom      69       4.9   华南   338.1
#3    2019-01-04 香蕉  Jimmy    87       3.8   华南   330.6
#4    2019-01-05 桃子  Tom      68       7.0   华中   476.0

# 数据类型。
#
#>>>df.dtypes
#time        datetime64[ns]
#fruit               object
#name                object
#kilogram             int32
#price              float64
#region              object
#amount             float64
#dtype: object

# ----------------------------------------------------------------------------------------------------

# 到这里你可以学到：

#     * 如何生成时间相关的数据。

#     * 如何从列表（可迭代对象）中生成随机数据。

#     * Pandas 的 DataFrame 自行创建，包含生成新字段。

#     * Pandas 数据合并。

# ----------------------------------------------------------------------------------------------------
# EOF
