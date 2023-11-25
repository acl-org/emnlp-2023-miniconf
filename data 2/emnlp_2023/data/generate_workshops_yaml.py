import pandas as pd
import yaml

# 读取Excel表格
df = pd.read_excel('input.xlsx', sheet_name='Workshop Schedule')

# 创建一个空的字典用于存储数据
data = []

# 遍历Excel表格的每一行
for index, row in df.iterrows():
    shortname = row['Shortname']
    title = row['Title']
    
    # 创建一个字典用于存储每一行的数据
    workshop_data = {
        'anthology_venue_id': shortname,
        'short_name': shortname,
        'name': title
    }
    
    # 将字典添加到数据列表中
    data.append(workshop_data)

# 将数据写入YAML文件
with open('workshops.yaml', 'w') as file:
    yaml.dump(data, file)