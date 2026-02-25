"""Number Guess - 数字当てゲーム"""

import random


def play():
    print("\n" + "-" * 40)
    print("  🔢  Number Guess  数字当てゲーム")
    print("-" * 40)
    print("1〜100 の数字を当ててください！")

    level = _choose_level()
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = {"easy": 10, "normal": 7, "hard": 5}[level]

    print(f"\n残り {max_attempts} 回のチャンスがあります。スタート！\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"  予想 (残り {remaining} 回): "))
        except ValueError:
            print("  数字を入力してください。")
            continue

        attempts += 1

        if guess == secret:
            print(f"\n  🎉 正解！ {attempts} 回で当てました！素晴らしい！\n")
            return
        elif guess < secret:
            print("  📈 もっと大きい！")
        else:
            print("  📉 もっと小さい！")

    print(f"\n  😢 残念！正解は {secret} でした。またチャレンジしてね！\n")


def _choose_level():
    print("\n難易度を選んでください:")
    print("  [1] Easy   (10回)")
    print("  [2] Normal (7回)")
    print("  [3] Hard   (5回)")
    while True:
        choice = input("難易度 (1-3): ").strip()
        if choice == "1":
            return "easy"
        if choice == "2":
            return "normal"
        if choice == "3":
            return "hard"
        print("  1〜3 で入力してください。")
