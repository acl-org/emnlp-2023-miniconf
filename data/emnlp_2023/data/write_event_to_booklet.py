import json

# 读取event.json文件
with open('data/emnlp_2023/data/event.json', 'r') as event_file:
    event_data = json.load(event_file)

# 读取booklet_data.json文件
with open('data/emnlp_2023/data/booklet_data.json', 'r') as booklet_file:
    booklet_data = json.load(booklet_file)

# 将event.json数据添加到booklet_data.json的events字段中
if 'social_events' in booklet_data:
    booklet_data['social_events'].update(event_data['social_events'])
else:
    booklet_data['social_events'] = event_data['social_events']

# 将更新后的数据写入booklet_data.json文件
with open('data/emnlp_2023/data/booklet_data.json', 'w') as booklet_file:
    json.dump(booklet_data, booklet_file, indent=4)

print("数据已成功添加到booklet_data.json文件的social_events字段。")