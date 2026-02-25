"""Word Scramble - 単語並べ替えゲーム"""

import random


WORDS = [
    ("python",   "プログラミング言語"),
    ("github",   "コード共有サービス"),
    ("claude",   "AIアシスタント"),
    ("terminal", "コマンドライン画面"),
    ("keyboard", "文字を入力する道具"),
    ("laptop",   "持ち運べるコンピュータ"),
    ("monitor",  "画面を表示する機器"),
    ("network",  "コンピュータをつなぐ仕組み"),
    ("browser",  "ウェブを見るソフト"),
    ("compiler", "コードを翻訳するツール"),
]


def play():
    print("\n" + "-" * 40)
    print("  🔤  Word Scramble  単語並べ替え")
    print("-" * 40)
    print("バラバラになった英単語を当ててください！")
    print("ヒント付き。5問勝負。\n")

    questions = random.sample(WORDS, min(5, len(WORDS)))
    score = 0

    for i, (word, hint) in enumerate(questions, 1):
        scrambled = _scramble(word)
        print(f"Q{i}. 並べ替えて！ → 「{scrambled}」")
        print(f"   ヒント: {hint}")

        answer = input("   答え: ").strip().lower()
        if answer == word:
            print("   ✅ 正解！\n")
            score += 1
        else:
            print(f"   ❌ 不正解。正解は「{word}」でした。\n")

    print("=" * 40)
    print(f"  スコア: {score} / {len(questions)}")
    if score == len(questions):
        print("  🏆 パーフェクト！すごい！")
    elif score >= len(questions) // 2:
        print("  👍 なかなか良い成績！")
    else:
        print("  📚 もっと練習しよう！")
    print()


def _scramble(word: str) -> str:
    chars = list(word)
    for _ in range(100):  # shuffle until different from original
        random.shuffle(chars)
        if chars != list(word):
            break
    return "".join(chars)
