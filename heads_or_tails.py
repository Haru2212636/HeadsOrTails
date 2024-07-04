import random

def coin_toss():
    return random.choice(["表", "裏"])

name = input("あなたの名前は何ですか？\n> ")
print(f"こんにちは、{name}さん！")

print("コインを投げます...")
results = [coin_toss() for _ in range(3)]

for i, result in enumerate(results, start=1):
    print(f"ラウンド {i}: {result}")

heads_count = results.count("表")
tails_count = results.count("裏")

print(f"表: {heads_count}, 裏: {tails_count}")


import random

def coin_toss():
    return random.choice(["表", "裏"])

print("コインを投げます...")
results = [coin_toss() for _ in range(3)]

for i, result in enumerate(results, start=1):
    print(f"ラウンド {i}: {result}")

heads_count = results.count("表")
tails_count = results.count("裏")

print(f"表: {heads_count}, 裏: {tails_count}")
