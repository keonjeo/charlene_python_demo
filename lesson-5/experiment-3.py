#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""

任务三：模拟第一轮发牌并打印出来

  1.创建4个玩家（1个庄家，3个闲家），具体包含姓名、筹码、要牌标识符、牌列表、牌点数、下注数等信息。

    （默认要牌标识符为True；筹码数为100）

  2.实现3个闲家下注，规定每次下注不超过20个筹码

  3.模拟产生一副除去大小王的扑克牌，并洗牌

  4.实现第一轮发牌，并打印出4个玩家的牌信息


"""

# import random

# card_list = [
#     ('红桃', 'A'),
#     ('红桃', '2'),
#     ('红桃', '3'),
#     ('红桃', '4'),
#     ('红桃', '5'),
#     ('红桃', '6'),
#     ('红桃', '7'),
#     ('红桃', '8'),
#     ('红桃', '9'),
#     ('红桃', '10'),
#     ('红桃', 'J'),
#     ('红桃', 'Q'),
#     ('红桃', 'K'),
#     ('方块', 'A'),
#     ('方块', '2'),
#     ('方块', '3'),
#     ('方块', '4'),
#     ('方块', '5'),
#     ('方块', '6'),
#     ('方块', '7'),
#     ('方块', '8'),
#     ('方块', '9'),
#     ('方块', '10'),
#     ('方块', 'J'),
#     ('方块', 'Q'),
#     ('方块', 'K'),
#     ('黑桃', 'A'),
#     ('黑桃', '2'),
#     ('黑桃', '3'),
#     ('黑桃', '4'),
#     ('黑桃', '5'),
#     ('黑桃', '6'),
#     ('黑桃', '7'),
#     ('黑桃', '8'),
#     ('黑桃', '9'),
#     ('黑桃', '10'),
#     ('黑桃', 'J'),
#     ('黑桃', 'Q'),
#     ('黑桃', 'K'),
#     ('梅花', 'A'),
#     ('梅花', '2'),
#     ('梅花', '3'),
#     ('梅花', '4'),
#     ('梅花', '5'),
#     ('梅花', '6'),
#     ('梅花', '7'),
#     ('梅花', '8'),
#     ('梅花', '9'),
#     ('梅花', '10'),
#     ('梅花', 'J'),
#     ('梅花', 'Q'),
#     ('梅花', 'K')
# ]


# def calculate(card_list):
#     sum = 0
#     for card in card_list:
#         # print(card)
#         # print('+++++++++++++++++++++++++++++++++')
#         # print(card[1])
#         # print('+++++++++++++++++++++++++++++++++')
#         card_number = transfer(card[1])
#         sum += card_number
#     return sum


# def transfer(poke):
#     # print('+++++++++++++++++++++++++++++++++')
#     # print(poke)
#     # print('+++++++++++++++++++++++++++++++++')
#     if poke == 'A':
#         return 1
#     elif poke == 'J':
#         return 0.5
#     elif poke == 'Q':
#         return 0.5
#     elif poke == 'K':
#         return 0.5
#     else:
#         return int(poke)


# def player(name, chip, card_list, bets):
#     number_of_cards = calculate(card_list)
#     want_more = needs_more_cards(number_of_cards)
#     print("========================================")
#     print("名字: ", name)
#     print("筹码: ", chip)
#     print("要牌标识符: ", want_more)
#     print("牌列表: ", card_list)
#     print("牌点数: ", number_of_cards)
#     print("下注数: ", bets)
#     print("========================================")


# def needs_more_cards(number_of_cards):
#     want_more = False
#     if number_of_cards < 10:
#         want_more = True
#     return want_more


# random_cards = random.sample(card_list, 52)

# player1_cards = random_cards[0:2]
# player2_cards = random_cards[2:4]
# player3_cards = random_cards[4:6]
# player4_cards = random_cards[6:8]

# player1 = player('张三', 100, player1_cards, 18)
# player2 = player('李四', 100, player2_cards, 13)
# player3 = player('小明', 100, player3_cards, 15)
# player4 = player('小红', 100, player4_cards, 10)



#!/usr/bin/env python

import random

player1 = []
player1_name = input("请输入庄家的姓名:")
player1.append(player1_name)
player1_money = "100"
player1.append(player1_money)
player1_flag = True
player1.append(player1_flag)
player1_cards = []
player1.append(player1_cards)
player1_pointsum = "0"
player1.append(player1_pointsum)
player1_bet = "0"
player1.append(player1_bet)


player2 = []
player2_name = input("请输入第一个闲家的姓名:")
player2.append(player2_name)
player2_money = "100"
player2.append(player2_money)
player2_flag = True
player2.append(player2_flag)
player2_cards = []
player2.append(player2_cards)
player2_pointsum = "0"
player2.append(player2_pointsum)
player2_bit = "0"
player2.append(player2_bit)


player3 = []
player3_name = input("请输入第二个闲家的姓名:")
player3.append(player3_name)
player3_money = "100"
player3.append(player3_money)
player3_flag = True
player3.append(player3_flag)
player3_cards = []
player3.append(player3_cards)
player3_pointsum = "0"
player3.append(player3_pointsum)
player3_bit = "0"
player3.append(player3_bit)


player4 = []
player4_name = input("请输入第三个闲家的姓名:")
player4.append(player4_name)
player4_money = "100"
player4.append(player4_money)
player4_flag = True
player4.append(player4_flag)
player4_cards = []
player4.append(player4_cards)
player4_pointsum = "0"
player4.append(player4_pointsum)
player4_bit = "0"
player4.append(player4_bit)


print(player1, player2, player3, player4)


player2_bit = input(player2[0] + ":请下注")
if int(player2_bit) > 20 or int(player2_bit) < 1:
    print("请重新下注:")
else:
    print(player2_bit)
player2.append(player2_bit)


player3_bit = input(player3[0] + ":请下注")
if int(player3_bit) > 20 or int(player3_bit) < 1:
    print("请重新下注:")
else:
    print(player3_bit)
player3.append(player3_bit)


player4_bit = input(player3[0] + ":请下注")
if int(player4_bit) > 20 or int(player4_bit) < 1:
    print("请重新下注:")
else:
    print(player4_bit)
player4.append(player4_bit)


print(player1, player2, player3, player4)


count = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "k", "Q"]
color = ["红桃", "黑桃", "梅花", "方块"]
cards = []
for i in count:
    for j in color:
        cards.append(i+j)
print('=========  第一次洗牌  ==========')
print(cards)

random.shuffle(cards)
print('=========  第二次洗牌  ==========')
print(cards)


j = 0
card1 = cards[j]
j = j+1
print(card1)
player1_cards = card1
player1[3].append(player1_cards)

j = 1
card2 = cards[j]
j = j+1
print(card2)
player2_cards = card2
player2[3].append(player2_cards)


j = 2
card3 = cards[j]
j = j+1
print(card3)
player3_cards = card3
player3[3].append(player3_cards)


j = 3
card4 = cards[j]
j = j+1
print(card4)
player4_cards = card4
player4[3].append(player4_cards)

j = j+1
print(player1, player2, player3, player4)


