cards=input().split(" ")
shuffles=int(input())

half=len(cards)//2
left_cards=[]
right_cards=[]
shuffled_cards=[]
for j in range(shuffles):
    for i in range(half):
        left_cards.append(cards[i])
    for i in range(half,len(cards)):
        right_cards.append(cards[i])
    for i in range(0,half):
        shuffled_cards.append(left_cards[i])
        shuffled_cards.append(right_cards[i])
    cards=shuffled_cards
    left_cards=[]
    right_cards=[]
    shuffled_cards=[]
print(cards)