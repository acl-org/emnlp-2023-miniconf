#!/bin/bash

python data/emnlp_2023/data/generate_booklet_data_json.py &&
python data/emnlp_2023/data/write_event_to_booklet.py &&
python data/emnlp_2023/data/generate_workshops_yaml.py &&
python emnlp_miniconf/import_emnlp2023.py &&
python data/emnlp_2023/data/generate_BoF_display.py &&
python data/emnlp_2023/data/write_BoF_display_to_conference.py &&
python data/emnlp_2023/data/generate_break_display.py &&
python data/emnlp_2023/data/write_break_display_to_conference.py &&
python data/emnlp_2023/data/generate_coffee_break_json.py &&
python data/emnlp_2023/data/write_break_to_conference.py &&
python data/emnlp_2023/data/write_social_event_display_to_confenence.py