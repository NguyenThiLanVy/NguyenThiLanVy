# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:02:34 2024

@author: USER
"""

import random

def play_game():
    """Chơi trò Kéo-Búa-Bao"""
    while True:
        player_choice = input("Bạn chọn gì? (kéo, búa, bao): ").lower()
        computer_choice = random.choice(["kéo", "búa", "bao"])

        print(f"Bạn chọn: {player_choice}")
        print(f"Máy tính chọn: {computer_choice}")

        if player_choice == computer_choice:
            print("Hòa!")
        elif (player_choice == "kéo" and computer_choice == "bao") or \
             (player_choice == "búa" and computer_choice == "kéo") or \
             (player_choice == "bao" and computer_choice == "búa"):
            print("Bạn thắng!")
        else:
            print("Máy tính thắng!")

        play_again = input("Bạn có muốn chơi tiếp không? (có/không): ").lower()
        if play_again != "có":
            break

if __name__ == "__main__":
    play_game()