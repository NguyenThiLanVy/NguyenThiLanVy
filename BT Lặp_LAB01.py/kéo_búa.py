# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:33:28 2024

@author: USER
"""

import random

# Khởi tạo số lượng người chơi ngẫu nhiên từ 8 đến 20
soluong= random.randint(8, 20)
choices = ['Kéo', 'Búa', 'Bao']

# Tạo danh sách người chơi
players = [{'name': f"Người chơi {i + 1}", 'choice': None} for i in range(soluong)]

# Máy cũng chọn ngẫu nhiên
may = random.choice(choices)
print(f"Máy chọn: {may}\n")

# Mỗi người chơi chọn ngẫu nhiên và xác định kết quả
for player in players:
    player['choice'] = random.choice(choices)
    
    # Xác định kết quả
    if player['choice'] == may:
        result = "Hòa"
    elif (player['choice'] == 'Kéo' and may == 'Bao') or \
         (player['choice'] == 'Búa' and may == 'Kéo') or \
         (player['choice'] == 'Bao' and may == 'Búa'):
        result = "Thắng"
    else:
        result = "Thua"
    
    print(f"{player['name']} chọn {player['choice']} - {result}")