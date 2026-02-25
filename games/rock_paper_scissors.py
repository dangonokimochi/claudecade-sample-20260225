"""Rock Paper Scissors - じゃんけん"""

import random


CHOICES = ["グー", "チョキ", "パー"]
EMOJI   = {"グー": "✊", "チョキ": "✌️", "パー": "✋"}

# wins_against[x] = x が勝てる手
WINS_AGAINST = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}


def play():
    print("\n" + "-" * 40)
    print("  ✊✌️✋  じゃんけん  Rock Paper Scissors")
    print("-" * 40)
    print("3 回勝負！\n")

    wins, losses, draws = 0, 0, 0

    for round_num in range(1, 4):
        print(f"--- Round {round_num} ---")
        player = _get_player_choice()
        computer = random.choice(CHOICES)

        print(f"  あなた  : {EMOJI[player]}  {player}")
        print(f"  コンピュータ: {EMOJI[computer]}  {computer}")

        result = _judge(player, computer)
        if result == "win":
            print("  🎉 あなたの勝ち！\n")
            wins += 1
        elif result == "lose":
            print("  😢 コンピュータの勝ち。\n")
            losses += 1
        else:
            print("  🤝 引き分け。\n")
            draws += 1

    print("=" * 40)
    print(f"  結果: {wins}勝 {losses}敗 {draws}分け")
    if wins > losses:
        print("  🏆 あなたの勝利！おめでとう！")
    elif losses > wins:
        print("  💀 コンピュータの勝利。またチャレンジしてね！")
    else:
        print("  🤝 引き分け！いい勝負でした！")
    print()


def _get_player_choice():
    print("  [1] グー  [2] チョキ  [3] パー")
    while True:
        choice = input("  選択: ").strip()
        if choice in ("1", "2", "3"):
            return CHOICES[int(choice) - 1]
        print("  1〜3 で入力してください。")


def _judge(player, computer):
    if player == computer:
        return "draw"
    if WINS_AGAINST[player] == computer:
        return "win"
    return "lose"
