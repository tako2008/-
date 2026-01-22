#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ひろゆき風チャットボットのテスト
Tests for Hiroyuki-style chatbot
"""

from hiroyuki_bot import HiroyukiBot


def test_basic_greetings():
    """基本的な挨拶のテスト"""
    bot = HiroyukiBot()
    
    # こんにちは
    response = bot.get_response('こんにちは')
    assert 'こんにちは' in response, f"Expected greeting response, got: {response}"
    print('✓ "こんにちは" test passed')
    
    # おはよう
    response = bot.get_response('おはよう')
    assert 'おはよう' in response, f"Expected morning greeting, got: {response}"
    print('✓ "おはよう" test passed')


def test_gratitude_responses():
    """感謝への応答のテスト"""
    bot = HiroyukiBot()
    
    # いつも見ています
    response = bot.get_response('いつも見ています')
    assert 'ありがとうございます' in response, f"Expected thanks response, got: {response}"
    print('✓ "いつも見ています" test passed')
    
    # ありがとう
    response = bot.get_response('ありがとう')
    assert 'いえいえ' in response, f"Expected humble response, got: {response}"
    print('✓ "ありがとう" test passed')


def test_apology_responses():
    """謝罪への応答のテスト"""
    bot = HiroyukiBot()
    
    # ごめん
    response = bot.get_response('ごめん')
    assert '次を考えましょう' in response or 'いえいえ' in response, f"Expected apology response, got: {response}"
    print('✓ "ごめん" test passed')
    
    # すみません
    response = bot.get_response('すみません')
    assert 'いえ' in response, f"Expected apology response, got: {response}"
    print('✓ "すみません" test passed')


def test_hiroyuki_personality():
    """ひろゆき特有の応答のテスト"""
    bot = HiroyukiBot()
    
    # 質問形式
    response = bot.get_response('これってどう思いますか？')
    assert response is not None and len(response) > 0
    print('✓ Question response test passed')
    
    # デフォルト応答
    response = bot.get_response('適当な文章')
    assert response is not None and len(response) > 0
    print('✓ Default response test passed')


def run_all_tests():
    """全てのテストを実行"""
    print('=' * 60)
    print('ひろゆき風チャットボット テスト実行中...')
    print('Running Hiroyuki Bot Tests...')
    print('=' * 60)
    
    try:
        test_basic_greetings()
        test_gratitude_responses()
        test_apology_responses()
        test_hiroyuki_personality()
        
        print('=' * 60)
        print('✓ All tests passed!')
        print('全てのテストが成功しました！')
        print('=' * 60)
        return True
        
    except AssertionError as e:
        print(f'\n✗ Test failed: {e}')
        return False


if __name__ == '__main__':
    success = run_all_tests()
    exit(0 if success else 1)
