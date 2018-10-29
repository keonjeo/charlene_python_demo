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

import random

card_list = [
    ('红桃', 'A'),
    ('红桃', '2'),
    ('红桃', '3'),
    ('红桃', '4'),
    ('红桃', '5'),
    ('红桃', '6'),
    ('红桃', '7'),
    ('红桃', '8'),
    ('红桃', '9'),
    ('红桃', '10'),
    ('红桃', 'J'),
    ('红桃', 'Q'),
    ('红桃', 'K'),
    ('方块', 'A'),
    ('方块', '2'),
    ('方块', '3'),
    ('方块', '4'),
    ('方块', '5'),
    ('方块', '6'),
    ('方块', '7'),
    ('方块', '8'),
    ('方块', '9'),
    ('方块', '10'),
    ('方块', 'J'),
    ('方块', 'Q'),
    ('方块', 'K'),
    ('黑桃', 'A'),
    ('黑桃', '2'),
    ('黑桃', '3'),
    ('黑桃', '4'),
    ('黑桃', '5'),
    ('黑桃', '6'),
    ('黑桃', '7'),
    ('黑桃', '8'),
    ('黑桃', '9'),
    ('黑桃', '10'),
    ('黑桃', 'J'),
    ('黑桃', 'Q'),
    ('黑桃', 'K'),
    ('梅花', 'A'),
    ('梅花', '2'),
    ('梅花', '3'),
    ('梅花', '4'),
    ('梅花', '5'),
    ('梅花', '6'),
    ('梅花', '7'),
    ('梅花', '8'),
    ('梅花', '9'),
    ('梅花', '10'),
    ('梅花', 'J'),
    ('梅花', 'Q'),
    ('梅花', 'K')
]


def calculate(card_list):
    sum = 0
    for card in card_list:
        # print(card)
        # print('+++++++++++++++++++++++++++++++++')
        # print(card[1])
        # print('+++++++++++++++++++++++++++++++++')
        card_number = transfer(card[1])
        sum += card_number
    return sum


def transfer(poke):
    # print('+++++++++++++++++++++++++++++++++')
    # print(poke)
    # print('+++++++++++++++++++++++++++++++++')
    if poke == 'A':
        return 1
    elif poke == 'J':
        return 0.5
    elif poke == 'Q':
        return 0.5
    elif poke == 'K':
        return 0.5
    else:
        return int(poke)


def player(name, chip, card_list, bets):
    number_of_cards = calculate(card_list)
    want_more = needs_more_cards(number_of_cards)
    print("========================================")
    print("名字: ", name)
    print("筹码: ", chip)
    print("要牌标识符: ", want_more)
    print("牌列表: ", card_list)
    print("牌点数: ", number_of_cards)
    print("下注数: ", bets)
    print("========================================")


def needs_more_cards(number_of_cards):
    want_more = False
    if number_of_cards < 10:
        want_more = True
    return want_more


random_cards = random.sample(card_list, 52)

player1_cards = random_cards[0:2]
player2_cards = random_cards[2:4]
player3_cards = random_cards[4:6]
player4_cards = random_cards[6:8]

player1 = player('张三', 100, player1_cards, 18)
player2 = player('李四', 100, player2_cards, 13)
player3 = player('小明', 100, player3_cards, 15)
player4 = player('小红', 100, player4_cards, 10)
