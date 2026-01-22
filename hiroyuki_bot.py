#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ひろゆき風チャットボット
Hiroyuki-style chatbot that mimics his personality and speaking patterns
"""

import re
import random


class HiroyukiBot:
    """ひろゆきの性格、話し方、考え方を模倣するチャットボット"""
    
    def __init__(self):
        # 基本的な応答パターン
        self.response_patterns = [
            # 挨拶系
            (r'こんにちは|こんにちわ', ['あ、こんにちはー', 'はい、こんにちはー']),
            (r'おはよう', ['あ、おはようございますー', 'おはようございますー']),
            (r'こんばんは|こんばんわ', ['あ、こんばんはー', 'こんばんはー']),
            
            # 感謝系
            (r'いつも見ています|いつも見てます|いつも見てる', ['あ、ありがとうございますー', 'ありがとうございますー']),
            (r'ありがとう|ありがと|感謝', ['いえいえ', 'いえいえ、どういたしまして']),
            
            # 謝罪系
            (r'ごめん|すみません|申し訳', ['いえ、次を考えましょう', 'いえいえ、気にしないでください']),
            
            # 質問・意見系
            (r'どう思いますか|どう思う', ['んー、それってあなたの感想ですよね？', 'それはですね、論理的に考えると...']),
            (r'なぜ|どうして|理由', ['それって何か根拠あるんですか？', 'んー、ちょっとそれは違う気がしますけどね']),
            (r'本当|ほんと', ['それ、本当ですか？ソースは？', 'うーん、僕はそうは思わないですけどね']),
            
            # 賛同・反論系
            (r'そうですね|その通り|同意', ['まあ、そうですよね', 'ですよね']),
            (r'違う|おかしい|間違', ['んー、でもそれってあなたの感想ですよね？', 'いや、論理的に考えてみてください']),
        ]
        
        # ひろゆき特有の口癖・フレーズ
        self.hiroyuki_phrases = [
            'それってあなたの感想ですよね？',
            'なんかデータとかあるんですか？',
            'それ、あなたが勝手に思ってるだけですよね',
            'うーん、それは違うと思いますよ',
            'ちょっと論理的に考えてみましょうよ',
            'んー、でもそれって嘘ですよね',
            'それって何か根拠あるんですか？',
        ]
    
    def get_response(self, user_input):
        """ユーザーの入力に対して、ひろゆき風の応答を返す"""
        user_input = user_input.strip()
        
        # 空の入力には応答しない
        if not user_input:
            return 'んー、何か言いたいことがあるんですか？'
        
        # パターンマッチングで応答を探す
        for pattern, responses in self.response_patterns:
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # パターンにマッチしない場合は、ひろゆき特有のフレーズを返す
        return self._get_default_response(user_input)
    
    def _get_default_response(self, user_input):
        """デフォルトの応答を生成"""
        responses = [
            'んー、' + random.choice(self.hiroyuki_phrases),
            'あー、' + random.choice(self.hiroyuki_phrases),
            random.choice(self.hiroyuki_phrases),
        ]
        
        # 質問形式の場合 (?, ?, か at the end, etc.)
        if re.search(r'[？?]|か$', user_input):
            return random.choice([
                'んー、それは難しい質問ですねー',
                'それってあなたの感想ですよね？',
                'なんかデータとかあるんですか？',
            ])
        
        return random.choice(responses)


def main():
    """対話型インターフェース"""
    bot = HiroyukiBot()
    
    print('=' * 50)
    print('ひろゆき風チャットボット')
    print('Hiroyuki-style Chatbot')
    print('=' * 50)
    print('終了するには "exit" または "quit" と入力してください')
    print()
    
    while True:
        try:
            user_input = input('あなた: ').strip()
            
            if user_input.lower() in ['exit', 'quit', '終了', 'bye']:
                print('ひろゆき: じゃあ、またー')
                break
            
            if not user_input:
                continue
            
            response = bot.get_response(user_input)
            print(f'ひろゆき: {response}')
            print()
            
        except (KeyboardInterrupt, EOFError):
            print('\nひろゆき: じゃあ、またー')
            break


if __name__ == '__main__':
    main()
