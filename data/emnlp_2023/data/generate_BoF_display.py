import pandas as pd
import json

def generate_bof_json():
    # 读取Excel文件
    df = pd.read_excel('data/emnlp_2023/data/input.xlsx', sheet_name='Affinity Groups & BoF')

    bof_display = {}
    # 遍历每一行数据
    for _, row in df.iterrows():
        start_time = row['Date'].strftime('%Y-%m-%dT') + row['Start Time'].strftime('%H:%M:%S') + "+08:00"
        end_time = row['Date'].strftime('%Y-%m-%dT') + row['End Time'].strftime('%H:%M:%S') + "+08:00"
        bof_data = {
            'display_name': row['Session Title'],
            'end_time': end_time,
            'events': {
                'id': {
                    'chairs': [],
                    'end_time': end_time,
                    'id': row['Session ID'],
                    'link': None,
                    'paper_ids': [],
                    'room': row['Room'],
                    'session': 'event_session',
                    'start_time': start_time,
                    'track': row['Track'],
                    'type': 'Socials'
                }
            },
            'id': row['Session ID'],
            'name': row['Session Title'],
            'plenary_events': {},
            'start_time': start_time,
            'tutorial_events': {},
            'type': 'Socials',
            'workshop_events': {}
        }
        bof_display[row['Track']] = bof_data

    # 将字典写入JSON文件
    with open('data/emnlp_2023/data/bof.json', 'w') as f:
        json.dump(bof_display, f, indent=4)

    print("数据已成功生成到bof.json文件。")

if __name__ == '__main__':
    generate_bof_json()