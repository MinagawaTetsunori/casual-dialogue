'''
ライブラリインストールなし環境での確認用
'''
import os
import sys
sys.path.append(os.getcwd())
import modules.casual_dialogue as cdial


if __name__ == '__main__':
    FILE_PATH = os.getcwd() + '\\tests\\sample_flow.tsv'
    cdial.dialogue(FILE_PATH)
    