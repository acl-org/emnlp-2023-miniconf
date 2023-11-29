import pandas as pd
import json

def generate_break_json():
    # 读取Excel文件
    df = pd.read_excel('data/emnlp_2023/data/input.xlsx', sheet_name='Breaks Schedule')

    breaks = {}
    # 遍历每一行数据
    for _, row in df.iterrows():
        start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S') + "+08:00"
        end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S') + "+08:00"
        break_data = {
            'chairs': [],
            'end_time': end_time,
            'id': row['id'],
            'link': None,
            'paper_ids': [],
            'room': None,
            'session': row['Session'],
            'start_time': start_time,
            'track': row['Track'],
            'type': row['Type']
        }
        breaks[row['id']] = break_data

    # 将字典写入JSON文件
    with open('data/emnlp_2023/data/break.json', 'w') as f:
        json.dump(breaks, f, indent=4)

    print("数据已成功生成到break.json文件。")

if __name__ == '__main__':
    generate_break_json()