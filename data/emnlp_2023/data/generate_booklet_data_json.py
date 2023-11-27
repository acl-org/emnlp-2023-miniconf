import pandas as pd
import json

# 读取三个Excel表格
df1 = pd.read_excel('input.xlsx', sheet_name='Plenary Schedule')
df2 = pd.read_excel('input.xlsx', sheet_name='Tutorials Schedule')
df3 = pd.read_excel('input.xlsx', sheet_name='Workshop Schedule')

# 创建一个空的字典列表用于存储所有数据
data = []

# 遍历第一个数据帧（Plenary Schedule）
for index, row in df1.iterrows():
    start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    # 处理每一行的数据，并添加到字典列表中
    plenary_data = {
        'id': row['id'],
        'title': row['Title'],
        'desc': row['Desc'],
        'location': row['Room'],
        'start_time': start_time,
        'end_time': end_time,
        'bio':row['bio'],
        'speaker_name':row['Presenter'],
        "institution": row['ins'],
        "image": 'null'  
    }
    data.append(plenary_data)

# 遍历第二个数据帧（Tutorial Schedule）
for index, row in df2.iterrows():
    start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    # 处理每一行的数据，并添加到字典列表中
    tutorial_data = {
        'id':row['Id'],
        'title': row['Title'],
        'desc': row['Desc'],
        'location': row['Room'],
        'start_time': start_time,
        'end_time': end_time,
        'hosts': [author.strip() for author in row['Authors'].split(',')],
        'rocketchat': row['Rocketchat']
    }
    data.append(tutorial_data)

# 遍历第三个数据帧（Workshop Schedule）
for index, row in df3.iterrows():
    start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S')
    end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S')
    # 处理每一行的数据，并添加到字典列表中
    workshop_data = {
        'id':row['Id'],
        'title': row['Title'],
        'desc': row['Desc'],
        'location': row['Room'],
        'start_time': start_time,
        'end_time': end_time,
        'url': row['url'],
        'chair': row['Invited Speakers']
    }
    data.append(workshop_data)

# 构建最终的字典
final_data = {
    "plenaries": data[:len(df1)],
    "tutorials": data[len(df1):len(df1)+len(df2)],
    "workshops": data[len(df1)+len(df2):]
}

# 将所有数据写入JSON文件
with open('booklet_data.json', 'w') as file:
    json.dump(final_data, file, indent=4)