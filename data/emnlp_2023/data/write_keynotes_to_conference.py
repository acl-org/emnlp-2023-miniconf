import json

# 读取plenaries.json文件
with open('data/emnlp_2023/data/plenaries.json', 'r') as f:
    plenaries_data = json.load(f)

# 读取conference.json文件
with open('data/emnlp_2023/data/conference.json', 'r') as f:
    conference_data = json.load(f)

# 替换conference.json中的plenaries数据
conference_data['plenaries'] = plenaries_data

# 将更新后的数据写入conference.json文件
with open('data/emnlp_2023/data/conference.json', 'w') as f:
    json.dump(conference_data, f, indent=4)

print("数据已成功替换到conference.json文件的plenaries字段。")