N = input()
cards = sorted(map(int, input().split()), reverse=True)

alice_sum = sum(cards[::2])
bob_sum = sum(cards[1::2])
print(alice_sum - bob_sum)
