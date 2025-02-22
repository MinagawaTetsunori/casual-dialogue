import csv

# 略称
# utt...utteranse(発話)


def _load_dialogue_flow(file_name: str) -> dict:
    '''
    casual_dialogue指定の構造を持つtsvファイルを読み込む
    '''
    dialogue_flow: list[list[str]] = []
    with open(file_name, encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        _ = next(reader)
        dialogue_flow = [cols for cols in reader]
    return dialogue_flow


def dialogue(file_name: str):
    '''
    1. bot文とuser選択肢を最初に出力
    2. consolから選択肢を半角数字で入力し、対応した分岐のbot文を出力
    '''
    # col names
    EVENT_ID = 0
    # SPEAKER = 1
    UTT = 2
    BRANCH = 3

    # speaker sections
    BOT_SECTION = 0
    USER_SECTION = 1

    dialogue_flow: list[list[str]] = _load_dialogue_flow(file_name)
    running_event_id: str = '1'

    while True:
        print('-------------------------')
        running_event: list[list[str]] \
            = [ls for ls in dialogue_flow if ls[EVENT_ID] == running_event_id]
        
        print('bot:')
        print(running_event[BOT_SECTION][UTT])
        if running_event[BOT_SECTION][BRANCH] == '-1':
            break
        if running_event[BOT_SECTION][BRANCH] != '0':
            running_event_id = running_event[BOT_SECTION][BRANCH]
            continue

        print('\nuser:')
        for i in range(len(running_event[USER_SECTION:])):
            print(str(i + 1) + '. ' + running_event[USER_SECTION + i][UTT])

        try:
            user_choice = input('\nchoice : ')
            running_event_id \
                = running_event[USER_SECTION + int(user_choice) - 1][BRANCH]
        except:
            print('-------------------------')
            print('※ 選択肢を半角数字で入力してください')
            continue

        # -1のイベントで実行修了
        if running_event_id == '-1':
            break

if __name__ == '__main__':
    print('hello')