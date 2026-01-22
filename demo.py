#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ひろゆき風チャットボットのデモ
Demo script for Hiroyuki-style chatbot
"""

from hiroyuki_bot import HiroyukiBot


def run_demo():
    """デモンストレーションを実行"""
    bot = HiroyukiBot()
    
    print('=' * 60)
    print('ひろゆき風チャットボット デモ')
    print('Hiroyuki-style Chatbot Demo')
    print('=' * 60)
    print()
    
    # デモ用の対話シナリオ
    demo_conversations = [
        'こんにちは',
        'いつも見ています',
        'ありがとう',
        'ごめん',
        'すみません',
        'これってどう思いますか？',
        'なぜそうなるんですか？',
        'おはよう',
        'こんばんは',
    ]
    
    for user_input in demo_conversations:
        response = bot.get_response(user_input)
        print(f'あなた: {user_input}')
        print(f'ひろゆき: {response}')
        print()
    
    print('=' * 60)
    print('デモ終了')
    print('Demo completed')
    print('=' * 60)


if __name__ == '__main__':
    run_demo()
