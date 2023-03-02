"""
一个文字游戏
"""

from jsonpath import jsonpath
from math import fabs
from random import randint
from requests import post, get
from time import sleep
from pygame import quit as pygame_quit
from pygame import mixer
import json
import os
import shutil

# 清屏
def clear():
    os.system('cls')


# 输入清屏
def clear_input(input_str='>'):
    clear_str = input(input_str)
    clear()
    return clear_str


# 返回相反值
def opposide(obj):
    if obj:
        return True
    else:
        return False


# 获取音乐
def get_music_name(platfrom):
    try:
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
        res = post(url=url, data=param, headers=headers)
        json_text = res.json()
        title = jsonpath(json_text, '$..title')
        author = jsonpath(json_text, '$..author')
        url = jsonpath(json_text, '$..url')
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
                    print('-' * 91)
                    print('输入错误(请输入正确的数字)')
        else:
            print('对不起，暂无搜索结果!')
    except:
        print('下载失败')


# 下载音乐
def song_download(url, title, author):
    try:
        print('歌曲:{0}-{1}\n正在下载...'.format(title, author))
        content = get(url).content
        music = os.path.exists(r'C:\ProgramData\DaiyuLinGototheJiaHome\music.mp3')
        if load_data['set']['2'] == 1:
            pygame_quit()
        if music:
            os.remove(r'C:\ProgramData\DaiyuLinGototheJiaHome\music.mp3')
        with open(file=r'C:\ProgramData\DaiyuLinGototheJiaHome\music.mp3', mode='wb') as f:
            f.write(content)
        new_folder(r'C:\ProgramData\DaiyuLinGototheJiaHome')
        print('下载完毕'.format(title, author))
    except:
        print('下载失败')
        sleep(1)


# 播放音乐
def play_music():
    try:
        mixer.init()
        mixer.music.load('C:\ProgramData\DaiyuLinGototheJiaHome\\music.mp3')
        mixer.music.play(-1)
        return 1
    except:
        pygame_quit()
        folder = os.path.exists('C:\ProgramData\DaiyuLinGototheJiaHome\\music.mp3')
        if folder:
            os.remove('C:\ProgramData\DaiyuLinGototheJiaHome\\music.mp3')
        return 0


# 猜数字游戏比大小
def number_right(a, b):
    if a < b:
        print('你输入的数字太小')
        return False
    elif a > b:
        print('你输入的数字太大')
        return False
    else:
        return True


# 格式化update
def show(num, title):
    if fabs(num) < 10000:
        print('%s: %d' % (title, num))
    if 10000 <= fabs(num) < 100000000:
        print('%s: %d万' % (title, num // 10000))
    if 100000000 <= fabs(num) < 1000000000000:
        print('%s: %d亿' % (title, num // 100000000))
    if 1000000000000 <= fabs(num) < 10000000000000000:
        print('%s: %d万亿' % (title, num // 1000000000000))
    if 10000000000000000 <= fabs(num):
        print('%s: %d兆' % (title, num // 10000000000000000))


# 挑战函数化
def challenge(int_num, str_num, gw_name, gw_health, gw_attack, gw_defence, gw_combat_effectiveness, plus_gold_coins,
              plus_attack, plus_defence, plus_health, use_invincible_potion, explain=None, treasure=None):
    gw_health, gw_defence, gw_attack = int(gw_health), int(gw_defence), int(gw_attack)
    combat_effectiveness = load_data['attack'] * 2 + load_data['defence'] * 3 + load_data['health']
    if Saodang:
        print('==============\n'
              '第%s关\n'
              '==============\n'
              '怪物名称:%s' % (str_num, gw_name))
        show(gw_health, '怪物血量')
        show(gw_attack, '怪物攻击')
        show(gw_defence, '怪物防御')
        print('==============')
        print('请输入扫荡次数(最多10次)\n'
              '[0]返回')
        print('=' * 14)
        try:
            o = int(clear_input())
            if o > 10 or o < 0:
                print('输入不合法')
                sleep(1.5)
                clear()
            elif o == 0:
                pass
            else:
                print('=' * 14)
                print('扫荡中...')
                sleep(2)
                print('获得了%s个金币' % (plus_gold_coins * o))
                load_data['gold_coins'] += (plus_gold_coins * o)
                load_data['attack'] += (plus_attack * o)
                load_data['defence'] += (plus_defence * o)
                load_data['health'] += (plus_health * o)
                print('攻击力得到提升')
                print('生命值得到提升')
                print('防御力得到提升')
                print('=' * 14)
                clear_input()
        except:
            print('输入不合法')
            sleep(1.5)
            clear()
    else:
        if explain and load_data['int_challenge'] == int(int_num):
            print('=================================')
            print(explain)
            print('=================================')
            clear_input()
        print('==============\n'
              '第%s关\n'
              '==============\n'
              '怪物名称:%s' % (str_num, gw_name))
        show(gw_health, '怪物血量')
        show(gw_attack, '怪物攻击')
        show(gw_defence, '怪物防御')
        print('=' * 14)
        clear_input()
        print('=' * 14)
        print('第%s关' % str_num)
        print('=' * 14)
        if combat_effectiveness > gw_combat_effectiveness:
            # 奖励面板
            load_data['gold_coins'] += plus_gold_coins
            load_data['attack'] += plus_attack
            load_data['defence'] += plus_defence
            load_data['health'] += plus_health
            print('你战胜了%s' % gw_name)
            print('获得了%s个金币' % plus_gold_coins)
            print('攻击力得到提升')
            print('生命值得到提升')
            print('防御力得到提升')
            if load_data['int_challenge'] == int(int_num):
                load_data['int_challenge'] += 1
                if treasure:
                    print('你获得了\033[5;33m稀世珍宝—— %s \033[0m!' % treasure)
                    load_data['treasure'][treasure] = 1
            print('=' * 14)
            clear_input()
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
                    clear_input()
                else:
                    pass
            else:
                print('提升属性再来吧')
                print('小提示:挑战之前的关卡可以提升属性')
                print('=' * 22)
                sleep(2)
                clear()
    return load_data


# 商品函数化
def goods(name, need_gold_coins, load_data, explain='', showsomething='', hp=0, df=0, att=0, potion=0):
    print('=' * 25)
    print(name)
    show(load_data['gold_coins'], '目前金币')
    show(need_gold_coins, '需要金币')
    print(explain)
    print(showsomething)
    print('是否选择购买')
    print('[\033[36menter\033[0m]是 [0]否')
    print('=' * 25)
    g = clear_input()
    if g == '':
        print('-' * 20)
        print('请输入你要购买的数量:')
        print('-' * 20)
        try:
            x = int(clear_input())
            if x > 0:
                if load_data['gold_coins'] >= (need_gold_coins * x):
                    load_data['gold_coins'] -= (need_gold_coins * x)
                    load_data['invincible_potion'] += (x * potion)
                    load_data['health'] += (x * hp)
                    load_data['attack'] += (x * att)
                    load_data['defence'] += (x * df)
                    print('-' * 14)
                    print('购买成功')
                    show(load_data['gold_coins'], '剩余金币')
                    print('-' * 14)
                    clear_input()
                    pass
                else:
                    print('-------------------')
                    print('你的金币不足')
                    show(load_data['gold_coins'], '金币')
                    print()
                    print('-------------------')
                    clear_input()
            else:
                pass
        except:
            pass
    else:
        pass
    return load_data


# 判定新玩家
def is_new():
    try:
        file_save = open('C:\ProgramData\DaiyuLinGototheJiaHome\save.json', 'r')
        file_save.close()
        return False
    except:
        return True


# 存档
def save(load_data):
    new_folder('C:\ProgramData\DaiyuLinGototheJiaHome')
    with open('C:\ProgramData\DaiyuLinGototheJiaHome\save.json', 'w') as file_save_data:
        data = json.dumps(load_data)
        file_save_data.write(data)


# 删除存档文件夹
def delete_saveload():
    shutil.rmtree(r'C:\ProgramData\DaiyuLinGototheJiaHome')


# 新建文件夹
def new_folder(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return False
    else:
        return True


if __name__ == '__main__':

    clear()
    print('====================\n'
          '游戏名:林黛玉进贾府\n'
          '目前版本:v2.2.12\n'
          '====================')

    f = clear_input()

    # 管理员面板
    while f == '20030426':
        print('=============================\n'
              '已进入管理员面板\n'
              '[\033[36menter\033[0m]使用满级账号进入游戏\n'
              '[1]设定值进入游戏\n'
              '[2]从已有存档进入游戏(若无则新建存档)\n'
              '=============================')

        t = clear_input()
        if t == '':
            print('-' * 30)
            load_data = {'attack': 3000000, 'defence': 2500000, 'health': 8000000, 'int_challenge': 21,
                         'gold_coins': 100000000, 'invincible_potion': 10000, 'name': '管理员', 'set': {'1': 1, '2': 0},
                         'treasure': {'艾尔登法环': 1, '照妖镜': 1, '如意金箍棒': 1, '传送法典': 1, '史莱姆雕塑': 1}}
            save(load_data)
            break
        elif t == '1':
            while True:
                try:
                    print('-' * 12)
                    print('  请依次输入')
                    print('-' * 12)
                    load_data = {'attack': float(input('攻击力：')), 'defence': float(input('防御力：')),
                                 'health': float(input('生命值：')),
                                 'int_challenge': 1, 'gold_coins': float(input('金币：')),
                                 'invincible_potion': int(input('无敌药水：')),
                                 'name': input('角色名：'), 'set': {'1': 1, '2': 0}, 'treasure': {}}
                    while load_data['name'] == '':
                        print('请输入你的角色名:')
                        load_data['name'] = clear_input()
                    save(load_data)
                    clear()
                    break
                except:
                    clear()
                    print('输入有误请重新输入')
                    sleep(1)
                    clear()
            break
        elif t == '2':
            break
        else:
            continue

    # 若为新玩家则新建存档
    if is_new():
        print('-' * 30)
        print('正在新建存档')
        print('请输入你的角色名:')
        print('-' * 30)
        load_data = {'attack': 50, 'defence': 20, 'health': 200, 'int_challenge': 1, 'gold_coins': 0,
                     'invincible_potion': 0, 'set': {'1': 0, '2': 0}, 'name': clear_input(), 'treasure': {}}
        while load_data['name'] == '':
            load_data['name'] = clear_input('请输入你的角色名:')
        save(load_data)

    # 读档
    new_folder('C:\ProgramData\DaiyuLinGototheJiaHome')
    with open('C:\ProgramData\DaiyuLinGototheJiaHome\save.json', 'r') as data:
        load_data = json.load(data)

    # 根据存档信息判定是否播放音乐
    if load_data['set']['2'] == 1: load_data['set']['2'] = play_music()
    # 删档退出初始化
    exit_game = 'no'
    # 暂停音乐初始化
    isPause = False
    # 扫荡模式初始化
    Saodang = False
    # 稀世珍宝介绍初始化
    treasure_introduction = {'照妖镜': '据说是那个女人最珍贵的宝物', '艾尔登法环': '显然不如100瓶雷碧',
                             '史莱姆雕塑': '好像叫做利姆露来着...', '传送法典': '顾名思义可以传送', '如意金箍棒': '一个小人物的便携武器'}

    # 游戏面板
    while True:
        # 退出判定
        if exit_game == '':
            break
        recharge_char = '[5]\033[34m充值\033[0m\n' if load_data['set']['1'] == 1 else ''
        save(load_data)

        print('\033[33m=============================================\n'
              '-------------------主界面--------------------\n'
              '=============================================\033[0m\n'
              '[1]\033[31m挑战副本\033[0m                           [x]\033[32m退出\n\033[0m'
              '[2]\033[31m状态\033[0m                               [*]\033[32m设置\033[0m\n'
              '[3]\033[31m商城\033[0m\n'
              '[4]\033[31m益智小游戏\033[0m\n'
              '{}'
              '\033[33m=============================================\033[0m'.format(recharge_char))

        x = clear_input()

        # 关卡面板循环
        while x == '1':
            save(load_data)
            now_int_challenge = 20 if load_data['int_challenge'] == 21 else load_data['int_challenge']
            print('=' * 39)
            print('\033[31m挑战副本\033[0m')
            print('=' * 39)
            print('目前解锁关卡为: %d/20\n'
                  '已解锁英雄副本: %d/2\n'
                  '[1]普通副本\n'
                  '[2]英雄副本\n'
                  '=======================================\n'
                  '[0]返回首页' % (now_int_challenge, (load_data['int_challenge'] - 1) // 10))
            print('=' * 39)
            l = clear_input()
            while l == '1':
                save(load_data)
                now_int_challenge = 20 if load_data['int_challenge'] == 21 else load_data['int_challenge']
                Saodang_Str = '扫荡模式' if Saodang else '普通模式'
                Saodang_Str_Op = '普通模式' if Saodang else '扫荡模式'
                print('=' * 39)
                print('\033[31m挑战副本({})\033[0m'.format(Saodang_Str))
                print('=' * 39)
                print('目前解锁关卡为: {}/20\n'
                      '请输入你要挑战的关卡\n'
                      '=======================================\n'
                      '[+]进入{}\n'
                      '[0]返回'.format(now_int_challenge - int(Saodang), Saodang_Str_Op))
                print('=' * 39)
                # 关卡判定
                p = clear_input()
                try:
                    p = int(p)
                    if p > load_data['int_challenge'] - int(Saodang) or p > 20 or p < 0:
                        print('=' * 39)
                        if Saodang_Str == '扫荡模式' and load_data['int_challenge'] == p:
                            print('还未挑战的关卡不能扫荡')
                        else:
                            print('你输入的关卡未解锁')
                        print('=' * 39)
                        sleep(1)
                        clear()
                    else:
                        # 返回
                        if p == 0:
                            break
                        # 数字依次为gw_health, gw_attack, gw_defence, gw_combat_effectiveness, plus_gold_coins,
                        #         plus_attack, plus_defence, plus_health, use_invincible_potion
                        # 第1关
                        elif p == 1:
                            load_data = challenge(1, '一', '哥布林小兵', 50, 10, 5, 0, 10, 4, 2, 5, 1,
                                                  '这是一片寂静的森林\n前方可以看到哥布林的村落\n哥布林是一种可怕的生物\n我们必须将它们赶尽杀绝\n出发吧\n开始你的旅程')
                        # 第2关
                        elif p == 2:
                            load_data = challenge(2, '二', '哥布林队长', 200, 50, 20, 370, 20, 20, 20, 100, 1,
                                                  '真是一场惊险的战斗\n让我们和队长来一次单挑')
                        # 第3关
                        elif p == 3:
                            load_data = challenge(3, '三', '哥布林首领', 300, 100, 60, 980, 100, 30, 25, 80, 1,
                                                  '他们居然还有首领\n看看我们能获得什么情报')
                        # 第4关
                        elif p == 4:
                            load_data = challenge(4, '四', '哥布林司令官', 800, 300, 150, 1350, 500, 30, 25, 80, 1,
                                                  '我们找到了他们的幕后指挥\n他们有什么秘密？', '史莱姆雕塑')
                        # 第5关
                        elif p == 5:
                            load_data = challenge(5, '五', '蘑菇兵', 500, 300, 150, 1500, 600, 30, 25, 80, 1,
                                                  '经过了与哥布林的激战\n我们向另一个方向出发\n前面有一些奇怪的生物')
                        # 第6关
                        elif p == 6:
                            load_data = challenge(6, '六', '蘑菇队长', 900, 350, 200, 2200, 800, 200, 100, 300, 1,
                                                  '这些怪物的社会体系\n怎么差不多？\n他们也有队长')
                        # 第7关
                        elif p == 7:
                            load_data = challenge(7, '七', '蘑菇法师', 2500, 600, 400, 5000, 1000, 200, 100, 300, 1,
                                                  '前方检测到强大的能量\n估计是他们的战力担当')
                        # 第8关
                        elif p == 8:
                            load_data = challenge(8, '八', '蘑菇魔王', 4000, 1000, 800, 8500, 2000, 600, 300, 900, 1,
                                                  '更强大的法术能量正在靠近')
                        # 第9关
                        elif p == 9:
                            load_data = challenge(9, '九', '蘑菇首领', 9000, 4700, 1400, 26600, 5000, 1200, 600, 1800, 1,
                                                  '首领，呵呵\n对我们来说都是小意思')
                        # 第10关
                        elif p == 10:
                            load_data = challenge(10, '十', '卢鑫(BOSS)', 20000, 10000, 5000, 45000, 5000, 1200, 600, 1800,
                                                  5, '我们有了新的情报\n原来这些怪物的真正统领者是...', '照妖镜')
                        # 第11关
                        elif p == 11:
                            load_data = challenge(11, '十一', '野蛮人门卫', 20000, 10000, 5000, 45000, 10000, 1200, 600, 1800,
                                                  8, '让我们继续前往另一个村落\n这里似乎是一个更大的城市\n说不定我们能在这里发现一些宝贝')
                        # 第12关
                        elif p == 12:
                            load_data = challenge(12, '十二', '野蛮人小队', 30000, 20000, 7000, 100000, 10000, 1200, 600, 1800,
                                                  8, '这个小队似乎有点实力')
                        # 第13关
                        elif p == 13:
                            load_data = challenge(13, '十三', '野蛮人精英', 50000, 20000, 10000, 160000, 15000, 3600, 1800,
                                                  5400,
                                                  10, '他们的精英想和我们来一次精彩的战斗')
                        # 第14关
                        elif p == 14:
                            load_data = challenge(14, '十四', '野蛮人长老', 80000, 30000, 12000, 300000, 20000, 3600, 1800,
                                                  5400,
                                                  10, '我们似乎正在逼近他们的指挥中心')
                        # 第15关
                        elif p == 15:
                            load_data = challenge(15, '十五', '野蛮人首领', 120000, 50000, 30000, 420000, 20000, 10000, 8000,
                                                  20000,
                                                  12, '或许我们要跟首领进行谈判\n他的手上似乎有些好东西', '传送法典')
                        # 第16关
                        elif p == 16:
                            load_data = challenge(16, '十六', '隐秘之地的大门', 0, 0, 0, 1500000, 50000, 15000, 10000, 40000, 30,
                                                  '我们通过上次获得的稀世珍宝————传送法典\n发现了一个新的地方\n但似乎以我们目前的实力很难进入这里')
                        # 第17关
                        elif p == 17:
                            load_data = challenge(17, '十七', '孙小圣(水帘洞)', 250000, 80000, 30000, 2200000, 80000, 15000,
                                                  10000,
                                                  40000, 40,
                                                  '我们终于打开了这扇门\n这是孙悟空的老家————水帘洞\n经过我们的侦查\n孙悟空好像收了个徒弟\n让我们和他较量一番')
                        # 第18关
                        elif p == 18:
                            load_data = challenge(18, '十八', '孙悟空的保镖(水帘洞)', 300000, 100000, 60000, 3000000, 100000,
                                                  50000,
                                                  30000,
                                                  100000, 75, '经过思考\n我们还是决定去找孙悟空谈谈\n说不定还能从他身上顺到什么宝贝\n但有人拦住了我们...')
                        # 第19关
                        elif p == 19:
                            load_data = challenge(19, '十九', '孙悟空(水帘洞)', 400000, 200000, 100000, 4500000, 150000, 50000,
                                                  30000,
                                                  100000, 125, '让我们看看弼马温有什么真本事', '如意金箍棒')
                        # 第20关
                        elif p == 20:
                            load_data = challenge(20, '二十', '\n现充爆炸大师崔智鑫\n牛头人李卓函\n纯爱战士王富顺', 500000, 300000,
                                                  150000, 7500000, 200000, 100000, 50000, 180000, 200,
                                                  '三小只居然也在这里\n还好我们没让他们跑了\n正好试试我们刚获得的金箍棒', '艾尔登法环')
                except:
                    if p == '+':
                        Saodang = opposide(Saodang)
                    elif p == '':
                        pass
                    else:
                        print('=' * 24)
                        print('输入的关卡不合法或者未解锁')
                        print('=' * 24)
                        sleep(0.7)
                        clear()
            while l == '2':
                save(load_data)
                now_int_challenge = 20 if load_data['int_challenge'] == 21 else load_data['int_challenge']
                Saodang_Str = '扫荡模式' if Saodang else '普通模式'
                Saodang_Str_Op = '普通模式' if Saodang else '扫荡模式'
                print('=' * 39)
                print('\033[31m挑战副本({})\033[0m'.format(Saodang_Str))
                print('=' * 39)
                print('已解锁英雄副本: {}/2\n'
                      '请输入你要挑战的关卡\n'
                      '=======================================\n'
                      '[+]进入{}\n'
                      '[0]返回'.format((load_data['int_challenge'] - 1) // 10, Saodang_Str_Op))
                print('=' * 39)
                p = clear_input()
                try:
                    p = int(p)
                    if p > ((load_data['int_challenge'] - 1) // 10) or p > 2 or p < 0:
                        print('=' * 39)
                        print('你输入的关卡未解锁')
                        print('=' * 39)
                        sleep(1)
                        clear()
                    else:
                        if p == 0:
                            break
                        elif p == 1:
                            load_data = challenge(1, '一', '卢鑫', 50000, 20000, 10000, 145000, 15000, 2400, 1200, 3600,
                                                  10)
                        elif p == 2:
                            load_data = challenge(2, '二', '\n现充爆炸大师崔智鑫\n牛头人李卓函\n纯爱战士王富顺', 23333333, 19198100,
                                                  1145140, 14500000, 500000, 150000, 50000, 200000, 250)
                        else:
                            print('=' * 24)
                            print('输入的关卡未解锁')
                            print('=' * 24)
                            sleep(0.7)
                            clear()
                except:
                    if p == '+':
                        Saodang = opposide(Saodang)
                    elif p == '':
                        pass
                    else:
                        print('=' * 24)
                        print('输入的关卡不合法或者未解锁')
                        print('=' * 24)
                        sleep(0.7)
                        clear()
            if l == '0':
                break
            else:
                continue
        # 状态面板循环
        while x == '2':
            print('=' * 21)
            print('\033[31m状态\033[0m')
            print('=' * 21)
            print('角色名: %s' % load_data['name'])
            show(load_data['health'], '生命值')
            show(load_data['attack'], '攻击力')
            show(load_data['defence'], '防御力')
            show(load_data['gold_coins'], '金币')
            print('=' * 21)
            print('[1]无敌药水 :%d瓶' % load_data['invincible_potion'])

            # 稀世珍宝显示读取并建立顺序列表
            count = 2
            treasure_list = [None, None]
            for k, v in load_data['treasure'].items():
                if v == 1:
                    print('[{}]\033[1;33m{}\033[0m'.format(count, k))
                    treasure_list.append(k)
                    count += 1
            print('=' * 21)
            print('[0]返回首页')
            print('=' * 21)
            try:
                t = int(clear_input())
                if t == 0:
                    break
                elif t == 1:
                    print('=' * 21)
                    print('无敌药水: %d瓶' % load_data['invincible_potion'])
                    print('在关卡无法闯过可以使用')
                    print('=' * 21)
                    t = clear_input()
                elif 2 <= t < len(treasure_list):
                    print('=' * 21)
                    print('\033[1;33m稀世珍宝——%s\033[0m' % treasure_list[int(t)])
                    print('%s' % treasure_introduction[treasure_list[int(t)]])
                    print('=' * 21)
                    t = clear_input()
                else:
                    pass
            except:
                pass
        # 商城面板循环
        while x == '3':
            save(load_data)
            print('=' * 28)
            print('\033[31m商城\033[0m')
            print('=' * 28)
            show(load_data['gold_coins'], '金币')
            print('目前商品:')
            print('[1]无敌药水')
            print('[2]飞升药水')
            print('[3]改名卡')
            print('[4]属性加强药水')
            print('=' * 28)
            print('[0]返回首页')
            print('=' * 28)

            f = clear_input()

            # 返回面板
            if f == '0':
                break
            # 无敌药水
            elif f == '1':
                load_data = goods('无敌药水', 1500, load_data, '属性:强行通过无法通过的关卡',
                                  '现有无敌药水: %d瓶' % load_data['invincible_potion'], potion=1)
            # 飞升药水
            elif f == '2':
                print('=' * 25)
                print('飞升药水')
                show(load_data['gold_coins'], '目前金币')
                print('需要金币:5000万')
                print('属性:可以瞬间达到最强状态')
                print('是否选择购买')
                print('[\033[36menter\033[0m]是 [0]否')
                print('=' * 25)
                g = clear_input()
                if g == '':
                    if load_data['health'] < 8000000 and load_data['attack'] < 3000000 \
                            and load_data['defence'] < 2500000:
                        if load_data['gold_coins'] > 50000000:
                            print('=' * 25)
                            print('购买成功')
                            print('已自动使用成功')
                            load_data['gold_coins'] -= 50000000
                            load_data['health'] = 8000000
                            load_data['attack'] = 3000000
                            load_data['defence'] = 2500000
                            show(load_data['gold_coins'], '金币')
                            print('目前属性:')
                            print('生命值:800万')
                            print('攻击力:300万')
                            print('防御力:250万')
                            print('=' * 25)
                            clear_input()
                        else:
                            print('=' * 25)
                            print('你的金币不足')
                            show(load_data['gold_coins'], '金币')
                            print('=' * 25)
                            clear_input()
                    else:
                        print('=' * 25)
                        print('你的属性太高 这种药剂对你无效')
                        print('=' * 25)
                        sleep(1)
                        clear()
                else:
                    pass
            # 改名卡
            elif f == '3':
                print('=' * 25)
                print('改名卡')
                show(load_data['gold_coins'], '目前金币')
                print('需要金币:1万')
                print('属性:给你一次修改名字的机会')
                print('是否选择购买')
                print('[\033[36menter\033[0m]是 [0]否')
                print('=' * 25)
                g = clear_input()
                if g == '':
                    if load_data['gold_coins'] > 10000:
                        print('=' * 18)
                        load_data['gold_coins'] -= 10000
                        show(load_data['gold_coins'], '金币')
                        print('请输入你的新角色名:')
                        print('=' * 18)
                        load_data['name'] = clear_input()
                        while load_data['name'] == '':
                            print('请输入你的角色名:')
                            load_data['name'] = clear_input()
                        print('=' * 18)
                        print('角色名修改完成')
                        print('=' * 18)
                        clear_input()
                    elif load_data['gold_coins'] < 10000:
                        print('=' * 22)
                        print('你的金币不足')
                        show(load_data['gold_coins'], '金币')
                        print('=' * 22)
                        clear_input()
                else:
                    pass
            # 属性加强药水
            elif f == '4':
                load_data = goods('属性加强药水', 2000, load_data, '属性:增加生命1000/攻击300/防御200', hp=1000, att=300, df=200)
            # 查询无果
            else:
                continue
        # 小游戏面板循环
        while x == '4':
            save(load_data)
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
                print('随机生成1-100的整数')
                print('猜的次数越少奖励越多')
                print('[\033[36menter\033[0m]开始游戏')
                print('[0]返回首页')
                print('=' * 23)
                t = clear_input()
                if t == '':
                    b = int(randint(1, 100))
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
                            print('=' * 21)
                            print('数字为%d' % b)
                            continue
                        try:
                            a = int(a)
                            if not 0 < a <= 100:
                                print('=' * 21)
                                print('输入不合法')
                                continue
                            print('=' * 21)
                            fg = number_right(a, b)
                            cn = cn + 1
                        except:
                            print('=' * 21)
                            print('输入不合法')
                            continue
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
                        clear_input()
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
                        save(load_data)
                        print('=' * 23)
                        print('抽奖小游戏')
                        show(10000, '每抽一次需要金币')
                        show(load_data['gold_coins'], '目前金币')
                        show(load_data['gold_coins']/10000, '你可以抽的次数')
                        print('=' * 23)
                        print('[0]返回')
                        print('=' * 23)
                        a = clear_input('请输入你要抽奖的次数(最多1000万)：')
                        cn = 0
                        if a == '0':
                            break
                        try:
                            a = int(a)
                            if load_data['gold_coins'] >= 10000 * a and 0 < a <= 10000000:
                                load_data['gold_coins'] -= (10000 * a)
                                print('正在抽奖...')
                                for i in range(a):
                                    b = int(randint(1, 100))
                                    if b == 1:
                                        cn += 800000
                                    if 1 < b < 11:
                                        cn += 18000
                                    if 10 < b < 51:
                                        cn += 1000
                            elif a > 10000000 or a <= 0:
                                print('=' * 23)
                                print('超出次数限制')
                                print('=' * 23)
                                clear_input()
                                continue
                            else:
                                print('=' * 23)
                                print('你的金币不足')
                                show(load_data['gold_coins'], '金币')
                                print('=' * 23)
                                clear_input()
                                cn = 0
                                continue
                        except:
                            print('=' * 23)
                            print('输入不合法')
                            continue
                        clear()
                        print('=' * 40)
                        print('抽奖小游戏')
                        print('=' * 40)
                        print('你总共抽了%d次' % a)
                        show(cn, '总计获得金币')
                        show(cn - a * 10000, '总计收益')
                        print('=' * 40)
                        load_data['gold_coins'] += cn
                        clear_input()
            elif t == '0':
                break
            else:
                pass
        # 充值面板循环
        while x == '5' and load_data['set']['1']:
            save(load_data)
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
                    clear_input()
                else:
                    print('=' * 28)
                    show(recharge, '充值金币')
                    load_data['gold_coins'] += recharge
                    show(load_data['gold_coins'], '目前金币')
                    print('=' * 28)
                    clear_input()
            except:
                pass
        # 设置面板循环
        while x == '*':
            save(load_data)
            char_recharge = '禁用' if load_data['set']['1'] else '启用'
            print('=' * 59)
            print('\033[32m设置\033[0m')
            print('=' * 59)
            print(('[1]{}充值功能                      [*]删除存档并退出游戏\n'
                   '[2]背景音乐\n'
                   '[0]返回首页\n'
                   '\n'
                   '[\033[36menter\033[0m]保存存档').format(char_recharge))
            print('=' * 59)
            o = clear_input()
            # 删档
            if o == '*':
                print('请确认是否删除现有存档（无法恢复）')
                print('[0]我再想想')
                print('[\033[36menter\033[0m]是的我确认我要删除存档')
                exit_game = clear_input()
                if exit_game == '':
                    delete_saveload()
                    break
            # 充值功能设置
            elif o == '1':
                load_data['set']['1'] = opposide(load_data['set']['1'])
            # 背景音乐
            elif o == '2':
                platfromList = ['netease', 'qq', 'kugou', 'kuwo', 'baidu']
                platfromListStr = ['网易云音乐(默认)', 'QQ音乐', '酷狗音乐', '酷我音乐', '百度音乐']
                platfrom = 'netease'
                platfromStr = platfromListStr[0]
                while True:
                    # 设置界面判断
                    music = os.path.exists(r'C:\ProgramData\DaiyuLinGototheJiaHome\music.mp3')
                    charDownload = '[4]切换背景音乐\n' if music else ''
                    charMusic = '暂停' if load_data['set']['2'] == 1 else '播放' if music else '下载并播放'
                    charDelete = '' if load_data['set']['2'] == 1 else '[3]删除背景音乐\n' if music else ''
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
                        if load_data['set']['2'] == 0:
                            music = os.path.exists(r'C:\ProgramData\DaiyuLinGototheJiaHome\music.mp3')
                            if music:
                                if isPause:
                                    mixer.music.unpause()
                                    load_data['set']['2'] = 1
                                    isPause = False
                                else:
                                    load_data['set']['2'] = play_music()
                            else:
                                get_music_name(platfrom)
                                clear()
                                load_data['set']['2'] = play_music()
                        else:
                            mixer.music.pause()
                            isPause = True
                            load_data['set']['2'] = 0
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
                            pygame_quit()
                            os.remove('C:\ProgramData\DaiyuLinGototheJiaHome\\music.mp3')
                        except:
                            print('=' * 30)
                            print('文件被占用或不存在')
                            print('=' * 30)
                            clear_input()
                    elif i == '4' and charDownload == '[4]切换背景音乐\n':
                        try:
                            print('当前搜索源为:%s' % platfromStr)
                            get_music_name(platfrom)
                            load_data['set']['2'] = play_music()
                            clear()
                        except:
                            print('=' * 30)
                            print('文件被占用或不存在')
                            print('=' * 30)
                            clear_input()
                    elif i == "0":
                        break
                    else:
                        pass
            # 存档
            elif o == '':
                save(load_data)
            # 返回
            elif o == '0':
                break
            else:
                continue
        # 管理员面板
        while x == '20030426':
            print('=============================\n'
                  '已进入管理员面板\n'
                  '[\033[36menter\033[0m]使用满级账号进入游戏\n'
                  '[1]设定值进入游戏\n'
                  '[2]重置存档\n'
                  '[0]返回\n'
                  '=============================')

            t = clear_input()
            if t == '':
                print('-' * 30)
                load_data = {'attack': 3000000, 'defence': 2500000, 'health': 8000000, 'int_challenge': 21,
                             'gold_coins': 100000000, 'invincible_potion': 10000, 'name': '管理员',
                             'set': {'1': 1, '2': 0},
                             'treasure': {'艾尔登法环': 1, '照妖镜': 1, '如意金箍棒': 1, '传送法典': 1, '史莱姆雕塑': 1}}
                save(load_data)
                break
            elif t == '1':
                while True:
                    try:
                        print('-' * 12)
                        print('  请依次输入')
                        print('-' * 12)
                        # 代码转换器
                        load_data = {'attack': float(input('攻击力：')), 'defence': float(input('防御力：')),
                                     'health': float(input('生命值：')),
                                     'int_challenge': 1, 'gold_coins': float(input('金币：')),
                                     'invincible_potion': int(input('无敌药水：')),
                                     'name': input('角色名：'), 'set': {'1': 1, '2': 0}, 'treasure': {}}
                        while load_data['name'] == '':
                            print('请输入你的角色名:')
                            load_data['name'] = clear_input()
                        save(load_data)
                        break
                    except:
                        clear()
                        print('输入有误请重新输入')
                        sleep(1)
                        clear()
                break
            elif t == '2':
                load_data = {'attack': 50, 'defence': 20, 'health': 200, 'int_challenge': 1, 'gold_coins': 0,
                             'invincible_potion': 0, 'set': {'1': 0, '2': 0}, 'name': clear_input(), 'treasure': {}}
                save(load_data)
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
            if q == '':
                # 关闭音乐
                if load_data['set']['2'] == 1:
                    pygame_quit()
                # 存档
                save(load_data)
                break
            else:
                continue
        # 刷新界面
        else:
            continue

    # 退出面板
    clear()
    print('============\n'
          ' 欢迎下次游玩\n'
          '============')
    sleep(1)
    quit()
