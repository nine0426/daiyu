import jsonpath
import math
import os
import pygame
import random
import requests
import time


# 清屏
def clear():
    os.system('cls')


# 输入清屏
def clear_input(input_str=''):
    clear_str = input(input_str)
    clear()
    return clear_str


# 获取音乐
def get_music_name(platfrom):
    try:
        '''
        搜索歌曲名称
        :return:
        '''
        print('-' * 91)
        name = input('请输入歌曲或歌手名称:')
        url = 'https://music.liuzhijin.cn/'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        param = {
            'input': name,
            'filter': 'name',
            'type': platfrom,
            'page': 1,
        }
        res = requests.post(url=url, data=param, headers=headers)
        json_text = res.json()
        title = jsonpath.jsonpath(json_text, '$..title')
        author = jsonpath.jsonpath(json_text, '$..author')
        url = jsonpath.jsonpath(json_text, '$..url')
        if title:
            songs = list(zip(title, author, url))
            t = 1
            while True:
                try:
                    print('-' * 91)
                    for s in songs:
                        print([t], s[0], s[1])
                        t += 1
                    print('-' * 91)
                    index = int(input('请输入音乐的序号:')) - 1
                    song_download(url[index], title[index], author[index])
                    break
                except:
                    clear()
                    print('输入错误(请输入正确的数字)')
        else:
            print('对不起，暂无搜索结果!')
    except:
        print('下载失败\n[1]请检查网络\n[2]尝试使用其他音乐\n[3]可以将mp3格式的文件重命名为1.mp3\n'
              '复制到C:\ProgramData\DaiyuLinGototheJiaHome')


# 下载音乐
def song_download(url, title, author):
    try:
        print('歌曲:{0}-{1}\n正在下载...'.format(title, author))
        content = requests.get(url).content
        music = os.path.exists(r'C:\ProgramData\DaiyuLinGototheJiaHome\1.mp3')
        if music:
            os.remove(r'C:\ProgramData\DaiyuLinGototheJiaHome\1.mp3')
        with open(file=r'C:\ProgramData\DaiyuLinGototheJiaHome\1.mp3', mode='wb') as f:
            f.write(content)
        new_folder(r'C:\ProgramData\DaiyuLinGototheJiaHome')
        print('下载完毕'.format(title, author))
    except:
        print('下载失败\n[1]请检查网络\n[2]尝试使用其他音乐\n[3]可以将mp3格式的文件重命名为1.mp3\n'
              '复制到C:\ProgramData\DaiyuLinGototheJiaHome')
        time.sleep(3)


# 播放音乐
def play_music():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
        pygame.mixer.music.play(-1)
        return 1
    except:
        print('音乐文件已损坏\n你可能下载了vip音乐')
        time.sleep(1)
        pygame.quit()
        folder = os.path.exists('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
        if folder:
            os.remove('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
        return 0


# 停止音乐
def stop_music():
    pygame.quit()


# 猜数字游戏比大小
def number_right(a, b):
    if a < b:
        print('你输入的数字太小')
        return False
    elif a > b:
        print('你输入的数字太大')
        return False
    else:
        print('猜对了')
        return True


# 格式化update
def show(name, title):
    if math.fabs(name) < 10000:
        print('%s: %d' % (title, name))
    if 10000 <= math.fabs(name) < 100000000:
        print('%s: %d万' % (title, name // 10000))
    if 100000000 <= math.fabs(name):
        print('%s: %d亿' % (title, name // 100000000))


# 挑战函数化
def challenge(int_num, str_num, gw_name, gw_health, gw_attack, gw_defence, gw_combat_effectiveness, plus_gold_coins,
              plus_attack, plus_defence, plus_health, use_invincible_potion, load_data):
    gw_health, gw_defence, gw_attack = int(gw_health), int(gw_defence), int(gw_attack)
    combat_effectiveness = load_data['attack'] * 2 + load_data['defence'] * 3 + load_data['health']
    print('=' * 14)
    print('''第%s关
------
怪物名称:%s''' % (str_num, gw_name))
    show(gw_health, '怪物血量')
    show(gw_attack, '怪物攻击')
    show(gw_defence, '怪物防御')
    print('''是否挑战此关卡
[\033[36menter\033[0m]是
[0]否''')
    print('=' * 14)
    o = clear_input()
    if o == '':
        print('=' * 14)
        print('第%s关' % str_num)
        print('=' * 14)
        if combat_effectiveness > gw_combat_effectiveness:
            # 奖励面板
            print('=' * 14)
            print('你战胜了%s' % gw_name)
            print('获得了%s个金币' % plus_gold_coins)
            if load_data['int_challenge'] == int(int_num):
                load_data['int_challenge'] += 1
            load_data['gold_coins'] += plus_gold_coins
            load_data['attack'] += plus_attack
            load_data['defence'] += plus_defence
            load_data['health'] += plus_health
            print('攻击力得到提升')
            print('生命值得到提升')
            print('防御力得到提升')
            print('=' * 14)
            time.sleep(0.7)
            clear()
        else:
            print('%s打败了你' % gw_name)
            print('=' * 22)
            if load_data['invincible_potion'] > use_invincible_potion:
                print('是否使用%d瓶无敌药水' % use_invincible_potion)
                print('[\033[36menter\033[0m]是 [0]否')
                n = clear_input()
                print('=' * 22)
                if n == '':
                    print('使用成功')
                    load_data['invincible_potion'] -= use_invincible_potion
                    print('剩余无敌药水: %s' % load_data['invincible_potion'])
                    print('=' * 22)
                    time.sleep(0.7)
                    clear()
                    print('=' * 22)
                    print('你战胜了%s' % gw_name)
                    print('获得了%s个金币' % plus_gold_coins)
                    if load_data['int_challenge'] == int(int_num):
                        load_data['int_challenge'] += 1
                    load_data['gold_coins'] += plus_gold_coins
                    load_data['attack'] += plus_attack
                    load_data['defence'] += plus_defence
                    load_data['health'] += plus_health
                    print('攻击力得到提升')
                    print('生命值得到提升')
                    print('防御力得到提升')
                    print('=' * 22)
                    time.sleep(0.7)
                    clear()
                else:
                    back_wait()
            else:
                print('提升属性再来吧')
                print('小提示:挑战之前的关卡可以提升属性')
                print('输入任意返回界面')
                print('=' * 22)
                clear_input()
    else:
        print('=' * 22)
        print('返回关卡界面成功')
        print('=' * 22)

    return load_data


# 返回等待
def back_wait():
    print('-' * 12)
    print('界面返回成功')
    print('-' * 12)
    time.sleep(0.5)
    clear()


# 判定新玩家
def is_new():
    try:
        file_save = open('C:\ProgramData\DaiyuLinGototheJiaHome\save.txt', 'r')
        file_save.close()
        return False
    except:
        return True


# 存档
def save(load_data):
    new_folder('C:\ProgramData\DaiyuLinGototheJiaHome')
    file_save_data = open('C:\ProgramData\DaiyuLinGototheJiaHome\save.txt', 'w')
    file_save_data.write(
        'save1 {} {} {} {} {} {} {} {} {}'.format(load_data['attack'], load_data['defence'], load_data['health'],
                                                  load_data['int_challenge'], load_data['gold_coins'],
                                                  load_data['invincible_potion'], load_data['name'],
                                                  load_data['set_1'], load_data['set_2']))
    file_save_data.close()


# 删除存档
def delete_saveload():
    os.remove('C:\ProgramData\DaiyuLinGototheJiaHome\save.txt')


# 新建文件夹
def new_folder(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return False
    else:
        return True


# 游戏界面
clear()

print('=' * 36)
print('''游戏名:林黛玉进贾府
目前版本:v2.2.7 ''')
print('=' * 36)

f = clear_input('输入任意开始：')

# 管理员面板可循环
while f == '20030426':
    print('-' * 30)
    print('已进入管理员面板')
    print('[\033[36menter\033[0m]使用满级账号进入游戏')
    print('[1]设定值进入游戏')
    print('-' * 30)
    t = clear_input()
    if t == '':
        print('-' * 30)
        print('读取满级存档成功')
        time.sleep(1)
        load_data = {'attack': 3000000, 'defence': 2500000, 'health': 8000000, 'int_challenge': 21,
                     'gold_coins': 100000000, 'invincible_potion': 10000, 'name': '管理员', 'set_1': 1, 'set_2': 0}
        save(load_data)
        print('存档成功')
        print('正在检查本地文件.....')
        print('-' * 30)
        break
    elif t == '1':
        while True:
            try:
                print('-' * 30)
                print('请依次输入')
                print('攻击力、防御力、生命值、金币、关卡、无敌药水、角色名')
                print('-' * 30)
                # 代码转换器
                load_data = {}
                load_data['attack'] = float(input('攻击力：'))
                load_data['defence'] = float(input('防御力：'))
                load_data['health'] = float(input('生命值：'))
                load_data['int_challenge'] = int(input('关卡：'))
                while not 0 < load_data['int_challenge'] < 22:
                    load_data['int_challenge '] = int(input('关卡：'))
                load_data['gold_coins'] = float(input('金币：'))
                load_data['invincible_potion'] = int(input('无敌药水：'))
                load_data['name'] = input('角色名：')
                while ' ' in load_data['name']:
                    print('角色名不能包含空格！')
                    print('请输入你的角色名:')
                    load_data['name'] = clear_input()
                while load_data['name'] == '':
                    print('请输入你的角色名:')
                    load_data['name'] = clear_input()
                load_data['set_1'] = 1
                load_data['set_2'] = 0
                save(load_data)
                print('-' * 30)
                print('已自动覆盖存档')
                print('-' * 30)
                time.sleep(1)
                clear()
                break
            except:
                print('输入有误请重新输入')
        break
    else:
        continue

# 读档
while True:
    # 判断新玩家并新建存档
    if is_new():
        print('-' * 30)
        print('正在新建存档')
        print('请输入你的角色名:')
        print('-' * 30)
        load_data = {'attack': 50, 'defence': 20, 'health': 200, 'int_challenge': 1, 'gold_coins': 0,
                     'invincible_potion': 0, 'set_1': 0, 'set_2': 0, 'name': clear_input()}
        while ' ' in load_data['name']:
            print('角色名不能包含空格！')
            print('请输入你的角色名:')
            load_data['name'] = clear_input()
        while load_data['name'] == '':
            print('请输入你的角色名:')
            load_data['name'] = clear_input()
        save(load_data)
        continue
    # 读档
    else:
        print('-' * 30)
        print('正在读取存档')
        new_folder('C:\ProgramData\DaiyuLinGototheJiaHome')
        file_save = open('C:\ProgramData\DaiyuLinGototheJiaHome\save.txt', 'r')
        content = file_save.readline()[6:].split()
        try:
            attack, defence, health, int_challenge, gold_coins, invincible_potion, name, set_1, set_2 = content
            load_data = {}
            load_data['attack'] = float(attack)
            load_data['defence'] = float(defence)
            load_data['health'] = float(health)
            load_data['int_challenge'] = int(int_challenge)
            load_data['gold_coins'] = float(gold_coins)
            load_data['invincible_potion'] = int(invincible_potion)
            load_data['set_1'] = int(set_1)
            load_data['set_2'] = int(set_2)
            load_data['name'] = name
            file_save.close()
            if load_data['attack'] < 0 or load_data['defence'] < 0 or load_data['health'] < 0 or load_data[
                'int_challenge'] < 1 or load_data['gold_coins'] < 0 or load_data['invincible_potion'] < 0 or not (
                    (load_data['set_1'] == 1 or load_data['set_1'] == 0) and (
                    load_data['set_2'] == 1 or load_data['set_2'] == 0)):
                print('存档文件已损坏')
                time.sleep(1)
                delete_saveload()
                print('原存档已被删除')
                print('-' * 14)
            print('-' * 30)
            time.sleep(0.5)
            clear()
            if set_2 == 1:
                set_2 = play_music()
            break
        except:
            file_save.close()
            print('存档文件已损坏')
            time.sleep(1)
            delete_saveload()
            print('原存档已被删除')
            print('-' * 14)
            time.sleep(2)
            clear()

# 删档退出初始化
exit_game = 'no'
# 暂停音乐初始化
isPause = False

# 游戏面板
while True:
    # 游戏主页面
    if exit_game == '': break
    recharge_char = '[5]\033[34m充值\033[0m\n' if load_data['set_1'] == 1 else ''
    print('\033[33m=============================================\n'
          '-------------------主界面--------------------\n'
          '=============================================\033[0m\n'
          '[1]\033[31m挑战副本\033[0m                           [x]\033[32m退出\n\033[0m'
          '[2]\033[31m状态\033[0m\n'
          '[3]\033[31m商城\033[0m\n'
          '[4]\033[31m益智小游戏\033[0m\n'
          '{}'
          '[\033[36menter\033[0m]保存存档                       [*]\033[32m设置\033[0m\n'
          '\033[33m=============================================\033[0m'.format(recharge_char))
    x = clear_input()
    # 关卡面板循环
    while x == '1':
        int_challenge = load_data['int_challenge']
        now_int_challenge = 20 if int_challenge == 21 else int_challenge
        print('=' * 39)
        print('\033[31m挑战副本\033[0m')
        print('=' * 39)
        print('目前你已解锁最新关卡为: %d/20' % now_int_challenge)
        print('已解锁英雄副本 %d/2' % ((int_challenge - 1) // 10))
        print('请输入你要挑战的关卡数(英雄副本加上前缀#):')
        print('[0]返回首页')
        print('=' * 39)
        p = clear_input()
        # 关卡判定器
        try:
            p = int(p)
            if p > int_challenge or p > 20 or p < 0:
                print('=' * 39)
                print('你输入的关卡未解锁')
                print('=' * 39)
                time.sleep(1)
                clear()
            else:
                # 返回
                if p == 0:
                    break
                # 数字依次为gw_health, gw_attack, gw_defence, gw_combat_effectiveness, plus_gold_coins,
                #         plus_attack, plus_defence, plus_health, use_invincible_potion
                # 第1关
                elif p == 1:
                    load_data = challenge(1, '一', '哥布林小兵', 50, 10, 5, 0, 10, 4, 2, 5, 1, load_data)
                # 第2关
                elif p == 2:
                    load_data = challenge(2, '二', '大哥布林', 200, 50, 20, 370, 20, 20, 20, 100, 1, load_data)
                # 第3关
                elif p == 3:
                    load_data = challenge(3, '三', '哥布林首领', 300, 100, 60, 980, 100, 30, 25, 80, 1, load_data)
                # 第4关
                elif p == 4:
                    load_data = challenge(4, '四', '哥布林司令官', 800, 300, 150, 1350, 500, 30, 25, 80, 1, load_data)
                # 第5关
                elif p == 5:
                    load_data = challenge(5, '五', '蘑菇兵', 500, 300, 150, 1500, 600, 30, 25, 80, 1, load_data)
                # 第6关
                elif p == 6:
                    load_data = challenge(6, '六', '蘑菇队长', 900, 350, 200, 2200, 800, 200, 100, 300, 1, load_data)
                # 第7关
                elif p == 7:
                    load_data = challenge(7, '七', '蘑菇法师', 2500, 600, 400, 5000, 1000, 200, 100, 300, 1, load_data)
                # 第8关
                elif p == 8:
                    load_data = challenge(8, '八', '蘑菇魔王', 4000, 1000, 800, 8500, 2000, 600, 300, 900, 1, load_data)
                # 第9关
                elif p == 9:
                    load_data = challenge(9, '九', '蘑菇首领', 9000, 4700, 1400, 26600, 5000, 1200, 600, 1800, 1, load_data)
                # 第10关
                elif p == 10:
                    load_data = challenge(10, '十', '卢鑫(BOSS)', 20000, 10000, 5000, 45000, 5000, 1200, 600, 1800, 5,
                                          load_data)
                # 第11关
                elif p == 11:
                    load_data = challenge(11, '十一', '野蛮人门卫', 20000, 10000, 5000, 45000, 10000, 1200, 600, 1800, 8,
                                          load_data)
                # 第12关
                elif p == 12:
                    load_data = challenge(12, '十二', '野蛮人小队', 30000, 20000, 7000, 100000, 10000, 1200, 600, 1800, 8,
                                          load_data)
                # 第13关
                elif p == 13:
                    load_data = challenge(13, '十三', '野蛮人精英', 50000, 20000, 10000, 160000, 15000, 3600, 1800, 5400, 10,
                                          load_data)
                # 第14关
                elif p == 14:
                    load_data = challenge(14, '十四', '野蛮人长老', 80000, 30000, 12000, 300000, 20000, 3600, 1800, 5400, 10,
                                          load_data)
                # 第15关
                elif p == 15:
                    load_data = challenge(15, '十五', '野蛮人首领', 120000, 50000, 30000, 420000, 20000, 10000, 8000, 20000,
                                          12, load_data)
                # 第16关
                elif p == 16:
                    load_data = challenge(16, '十六', '隐秘之地', 0, 0, 0, 1500000, 50000, 15000, 10000, 40000, 30, load_data)
                # 第17关
                elif p == 17:
                    load_data = challenge(17, '十七', '孙小圣(水帘洞)', 250000, 80000, 30000, 2200000, 80000, 15000, 10000,
                                          40000, 40, load_data)
                # 第18关
                elif p == 18:
                    load_data = challenge(18, '十八', '孙悟空的保镖(水帘洞)', 300000, 100000, 60000, 3000000, 100000, 50000, 30000,
                                          100000, 75, load_data)
                # 第19关
                elif p == 19:
                    load_data = challenge(19, '十九', '孙悟空(水帘洞)', 400000, 200000, 100000, 4500000, 150000, 50000, 30000,
                                          100000, 125, load_data)
                # 第20关
                elif p == 20:
                    load_data = challenge(20, '二十', '崔智鑫现充爆炸大师\n牛头人忠实粉丝李卓函\n王富顺纯爱战士\n(增强模式)(新代猴王)', 500000, 300000,
                                          150000, 7500000, 200000, 100000, 50000, 180000, 200, load_data)
        except:
            if p == '#1':
                load_data = challenge(1, '一', '卢鑫(增强模式)', 50000, 20000, 10000, 145000, 15000, 2400, 1200, 3600, 10,
                                      load_data)
            elif p == '#2':
                load_data = challenge(2, '二', '崔智鑫现充爆炸大师\n牛头人忠实粉丝李卓函\n王富顺纯爱战士\n(增强模式)(新代猴王)', 23333333, 19198100,
                                      1145140, 14500000, 500000, 150000, 50000, 200000, 250, load_data)
            else:
                print('=' * 24)
                print('输入的关卡不合法或者未解锁')
                print('输入任意继续')
                print('=' * 24)
                time.sleep(0.7)
                clear()
    # 状态面板循环
    while x == '2':
        health = load_data['health']
        name = load_data['name']
        attack = load_data['attack']
        defence = load_data['defence']
        invincible_potion = load_data['invincible_potion']
        print('=' * 21)
        print('\033[31m状态\033[0m')
        print('=' * 21)
        print('角色名: %s' % name)
        show(health, '生命值')
        show(attack, '攻击力')
        show(defence, '防御力')
        print('=' * 21)
        show(load_data['gold_coins'], '金币')
        print('=' * 21)
        print('[1]无敌药水 :%d瓶' % invincible_potion)
        print('[0]返回首页')
        print('=' * 21)
        t = clear_input()
        if t == '1':
            print('=' * 21)
            print('无敌药水: %d瓶' % invincible_potion)
            print('在关卡无法闯过可以使用')
            print('=' * 21)
            t = clear_input('输入任意返回：')
        elif t == '0':
            back_wait()
            break
        else:
            back_wait()
    # 商城面板循环
    while x == '3':
        gold_coins = load_data['gold_coins']
        print('=' * 28)
        print('\033[31m商城\033[0m')
        print('=' * 28)
        show(gold_coins, '金币')
        print('目前商品:')
        print('[1]无敌药水')
        print('[2]飞升药水')
        print('[3]改名卡')
        print('[4]属性加强药水')
        print('')
        print('[0]返回首页')
        print('=' * 28)
        f = clear_input()
        # 返回面板
        if f == '0':
            back_wait()
            break
        # 无敌药水
        elif f == '1':
            print('-' * 21)
            show(gold_coins, '金币')
            print('无敌药水')
            print('需要金币:1500')
            print('目前无敌药水: %d瓶' % load_data['invincible_potion'])
            print('属性:只要你的无敌药水够多没有你通不过的关卡')
            print('是否选择购买')
            print('[\033[36menter\033[0m]是 [0]否')
            print('-' * 21)
            g = clear_input()
            if g == '':
                print('-' * 21)
                print('请输入你要购买的数量:')
                print('-' * 21)
                x = clear_input()
                try:
                    x = int(x)
                    if x > 0:
                        if gold_coins >= 1500 * x:
                            gold_coins -= 1500 * x
                            load_data['invincible_potion'] += x
                            print('-' * 12)
                            print('购买成功')
                            show(gold_coins, '金币')
                            print('目前无敌药水: %d瓶' % load_data['invincible_potion'])
                            print('-' * 14)
                            t = clear_input('输入任意返回界面：')
                            pass
                        else:
                            print('-------------------')
                            print('你的金币不足')
                            show(gold_coins, '金币')
                            print()
                            print('-------------------')
                            t = clear_input('输入任意返回界面：')
                    else:
                        back_wait()
                except:
                    back_wait()
            else:
                back_wait()
        # 飞升药水
        elif f == '2':
            print('=' * 25)
            show(gold_coins, '金币')
            print('飞升药水')
            print('需要金币:5000万')
            print('属性:可以瞬间达到最强状态')
            print('是否选择购买')
            print('[\033[36menter\033[0m]是 [0]否')
            print('=' * 25)
            g = clear_input()
            if g == '':
                if load_data['health'] < 8000000 and load_data['attack'] < 3000000 and load_data['defence'] < 2500000:
                    if gold_coins > 50000000:
                        print('=' * 25)
                        print('购买成功')
                        print('已自动使用成功')
                        gold_coins -= 50000000
                        health = 8000000
                        attack = 3000000
                        defence = 2500000
                        show(gold_coins, '金币')
                        print('目前属性:')
                        print('生命值:800万')
                        print('攻击力:300万')
                        print('防御力:250万')
                        print('=' * 25)
                        clear_input('输入任意返回界面：')
                    else:
                        print('=' * 25)
                        print('你的金币不足')
                        show(gold_coins, '金币')
                        print('=' * 25)
                        clear_input('输入任意返回界面：')
                else:
                    print('=' * 25)
                    print('你的属性太高 这种药剂对你无效')
                    print('=' * 25)
                    time.sleep(1)
                    clear()
            else:
                back_wait()
        # 改名卡
        elif f == '3':
            print('=' * 25)
            show(gold_coins, '金币')
            print('改名卡')
            print('需要金币:1万')
            print('属性:给你一次修改名字的机会')
            print('是否选择购买')
            print('[\033[36menter\033[0m]是 [0]否')
            print('=' * 25)
            g = clear_input()
            if g == '':
                if gold_coins > 10000:
                    print('=' * 18)
                    print('购买成功')
                    show(gold_coins, '金币')
                    print('请输入你的新角色名:')
                    print('=' * 18)
                    load_data['name'] = clear_input()
                    while ' ' in load_data['name']:
                        print('角色名不能包含空格！')
                        print('请输入你的角色名:')
                        load_data['name'] = clear_input()
                    while load_data['name'] == '':
                        print('请输入你的角色名:')
                        load_data['name'] = clear_input()
                    print('=' * 18)
                    print('角色名修改完成')
                    gold_coins -= 10000
                    print('=' * 18)
                    clear_input('输入任意返回界面：')
                elif gold_coins < 10000:
                    print('=' * 22)
                    print('你的金币不足')
                    show(gold_coins, '金币')
                    print('=' * 22)
                    clear_input('输入任意返回界面：')
            else:
                back_wait()
        # 属性加强药水
        elif f == '4':
            print('=' * 33)
            show(gold_coins, '金币')
            print('属性加强药水')
            print('需要金币:2000')
            print('属性:增加生命1000攻击300防御200')
            print('是否选择购买')
            print('[\033[36menter\033[0m]是 [0]否')
            print('=' * 33)
            g = clear_input()
            if g == '':
                print('=' * 17)
                print('请输入你要购买的数量:')
                print('=' * 17)
                x = clear_input()
                try:
                    x = int(x)
                    if x > 0:
                        if gold_coins >= 2000 * x:
                            print('=' * 17)
                            print('购买成功')
                            gold_coins -= 2000 * x
                            load_data['health'] += 1000 * x
                            load_data['attack'] += 300 * x
                            load_data['defence'] += 200 * x
                            show(gold_coins, '金币')
                            print('目前属性:')
                            show(load_data['health'], '生命值')
                            show(load_data['attack'], '攻击力')
                            show(load_data['defence'], '防御力')
                            print('=' * 17)
                            clear_input('输入任意返回界面：')
                        else:
                            print('=' * 17)
                            print('你的购买不合要求')
                            print('=' * 17)
                            clear_input('输入任意返回界面：')
                    else:
                        back_wait()
                except:
                    back_wait()
            else:
                back_wait()
        # 查询无果面板
        else:
            continue
        # 存入字典
        load_data['gold_coins'] = gold_coins
    # 小游戏面板循环
    while x == '4':
        print('=' * 21)
        print('\033[31m益智小游戏\033[0m')
        print('=' * 21)
        print('[1]猜数字游戏')
        print('[2]抽奖小游戏')
        print('[0]返回首页')
        print('=' * 21)
        t = clear_input()
        if t == '1':
            print('=' * 23)
            print('猜数字游戏')
            print('=' * 23)
            print('系统会随机生成1到100的整数')
            print('你可以通过输入来猜测随机的数字')
            print('猜的次数越少获得的奖励越多')
            print('[\033[36menter\033[0m]开始游戏')
            print('[0]返回首页')
            print('=' * 23)
            t = clear_input()
            if t == '':
                b = int(random.randint(1, 100))
                fg = False
                cn = 0
                while not fg:
                    print('=' * 21)
                    print('猜数字游戏')
                    print('[0]退出游戏')
                    print('=' * 21)
                    a = clear_input('你的第%s次输入:' % (cn + 1))
                    if a == '0':
                        cn = 0
                        break
                    elif a == '*':
                        print('=' * 23)
                        print('数字为%d' % b)
                        print('=' * 23)
                        continue
                    try:
                        a = int(a)
                        if not 0 < a <= 100:
                            print('-' * 12)
                            print('输入不合法')
                            back_wait()
                            continue
                        clear()
                        fg = number_right(a, b)
                        cn = cn + 1
                    except:
                        print('-' * 12)
                        print('输入不合法')
                        back_wait()
                        continue
                time.sleep(1)
                clear()
                guess_award = 1 if cn > 8 else 8 - cn
                if not cn == 0:
                    print('=' * 40)
                    print('猜数字游戏')
                    print('=' * 40)
                    print('你猜了%s次得到了答案' % cn)
                    print('你的生命、攻击、防御、金币增加%d%%' % guess_award)
                    if guess_award == 0:
                        print('运气不太好继续加油吧！')
                    print('=' * 40)
                    load_data['attack'] *= (1 + guess_award / 100)
                    load_data['defence'] *= (1 + guess_award / 100)
                    load_data['health'] *= (1 + guess_award / 100)
                    load_data['gold_coins'] *= (1 + guess_award / 100)
                    time.sleep(3)
                    clear()
        elif t == '2':
            print('=' * 23)
            print('抽奖小游戏')
            print('=' * 23)
            print('你可以支付1万金币进行一次抽奖')
            print('1%概率获得80万金币')
            print('9%概率获得1.8万金币')
            print('40%概率获得1000金币')
            print('[\033[36menter\033[0m]开始游戏')
            print('[0]返回首页')
            print('=' * 23)
            t = clear_input()
            if t == '':
                while True:
                    print('=' * 23)
                    print('抽奖小游戏')
                    print('=' * 23)
                    show(load_data['gold_coins'], '金币')
                    print('[0]返回首页')
                    print('=' * 23)
                    a = clear_input('请输入你要抽奖的次数：')
                    fg = False
                    cn = 0
                    if a == '0':
                        clear()
                        cn = 0
                        break
                    try:
                        a = int(a)
                        if load_data['gold_coins'] >= 10000 * a:
                            load_data['gold_coins'] -= (10000 * a)
                            print('正在计算...')
                            for i in range(a):
                                b = int(random.randint(1, 100))
                                if b == 1:
                                    cn += 800000
                                if 1 < b < 11:
                                    cn += 18000
                                if 10 < b < 51:
                                    cn += 1000
                            clear()
                        else:
                            print('=' * 22)
                            print('你的金币不足')
                            show(load_data['gold_coins'], '金币')
                            print('=' * 22)
                            clear_input('输入任意返回界面：')
                            cn = 0
                            break
                    except:
                        print('-' * 12)
                        print('输入不合法')
                        back_wait()
                        continue
                    time.sleep(1)
                    clear()
                    if cn == 0:
                        print('=' * 18)
                        print('抽奖小游戏')
                        print('=' * 18)
                        print('金币不足')
                        back_wait()
                        break
                    print('=' * 40)
                    print('抽奖小游戏')
                    print('=' * 40)
                    print('你总共抽了%d次' % a)
                    show(cn, '总计获得金币')
                    show(cn - a * 10000, '总计收益')
                    print('=' * 40)
                    time.sleep(2.5)
                    load_data['gold_coins'] += cn
                    clear()
        elif t == '0':
            back_wait()
            break
        else:
            back_wait()
    # 充值面板循环
    while x == '5' and load_data['set_1'] == 1:
        print('=' * 41)
        print('\033[34m充值\033[0m')
        print('=' * 41)
        show(load_data['gold_coins'], '金币')
        print('请输入你要充值的金币数：')
        print('[0]返回首页')
        print('=' * 41)
        try:
            recharge = int(clear_input())
            if recharge == 0:
                break
            elif recharge < 0:
                print('=' * 28)
                print('金币输入不合法')
                print('=' * 28)
                clear_input('输入任意返回界面：')
            else:
                print('=' * 28)
                show(recharge, '充值金币')
                load_data['gold_coins'] += recharge
                show(load_data['gold_coins'], '目前金币')
                print('=' * 28)
                clear_input('输入任意返回界面：')
        except:
            print('=' * 28)
            print('金币输入不合法')
            print('=' * 28)
            time.sleep(1)
            clear()
    # 设置面板循环
    while x == '*':
        char_recharge = '禁用' if load_data['set_1'] == 1 else '启用'
        print('=' * 59)
        print('\033[32m设置\033[0m')
        print('=' * 59)
        print(('[1]暂时{}充值功能                  [*]删除存档并退出游戏\n'
               '[2]背景音乐\n'
               '[0]返回首页\n'
               '\n'
               '[\033[36menter\033[0m]保存存档').format(char_recharge))
        print('=' * 59)
        o = clear_input()
        if o == '*':
            print('请确认是否删除现有存档（无法恢复）')
            print('[0]我再想想')
            print('[\033[36menter\033[0m]是的我确认我要删除存档')
            exit_game = clear_input()
            if exit_game == '':
                delete_saveload()
                print('=' * 12)
                print('存档删除成功')
                print('=' * 12)
                time.sleep(1)
                break
        elif o == '1':
            if load_data['set_1'] == 0:
                print('=' * 13)
                print('充值系统已启用')
                print('=' * 13)
                load_data['set_1'] = 1
                time.sleep(0.8)
                clear()
            else:
                print('=' * 12)
                print('充值系统已禁用')
                print('=' * 12)
                load_data['set_1'] = 0
                time.sleep(0.8)
                clear()
        elif o == '2':
            platfromList = ['netease', 'qq', 'kugou', 'kuwo', 'baidu' ]
            platfromListStr = ['网易云音乐(默认)', 'QQ音乐', '酷狗音乐', '酷我音乐', '百度音乐' ]
            platfrom = 'netease'
            platfromStr = platfromListStr[0]
            while True:
                # 设置界面判断
                music = os.path.exists(r'C:\ProgramData\DaiyuLinGototheJiaHome\1.mp3')
                charDownload = '[4]切换背景音乐\n' if music else ''
                charMusic = '暂停' if load_data['set_2'] == 1 else '播放' if music else '下载并播放'
                charDelete = '' if load_data['set_2'] == 1 else '[3]删除背景音乐\n' if music else ''
                print('=' * 25)
                print('设置')
                print('=' * 25)
                print('当前搜索源为:%s' % platfromStr)
                print(('[1]{}背景音乐\n'
                       '[2]切换搜索源\n'
                       '{}'
                       '{}'
                       '[0]返回首页').format(charMusic, charDelete, charDownload))
                print('=' * 25)
                i = clear_input()
                if i == '1':
                    if load_data['set_2'] == 0:
                        music = os.path.exists('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
                        if music:
                            if isPause:
                                pygame.mixer.music.unpause()
                                load_data['set_2'] = 1
                                isPause = False
                            else:
                                print('=' * 14)
                                print('开始播放背景音乐')
                                print('=' * 14)
                                load_data['set_2'] = play_music()
                                time.sleep(0.8)
                                clear()
                        else:
                            get_music_name(platfrom)
                            time.sleep(0.8)
                            clear()
                            load_data['set_2'] = play_music()
                            print('=' * 14)
                            print('开始播放背景音乐')
                            print('=' * 14)
                            time.sleep(0.8)
                            clear()
                    else:
                        print('=' * 12)
                        print('背景音乐已暂停')
                        print('=' * 12)
                        pygame.mixer.music.pause()
                        isPause = True
                        load_data['set_2'] = 0
                        time.sleep(0.8)
                        clear()
                elif i == '2':
                    print('=' * 25)
                    print('当前搜索源为:%s' % platfromStr)
                    print('[1]网易云音乐\n[2]QQ音乐\n[3]酷狗音乐\n[4]酷我音乐\n[5]百度音乐')
                    print('=' * 25)
                    try:
                        musicplat = int(input('输入音乐平台类型:')) - 1
                        platfrom = platfromList[musicplat]
                        platfromStr = platfromListStr[musicplat]
                        clear()
                    except:
                        print('输入错误')
                elif i == '3' and charDelete == '[3]删除背景音乐\n':
                    try:
                        pygame.quit()
                        os.remove('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
                        print('=' * 12)
                        print('删除成功')
                        print('=' * 12)
                        time.sleep(0.8)
                        clear()
                    except:
                        print('=' * 30)
                        print('文件被占用或不存在\n请先关闭音乐重载游戏后重试')
                        print('=' * 30)
                        time.sleep(2)
                        clear()
                elif i == '4' and charDownload == '[4]切换背景音乐\n':
                    try:
                        if load_data['set_2'] == 1:
                            stop_music()
                        print('当前搜索源为:%s' % platfromStr)
                        get_music_name(platfrom)
                        time.sleep(0.8)
                        print('开始播放背景音乐')
                        print('-' * 91)
                        load_data['set_2'] = play_music()
                        clear()
                    except:
                        print('=' * 30)
                        print('文件被占用或不存在\n请先关闭音乐重载游戏后重试')
                        print('=' * 30)
                        time.sleep(1.5)
                        clear()
                else:
                    back_wait()
        elif o == '':
            print('=' * 12)
            print('保存存档成功')
            print('=' * 12)
            save(load_data)
            time.sleep(0.8)
            clear()
        elif o == '0':
            break
        else:
            back_wait()
    # 管理员面板
    while x == '20030426':
        print('-' * 30)
        print('已进入管理员面板')
        print('[\033[36menter\033[0m]使用满级账号进入游戏')
        print('[1]修改设定值')
        print('[0]返回首页')
        print('-' * 30)
        t = clear_input()
        if t == '':
            print('-' * 30)
            print('读取满级存档成功')
            time.sleep(1)
            load_data = {'attack': 3000000, 'defence': 2500000, 'health': 8000000, 'int_challenge': 21,
                         'gold_coins': 100000000, 'invincible_potion': 10000, 'name': '管理员', 'set_1': 1, 'set_2': 0}
            save(load_data)
            print('载入成功')
            print('正在检查本地文件.....')
            print('-' * 30)
            break
        elif t == '1':
            while True:
                try:
                    print('-' * 30)
                    print('请依次输入')
                    print('攻击力、防御力、生命值、金币、关卡、无敌药水、角色名')
                    print('-' * 30)
                    # 代码转换器
                    load_data = {}
                    load_data['attack'] = float(input('攻击力：'))
                    load_data['defence'] = float(input('防御力：'))
                    load_data['health'] = float(input('生命值：'))
                    load_data['int_challenge'] = int(input('关卡：'))
                    while not 0 < load_data['int_challenge'] < 22:
                        load_data['int_challenge '] = int(input('关卡：'))
                    load_data['gold_coins'] = float(input('金币：'))
                    load_data['invincible_potion'] = int(input('无敌药水：'))
                    load_data['name'] = input('角色名：')
                    while ' ' in load_data['name']:
                        print('角色名不能包含空格！')
                        print('请输入你的角色名:')
                        load_data['name'] = clear_input()
                    while load_data['name'] == '':
                        print('请输入你的角色名:')
                        load_data['name'] = clear_input()
                    load_data['set_1'] = 1
                    load_data['set_2'] = 0
                    save(load_data)
                    print('-' * 30)
                    print('已自动覆盖存档')
                    print('-' * 30)
                    time.sleep(1)
                    clear()
                    break
                except:
                    print('输入有误请重新输入')
            break
        elif t == '0':
            break
        else:
            continue
    # 退出面板
    if x == 'x':
        print('=' * 14)
        print('请确定是否\033[32m退出\033[0m')
        print('[\033[36menter\033[0m]是')
        print('[0]否')
        print('=' * 14)
        q = clear_input()
        # 退出确定
        if q == '':
            # 存档
            if load_data['set_2'] == 1:
                stop_music()
            save(load_data)
            print('====================')
            print('存档已自动保存成功')
            print('====================')
            time.sleep(0.5)
            break
        # 退出取消
        else:
            print('=' * 12)
            print('主页面返回成功')
            print('=' * 12)
            time.sleep(0.5)
            clear()
            continue
    # 存档
    elif x == '':
        save(load_data)
        print('=' * 12)
        print('保存存档成功')
        print('=' * 12)
        time.sleep(0.8)
        clear()
        continue
    # 刷新界面
    else:
        continue

# 感谢游玩面板
clear()
print('=============\n'
      '欢迎下次游玩\n'
      '=============')
time.sleep(1)
quit()
