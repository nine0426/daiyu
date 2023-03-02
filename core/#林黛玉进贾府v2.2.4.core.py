import time
import random
import requests
import jsonpath
import shutil
import pygame
import os

# 下载音乐*
def song_download(url, title, author):
    print('歌曲:{0}-{1}\n正在下载...'.format(title, author))
    content = requests.get(url).content
    with open(file='1.mp3', mode='wb') as f:
        f.write(content)
    Newfolder('C:\ProgramData\DaiyuLinGototheJiaHome')
    folder = os.path.exists("C:\\ProgramData\\DaiyuLinGototheJiaHome\\1.mp3")
    if folder:
        os.remove("C:\\ProgramData\\DaiyuLinGototheJiaHome\\1.mp3")
    shutil.move("1.mp3", "C:\ProgramData\DaiyuLinGototheJiaHome")
    print('下载完毕'.format(title, author))

# 下载音乐
def get_music_name():
    """
    搜索歌曲名称
    :return:
    """
    name = input("请输入歌曲名称:")
    platfrom = 'netease'
    print("-------------------------------------------------------")
    url = 'https://music.liuzhijin.cn/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        # 判断请求是异步还是同步
        "x-requested-with": "XMLHttpRequest",
    }
    param = {
        "input": name,
        "filter": "name",
        "type": platfrom,
        "page": 1,
    }
    res = requests.post(url=url, data=param, headers=headers)
    json_text = res.json()

    title = jsonpath.jsonpath(json_text, '$..title')
    author = jsonpath.jsonpath(json_text, '$..author')
    url = jsonpath.jsonpath(json_text, '$..url')
    if title:
        songs = list(zip(title, author, url))
        t = 1
        for s in songs:
            print([t], s[0], s[1])
            t += 1
        print("==============")
        while True:
            try:
                index = int(input("请输入音乐的序号:")) - 1
                song_download(url[index], title[index], author[index])
                break
            except:
                print('输入错误(请输入正确的数字)')
    else:
        print("对不起，暂无搜索结果!")

# 停止音乐
def suspend_music():
    pygame.quit()

# 播放音乐
def play_music():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
        pygame.mixer.music.play(-1)
        return 1
    except:
        print('音乐文件已损坏，你可能下载了vip音乐')
        pygame.quit()
        folder = os.path.exists("C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3")
        if folder:
            os.remove("C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3")
        return 0

# 猜数字游戏比大小
def number_right(a, b):
    if a < b:
        print("你输入的数字太小")
        return False
    elif a > b:
        print("你输入的数字太大")
        return False
    else:
        print("猜对了")
        return True

# 金币格式化
def XianshiJb():
    if jb < 10000:
        print("金币: %d" % jb)
    if 10000 <= jb < 100000000:
        print("金币: %d万" % (jb // 10000))
    if 100000000 <= jb < 1000000000000:
        print("金币: %d亿" % (jb // 100000000))
    if jb >= 1000000000000:
        print("金币：超出显示长度")

# 怪物血量格式化
def XianshiGwHp(hp):
    if hp < 10000:
        print("怪物血量: %d" % jb)
    if 10000 <= hp < 100000000:
        print("怪物血量: %d万" % (jb // 10000))
    if 100000000 <= hp < 1000000000000:
        print("怪物血量: %d亿" % (jb // 100000000))

# 怪物攻击格式化
def XianshiGwAttack(hp):
    if hp < 10000:
        print("怪物攻击: %d" % jb)
    if 10000 <= hp < 100000000:
        print("怪物攻击: %d万" % (jb // 10000))
    if 100000000 <= hp < 1000000000000:
        print("怪物攻击: %d亿" % (jb // 100000000))

# 怪物防御格式化
def XianshiGwDefence(hp):
    if hp < 10000:
        print("怪物防御: %d" % jb)
    if 10000 <= hp < 100000000:
        print("怪物防御: %d万" % (jb // 10000))
    if 100000000 <= hp < 1000000000000:
        print("怪物防御: %d亿" % (jb // 100000000))

# 挑战函数化
def TiaoZhan(intnum, num, name, hp, attack, defence, gwzdl, zdl, jb, gq, gj, fy, sm, wdys, plusJb, plusGj, plusFy,
             plusSm, useWdys):
    hp = int(hp)
    defence = int(attack)
    attack = int(defence)
    print("------")
    print('''第%s关
------
怪物名称:%s''')
    XianshiGwHp(hp)
    XianshiGwAttack(defence)
    XianshiGwDefence(attack)
    print('''是否挑战此关卡
[enter]是
[0]否''')
    print("--------------")
    o = clearInput()
    if o == "":
        print("------")
        print("第%s关" % num)
        print("------")
        if zdl > gwzdl:
            # 奖励面板
            print("--------------------")
            print("你战胜了%s" % name)
            print("获得了%s个金币" % plusJb)
            intnum = int(intnum)
            if gq == intnum:
                gq += 1
            jb += plusJb
            gj += plusGj
            fy += plusFy
            sm += plusSm
            print("攻击力得到提升")
            print("生命值得到提升")
            print("防御力得到提升")
            print("输入任意回到关卡界面")
            print("--------------------")
            j = clearInput()
        else:
            print("%s打败了你" % name)
            print("------------------")
            if wdys > 0:
                print("是否使用%d瓶无敌药水" % useWdys)
                print("[enter]是 [0]否")
                n = clearInput()
                print("--------------")
                if n == "":
                    print("使用成功")
                    wdys = wdys - useWdys
                    print("剩余无敌药水: %s" % wdys)
                    print("----------------")
                    print("输入任意回到关卡界面")
                    m = clearInput()
                    print("--------------------")
                    print("你战胜了%s" % name)
                    print("获得了%s个金币" % plusJb)
                    jb += plusJb
                    jb += plusJb
                    gj += plusGj
                    fy += plusFy
                    sm += plusSm
                    print("攻击力得到提升")
                    print("生命值得到提升")
                    print("防御力得到提升")
                    print("输入任意回到关卡界面")
                    print("--------------------")
                    pp = clearInput()
                else:
                    backWait()
            else:
                print("提升属性再来吧")
                print("小提示:挑战之前的关卡可以提升属性")
                print("输入任意返回界面")
                print("--------------------")
                m = clearInput()
    else:
        print("----------------")
        print("返回关卡界面成功")
        print("----------------")

    return [gj, fy, sm, jb, gq, wdys]

# 返回等待
def backWait():
    print("------------")
    print("界面返回成功")
    print("------------")
    time.sleep(0.5)
    os.system("cls")

# 输入清屏
def clearInput():
    clear = input()
    os.system("cls")
    return clear

# 判定新玩家
def isNew():
    try:
        file_save = open("C:\ProgramData\DaiyuLinGototheJiaHome\save.txt", "r")
        file_save.close()
        return False
    except:
        return True

# 存档
def save(attack, defense, hp, guanqia, Goldcoins, wdys, name, set1, set2):
    file = "C:\ProgramData\DaiyuLinGototheJiaHome"
    Newfolder(file)
    file_save_data = open("C:\ProgramData\DaiyuLinGototheJiaHome\save.txt", "w")
    file_save_data.write(
        "**save1 {} {} {} {} {} {} {} {} {}".format(attack, defense, hp, guanqia, Goldcoins, wdys, name, set1, set2))
    file_save_data.close()

# 删除存档
def delete():
    os.remove("C:\ProgramData\DaiyuLinGototheJiaHome\save.txt")

# 新建文件夹
def Newfolder(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        return False
    else:
        return True


# 游戏界面
while True:
    z = 1
    # 公告
    while z == 1:
        os.system('cls')
        print("=" * 36)
        print("游戏名:林黛玉进贾府")
        print("目前版本:v2.2.4")
        print('''[*]支持自定义搜索歌曲背景音乐！
[1]格式化挑战数据
[2]新增抽奖小游戏
[3]菜单添加颜色
[4]其他优化

''')
        print("注意事项:")
        print("[1]请认真阅读每条信息")
        print("[2]游戏通过加载本地文档进行读档")
        print("-------------------------------")
        print("输入任意开始游戏")
        f = clearInput()
        # 管理员面板可循环
        while f == "20030426":
            print("-" * 30)
            print("已进入管理员面板")
            print("[enter]使用满级账号进入游戏")
            print("[2]使用代码转换")
            print("-" * 30)
            t = clearInput()
            if t == "":
                print("-" * 30)
                print("读取满级存档成功")
                print("载入成功")
                print("正在检查本地文件.....")
                print("-" * 30)
                time.sleep(1)
                gj = 1500000
                fy = 500000
                sm = 3000000
                gq = 21
                zdl = 2 * gj + 3 * fy + sm
                jb = 10000000
                wdys = 10000
                name = "管理员"
                set1 = 1
                set2 = 0
                save(gj, fy, sm, gq, jb, wdys, name, set1, set2)
                break
            if t == "2":
                while True:
                    try:
                        print("-" * 30)
                        print("请依次输入")
                        print("攻击力、防御力、生命值、金币、关卡、无敌药水、角色名")
                        print("-" * 30)
                        print("注意:")
                        print("攻击力50~10000")
                        print("防御力20~7000")
                        print("生命值200~100000")
                        print("关卡在1~10")
                        print("金币没有上限")
                        print("无敌药水没有上限")
                        print("开始输入代码：")
                        print("-" * 30)
                        # 代码转换器
                        gj = input("攻击力：")
                        fy = input("防御力：")
                        sm = input("生命值：")
                        gq = input("关卡：")
                        jb = input("金币：")
                        wdys = input("无敌药水：")
                        name = input("角色名：")
                        while " " in name:
                            print("角色名不能包含空格！")
                            print("请输入你的角色名:")
                            name = clearInput()
                        while name == "":
                            print("请输入你的角色名:")
                            name = clearInput()
                        gj = float(gj)
                        fy = float(fy)
                        sm = float(sm)
                        gq = float(gq)
                        jb = float(jb)
                        wdys = float(wdys)
                        set1 = 0
                        set2 = 0
                        # 代码输出器
                        save(gj, fy, sm, gq, jb, wdys, name, set1, set2)
                        print("-" * 30)
                        print("代码转换完成")
                        time.sleep(2)
                        print("六个代码输出成功")
                        print("已自动覆盖存档")
                        print("-" * 30)
                        break
                    except:
                        print("请重新输入")
                break
            else:
                continue
            # 新玩家判定器
        # 判断新玩家
        if isNew():
            print("-" * 30)
            print("欢迎你第一次游玩本游戏")
            print("请输入你的角色名:")
            print("-" * 30)
            name = clearInput()
            while " " in name:
                print("角色名不能包含空格！")
                print("请输入你的角色名:")
                name = clearInput()
            while name == "":
                print("请输入你的角色名:")
                name = clearInput()
            gj = 50
            fy = 20
            sm = 200
            zdl = 2 * gj + 3 * fy + sm
            jb = 0
            gq = 1
            wdys = 0
            set1 = 0
            set2 = 0
            save(gj, fy, sm, gq, jb, wdys, name, set1, set2)
            z = z + 1
        # 读档
        else:
            print("-" * 30)
            print("正在读取存档")
            try:
                file = "C:\ProgramData\DaiyuLinGototheJiaHome"
                Newfolder(file)
                file_save = open("C:\ProgramData\DaiyuLinGototheJiaHome\save.txt", "r")
                content1 = file_save.readline()
                content2 = content1[8:]
                content = content2.split()
                gj = float(content[0])
                fy = float(content[1])
                sm = float(content[2])
                gq = int(content[3])
                jb = float(content[4])
                wdys = float(content[5])
                name = content[6]
                set1 = int(content[7])
                set2 = int(content[8])
                file_save.close()
                if gj < 2 or fy < 0 or sm < 100 or gq < 1 or jb < 0 or wdys < 0:
                    print("存档文件已损坏")
                    time.sleep(1)
                    delete()
                    print("原存档已被删除")
                    print("--------------")
                if set1 == 1 or set1 == 0:
                    oo = 1
                if set2 == 1 or set2 == 0:
                    oo = 1
                if oo != 1:
                    print("存档文件已损坏")
                    time.sleep(1)
                    delete()
                    print("原存档已被删除")
                    print("--------------")
                print("-" * 30)
                time.sleep(0.5)
                os.system("cls")
                z += 1
            except:
                file_save.close()
                print("存档文件已损坏")
                time.sleep(1)
                delete()
                print("原存档已被删除")
                print("--------------")
                time.sleep(2)
                os.system("cls")
            if set2 == 1:
                set2 = play_music()
    # 游戏面板
    while z == 2:
        # 游戏主页面
        zdl = 2 * gj + 3 * fy + sm
        print('=============================================\n'
              '-------------------\033[33m主界面\033[0m--------------------\n'
              '=============================================\n'
              '[1]\033[31m挑战副本\033[0m                          \033[32m[x]退出\n\033[0m'
              '[2]\033[31m状态\033[0m     \n'
              '[3]\033[31m商城\033[0m\n'
              '[4]\033[31m益智小游戏\033[0m')
        if set1 == 1:
            print("\033[34m[5]充值\033[0m")
        print("                                     \033[32m[*]设置\033[0m")
        print("=============================================")
        # 菜单选择面板
        x = clearInput()
        # 关卡面板
        if x == "1":
            # 关卡选择器
            while True:
                zdl = 2 * gj + 3 * fy + sm
                print("=======================================")
                print("\033[31m挑战副本\033[0m")
                print("=======================================")
                print("目前你已解锁最新关卡为: %d/20" % gq)
                print("已解锁英雄副本 %d/2" % ((gq - 1) // 10))
                print("请输入你要挑战的关卡数(英雄副本加上前缀#):")
                print("[0]返回首页")
                print("=======================================")
                p = clearInput()
                # 关卡判定器
                try:
                    p = int(p)
                    if gq < p <= 10:
                        print("你输入的关卡未解锁")
                        time.sleep(1)
                    else:
                        if p == 0:
                            backWait()
                            break
                        # 第一关
                        elif p == 1:
                            a = TiaoZhan(1, "一", "哥布林小兵", 50, 10, 5, 0, zdl, jb, gq, gj, fy, sm, wdys, 10,
                                         4, 2, 5, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第二关
                        elif p == 2:
                            a = TiaoZhan(2, "二", "大哥布林", 200, 50, 20, 370, zdl, jb, gq, gj, fy, sm, wdys, 20,
                                         20, 20, 100, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第三关
                        elif p == 3:
                            a = TiaoZhan(3, "三", "哥布林首领", 300, 100, 60, 980, zdl, jb, gq, gj, fy, sm, wdys, 100,
                                         30, 25, 80, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第四关
                        elif p == 4:
                            a = TiaoZhan(4, "四", "哥布林司令官", 800, 300, 150, 1350, zdl, jb, gq, gj, fy, sm, wdys, 500,
                                         30, 25, 80, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第五关
                        elif p == 5:
                            a = TiaoZhan(5, "五", "蘑菇兵", 500, 300, 150, 1500, zdl, jb, gq, gj, fy, sm, wdys, 600,
                                         30, 25, 80, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第六关
                        elif p == 6:
                            a = TiaoZhan(6, "六", "蘑菇队长", 900, 350, 200, 2200, zdl, jb, gq, gj, fy, sm, wdys, 800,
                                         200, 100, 300, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第七关
                        elif p == 7:
                            a = TiaoZhan(7, "七", "蘑菇法师", 2500, 600, 400, 5000, zdl, jb, gq, gj, fy, sm, wdys, 1000,
                                         200, 100, 300, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第八关
                        elif p == 8:
                            a = TiaoZhan(8, "八", "蘑菇魔王", 4000, 1000, 800, 8500, zdl, jb, gq, gj, fy, sm, wdys, 2000,
                                         600, 300, 900, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第九关
                        elif p == 9:
                            a = TiaoZhan(9, "九", "蘑菇首领", 9000, 4700, 1400, 26600, zdl, jb, gq, gj, fy, sm, wdys, 5000,
                                         1200, 600, 1800, 1)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第十关
                        elif p == 10:
                            a = TiaoZhan(10, "十", "卢鑫(BOSS)", 20000, 10000, 5000, 45000, zdl, jb, gq, gj, fy, sm, wdys,
                                         5000,
                                         1200, 600, 1800, 5)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第十一关
                        elif p == 11:
                            a = TiaoZhan(11, "十一", "野蛮人门卫", 20000, 10000, 5000, 45000, zdl, jb, gq, gj, fy, sm, wdys,
                                         10000,
                                         1200, 600, 1800, 8)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第12关
                        elif p == 12:
                            a = TiaoZhan(12, "十二", "野蛮人小队", 30000, 20000, 7000, 100000, zdl, jb, gq, gj, fy, sm, wdys,
                                         10000,
                                         1200, 600, 1800, 8)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第13关
                        elif p == 13:
                            a = TiaoZhan(13, "十三", "野蛮人精英", 50000, 20000, 10000, 160000, zdl, jb, gq, gj, fy, sm, wdys,
                                         15000,
                                         3600, 1800, 5400, 10)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第14关
                        elif p == 14:
                            a = TiaoZhan(14, "十四", "野蛮人长老", 80000, 30000, 12000, 300000, zdl, jb, gq, gj, fy, sm, wdys,
                                         20000,
                                         3600, 1800, 5400, 10)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第15关
                        elif p == 15:
                            a = TiaoZhan(15, "十五", "野蛮人首领", 120000, 50000, 30000, 420000, zdl, jb, gq, gj, fy, sm, wdys,
                                         20000,
                                         10000, 8000, 20000, 12)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第16关
                        elif p == 16:
                            a = TiaoZhan(16, "十六", "隐秘之地", 0, 0, 0, 1500000, zdl, jb, gq, gj, fy, sm, wdys,
                                         50000,
                                         15000, 10000, 40000, 30)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第17关
                        elif p == 17:
                            a = TiaoZhan(17, "十七", "孙小圣(水帘洞)", 250000, 80000, 30000, 2200000, zdl, jb, gq, gj, fy, sm,
                                         wdys,
                                         80000,
                                         15000, 10000, 40000, 40)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第18关
                        elif p == 18:
                            a = TiaoZhan(18, "十八", "孙悟空的保镖(水帘洞)", 300000, 100000, 60000, 3000000, zdl, jb, gq, gj, fy,
                                         sm,
                                         wdys,
                                         100000,
                                         50000, 30000, 100000, 75)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第十一关
                        elif p == 19:
                            a = TiaoZhan(19, "十九", "孙悟空(水帘洞)", 400000, 200000, 100000, 4500000, zdl, jb, gq, gj, fy, sm,
                                         wdys,
                                         150000,
                                         50000, 30000, 100000, 125)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                        # 第十一关
                        elif p == 20:
                            a = TiaoZhan(20, "二十", "崔智鑫、李卓函和王富顺(BOSS)(新代猴王)", 500000, 300000, 150000, 7500000, zdl, jb,
                                         gq,
                                         gj,
                                         fy, sm, wdys,
                                         200000,
                                         100000, 50000, 180000, 200)
                            gj = a[0]
                            fy = a[1]
                            sm = a[2]
                            jb = a[3]
                            gq = a[4]
                            wdys = a[5]
                except:
                    if p == "#1":
                        a = TiaoZhan(1, "一（英雄）", "卢鑫(BOSS)", 50000, 20000, 10000, 145000, zdl, jb, gq, gj, fy, sm, wdys,
                                     15000,
                                     2400, 1200, 3600, 10)

                        gj = a[0]
                        fy = a[1]
                        sm = a[2]
                        jb = a[3]
                        gq = a[4]
                        wdys = a[5]
                    elif p == "#2":
                        a = TiaoZhan(2, "二（英雄）", "崔智鑫、李卓函和王富顺(BOSS)(新代猴王)", 233333333, 1919810, 114514, 14500000, zdl,
                                     jb,
                                     gq,
                                     gj, fy, sm, wdys, 500000,
                                     150000, 50000, 200000, 250)

                        gj = a[0]
                        fy = a[1]
                        sm = a[2]
                        jb = a[3]
                        gq = a[4]
                        wdys = a[5]
                    else:
                        print("--------------")
                        print("输入的关卡不合法或者未解锁")
                        print("输入任意继续")
                        print("--------------")
                        t = clearInput()
        # 状态面板
        elif x == "2":
            while True:
                print("=====================")
                print("\033[31m状态\033[0m")
                print("=====================")
                print("角色名: %s" % name)
                print("生命值: %d" % sm)
                print("攻击力: %d" % gj)
                print("防御力: %d" % fy)
                print("=====================")
                XianshiJb()
                print("=====================")
                print("[1]无敌药水 :%d瓶" % wdys)
                print("[0]返回首页")
                print("=====================")
                t = clearInput()
                if t == "1":
                    print("------------------------")
                    print("无敌药水: %d瓶" % wdys)
                    print("在关卡无法闯过可以使用")
                    print("输入任意返回界面")
                    print("------------------------")
                    t = clearInput()
                elif t == "0":
                    backWait()
                    break
                else:
                    backWait()
        # 商城面板
        elif x == "3":
            r = 0
            while r == 0:
                print("============================")
                print("\033[31m商城\033[0m")
                print("============================")
                XianshiJb()
                print("目前商品:")
                print("[1]无敌药水")
                print("[2]满级药水")
                print("[3]改名卡")
                print("[4]属性加强药水")
                print("---请输入商品序号选择购买---")
                print("-------[0]返回首页--------")
                print("------------------------")
                f = clearInput()
                # 返回面板
                if f == "0":
                    backWait()
                    r = r + 1
                    pass
                # 无敌药水
                elif f == "1":
                    print("---------------------")
                    XianshiJb()
                    print("无敌药水")
                    print("金币:1500")
                    print("属性:只要你的无敌药水够多没有你通不过的关卡")
                    print("是否选择购买")
                    print("[enter]是 [0]否")
                    print("---------------------")
                    g = clearInput()
                    if g == "":
                        print("---------------------")
                        print("请输入你要购买的数量:")
                        print("---------------------")
                        x = clearInput()
                        try:
                            x = int(x)
                            if x > 0:
                                if jb >= 1500 * x:
                                    jb = jb - 1500 * x
                                    wdys = wdys + x
                                    print("------------")
                                    print("购买成功")
                                    XianshiJb()
                                    print("无敌药水: %s瓶" % wdys)
                                    print("输入任意返回界面")
                                    print("--------------")
                                    t = clearInput()
                                    pass
                                elif jb < 1500 * x:
                                    print("-------------------")
                                    print("你的金币不足")
                                    XianshiJb()
                                    print("输入任意返回界面")
                                    print("-------------------")
                                    t = clearInput()
                            else:
                                print("-------------------")
                                print("输入错误正在返回首页")
                                print("-------------------")
                                backWait()
                        except:
                            backWait()
                    else:
                        backWait()
                # 满级药水
                elif f == "2":
                    print("=========================")
                    print("初级满级药水")
                    print("金币:100万")
                    XianshiJb()
                    print("属性:可以瞬间达到第十关最强状态")
                    print("是否选择购买")
                    print("[enter]是 [0]否")
                    print("=========================")
                    g = clearInput()
                    if g == "":
                        if sm < 100000 or gj < 10000 or fy < 7000:
                            if jb > 1000000:
                                print("=========================")
                                print("购买成功")
                                print("已自动使用成功")
                                jb = jb - 1000000
                                sm = 100000
                                gj = 10000
                                fy = 7000
                                XianshiJb()
                                print("目前属性:")
                                print("生命值:100000")
                                print("攻击力:10000")
                                print("防御力:7000")
                                print("输入任意返回界面")
                                print("=========================")
                                t = clearInput()
                            elif jb < 5000000:
                                print("=========================")
                                print("你的金币不足")
                                XianshiJb()
                                print("输入任意返回界面")
                                print("=========================")
                                t = clearInput()
                        else:
                            print("-----------------------------")
                            print("你的属性太高 这种药剂对你无效")
                            print("-----------------------------")
                    elif g == "0":
                        backWait()
                # 改名卡
                elif f == "3":
                    print("=========================")
                    print("改名卡")
                    print("金币:1万")
                    XianshiJb()
                    print("属性:给你一次修改名字的机会")
                    print("是否选择购买")
                    print("[enter]是 [0]否")
                    print("=========================")
                    g = clearInput()
                    if g == "":
                        if jb > 10000:
                            print("==================")
                            print("购买成功")
                            XianshiJb(jb)
                            print("请输入你的新角色名:")
                            print("==================")
                            name = clearInput()
                            while " " in name:
                                print("角色名不能包含空格！")
                                print("请输入你的角色名:")
                                name = clearInput()
                            while name == "":
                                print("请输入你的角色名:")
                                name = clearInput()
                            print("==================")
                            print("角色名修改完成")
                            jb = jb - 10000
                            print("输入任意返回界面")
                            print("==================")
                            t = clearInput()
                        elif jb < 10000:
                            print("======================")
                            print("你的金币不足")
                            XianshiJb()
                            print("输入任意返回界面")
                            print("======================")
                            t = clearInput()
                    elif g == "0":
                        backWait()
                    pass
                # 属性加强药水
                elif f == "4":
                    print("=================================")
                    print("属性加强药水")
                    print("金币:2000")
                    XianshiJb()
                    print("属性:增加生命1000攻击300防御200")
                    print("是否选择购买")
                    print("[enter]是 [0]否")
                    print("=================================")
                    g = clearInput()
                    if g == "":
                        print("=================")
                        print("请输入你要购买的数量:")
                        print("=================")
                        x = clearInput()
                        try:
                            x = int(x)
                            if x > 0:
                                if jb >= 2000 * x and sm < 100000 and gj < 10000 and fy < 7000:
                                    print("=================")
                                    print("购买成功")
                                    jb = jb - 2000 * x
                                    XianshiJb()
                                    print("目前属性:")
                                    print("生命值:%s" % (sm + 1000 * x))
                                    print("攻击力:%s" % (gj + 300 * x))
                                    print("防御力:%s" % (fy + 200 * x))
                                    sm = sm + 1000 * x
                                    gj = gj + 300 * x
                                    fy = fy + 200 * fy
                                    print("输入任意返回界面")
                                    print("=================")
                                    t = clearInput()
                                    pass
                                else:
                                    print("=================")
                                    print("你的购买不合要求")
                                    print("输入任意返回界面")
                                    print("=================")
                                    t = clearInput()
                            else:
                                backWait()
                        except:
                            backWait()
                    else:
                        backWait()
                # 查询无果面板
                else:
                    print("=================")
                    print("目前没有该商品")
                    print("输入任意返回界面")
                    print("=================")
                    t = clearInput()
        # 小游戏面板
        elif x == "4":
            while True:
                print("=====================")
                print("\033[31m益智小游戏\033[0m")
                print("=====================")
                print("[1]猜数字游戏")
                print("[2]抽奖小游戏")
                print("[0]返回首页")
                print("=====================")
                t = clearInput()
                if t == "1":
                    print("=======================")
                    print("猜数字游戏")
                    print("=======================")
                    print("系统会随机生成1到100的整数")
                    print("你可以通过输入来猜测随机的数字")
                    print("猜的次数越少获得的奖励越多")
                    print("[enter]开始游戏")
                    print("[0]返回首页")
                    print("=======================")
                    t = clearInput()
                    if t == "":
                        b = int(random.randint(1, 100))
                        fg = False
                        cn = 0
                        while not fg:
                            print("猜数字游戏")
                            print("[0]退出游戏")
                            print("=====================")
                            a = input("你的第%s次输入:" % (cn + 1))
                            if a == "0":
                                os.system('cls')
                                cn = 0
                                break
                            try:
                                a = int(a)
                                os.system("cls")
                                print("=====================")
                                fg = number_right(a, b)
                                cn = cn + 1
                            except:
                                print("------------")
                                print("输入不合法")
                                backWait()
                        time.sleep(1)
                        os.system("cls")
                        if 0 < cn < 8:
                            fuckyou = 8 - cn
                        elif cn > 8:
                            fuckyou = 1
                        if cn == 0:
                            pass
                        else:
                            print("========================================")
                            print("猜数字游戏")
                            print("========================================")
                            print("你猜了%s次得到了答案" % cn)
                            print("你的生命、攻击、防御、金币增加%d%%" % fuckyou)
                            if fuckyou == 0:
                                print("运气不太好继续加油吧！")
                            print("========================================")
                            gj *= (1 + fuckyou / 100)
                            gj *= (1 + fuckyou / 100)
                            gj *= (1 + fuckyou / 100)
                            gj *= (1 + fuckyou / 100)
                            time.sleep(3)
                            os.system("cls")
                elif t == "2":
                    print("=======================")
                    print("抽奖小游戏")
                    print("=======================")
                    print("你可以支付10000金币进行一次抽奖")
                    print("1%概率获得80万金币")
                    print("9%概率获得1.5万金币")
                    print("40%概率获得1000金币")
                    print("[enter]开始游戏")
                    print("[0]返回首页")
                    print("=======================")
                    t = clearInput()
                    if t == "":
                        while True:
                            print("=======================")
                            print("抽奖小游戏")
                            print("=======================")
                            print("请输入你要抽奖的次数")
                            XianshiJb()
                            print("[0]返回首页")
                            print("=======================")
                            a = clearInput()
                            fg = False
                            cn = 0
                            if a == "0":
                                os.system('cls')
                                cn = 0
                                break
                            try:
                                a = int(a)
                                if jb > 2000 * a:
                                    for i in range(a):
                                        b = int(random.randint(1, 100))
                                        if b == 1:
                                            cn += 800000
                                        if 1 < b < 11:
                                            cn += 15000
                                        if 10 < b < 51:
                                            cn += 1000
                            except:
                                print("------------")
                                print("输入不合法")
                                backWait()
                                continue
                            time.sleep(1)
                            os.system("cls")
                            if cn ==0:
                                print("==================")
                                print("抽奖小游戏")
                                print("==================")
                                print("金币不足")
                                backWait()
                                break
                            print("========================================")
                            print("抽奖小游戏")
                            print("========================================")
                            print("你总共抽了%d次" % a)
                            print("你获得了%d金币" % cn)
                            print("========================================")
                            time.sleep(3)
                            jb+=cn
                            os.system("cls")
                elif t == "0":
                    backWait()
                    break
                else:
                    backWait()
        # 退出面板
        elif x == "x":
            print("==============")
            print("请确定是否\033[32m[x]退出\n\033[0m")
            print("[enter]是")
            print("[0]否")
            print("==============")
            q = clearInput()
            # 退出确定
            if q == "":
                print("=====================")
                print("正在准备进行代码转换")
                print("代码转换进行中 请耐心等待")
                time.sleep(0.5)
                print("=====================")
                os.system("cls")
                # 代码输出器
                print("=====================")
                print("存档已自动保存成功")
                print("=====================")
                save(gj, fy, sm, gq, jb, wdys, name, set1, set2)
                time.sleep(0.5)
                z = z + 1
                os.system("cls")
            # 退出取消
            else:
                print("=====================")
                print("主页面返回成功")
                print("=====================")
                time.sleep(0.5)
                os.system("cls")
                pass
        # 充值面板
        elif x == "5" and set1 == 1:
            while True:
                print("=========================================")
                print("\033[34m[5]充值\033[0m")
                XianshiJb()
                print("请输入你要充值的金币数（1元等于1000金币）：)")
                print("[0]返回首页")
                print("=========================================")
                cz = clearInput()
                try:
                    cz = int(cz)
                    if cz == 0:
                        backWait()
                        break
                    elif cz < 0:
                        print("============================")
                        print("金币输入不合法")
                        print("输入任意返回界面")
                        print("============================")
                        t = clearInput()
                    else:
                        print("============================")
                        print("请输入你的手机号:")
                        print("============================")
                        sjh = clearInput()
                        sjh = int(sjh)
                        if 10000000000 < sjh < 20000000000:
                            print("============================")
                            if cz < 10000:
                                print("充值%d金币成功" % cz)
                            if 10000 <= cz < 100000000:
                                print("充值%d万金币成功" % (cz // 10000))
                            if 100000000 <= cz < 1000000000000:
                                print("充值%d亿金币成功" % (cz // 100000000))
                            if cz >= 1000000000000:
                                print("充值超出显示长度金币成功")
                            hf = cz / 1000
                            jb = jb + cz
                            if jb < 10000:
                                print("目前金币: %d" % jb)
                            if 10000 <= jb < 100000000:
                                print("目前金币: %d万" % (jb // 10000))
                            if 100000000 <= jb < 1000000000000:
                                print("目前金币: %d亿" % (jb // 100000000))
                            if jb >= 1000000000000:
                                print("目前金币：超出显示长度")
                            print("输入任意返回界面")
                            print("============================")
                            t = clearInput()
                        else:
                            print("============================")
                            print("手机号码输入错误")
                            print("充值失败")
                            print("输入任意返回界面")
                            print("============================")
                            t = clearInput()
                except:
                    print("============================")
                    print("金币输入不合法")
                    print("输入任意返回界面")
                    print("============================")
                    time.sleep(1)
                    os.system("cls")
            # 输入任意重载主面板
        # 设置面板
        elif x == "*":
            while True:
                if set1 == 1:
                    charChongZhi = "禁用"
                else:
                    charChongZhi = "启用"
                print("===========================================================")
                print("\033[32m[*]设置\033[0m")
                print("===========================================================")
                print(('[1]暂时{}充值功能                            [*]删除存档\n'
                       '[2]背景音乐                          [-]浏览上个版本的公告\n'
                       '[0]返回首页\n'
                       '[enter]保存存档').format(charChongZhi))
                print("===========================================================")
                o = clearInput()
                if o == "*":
                    print("！请确认删除现有存档（无法恢复）")
                    print("[0]我再想想")
                    print("[1]是的我确认我要删除存档")
                    u = clearInput()
                    if u == "1":
                        print("！！！请再次确认删除现有存档（无法恢复）")
                        print("[0]我再想想")
                        print("[1]是的我确认我要删除存档")
                        u = clearInput()
                        if u == "1":
                            delete()
                            z -= 1
                            break
                elif o == "0":
                    backWait()
                    break
                elif o == "1":
                    if set1 == 0:
                        print("============")
                        print("充值系统已启用")
                        print("============")
                        set1 = 1
                        time.sleep(0.8)
                        os.system("cls")
                    else:
                        print("============")
                        print("充值系统已禁用")
                        print("============")
                        set1 = 0
                        time.sleep(0.8)
                        os.system("cls")
                elif o == "-":
                    print("游戏名:林黛玉进贾府")
                    print("版本:v2.0.0")
                    print('[1]更新clear界面\n'
                          '[2]更新本地存档加载，更新存档有关功能\n'
                          '[3]修复所有已发现导致崩溃的bug\n'
                          '[4]金币使用新的展示方式\n'
                          '[5]修改关卡的部分文字\n'
                          '[6]修复1.3.9商城无法购买的bug\n'
                          '[7]可以使用enter键直接进行下一步\n'
                          '[8]合并人物和背包为状态\n'
                          '[9]增加设置面板\n'
                          '\n'
                          '版本:v2.0.1\n'
                          '[1]存档位置变更为C:\ProgramData\DaiyuLinGototheJiaHome\save.txt\n'
                          '[2]重新设置部分加载方式\n'
                          '[3]充值功能纳入设置\n'
                          '[4]简化退出方式\n'
                          '\n'
                          '版本:v2.0.2\n'
                          '[1]优化商城\n'
                          '[2]优化金币显示\n'
                          '[3]取消存档加密\n'
                          '\n'
                          '版本:v2.0.3\n'
                          '[1]更新存档损坏判断\n'
                          '[2]优化界面排版\n'
                          '[3]增加英雄副本\n'
                          '\n'
                          '版本:v2.1.0\n'
                          '[1]减少代码错误\n'
                          '[2]新增小游戏\n'
                          '[3]用函数加载关卡优化关卡难度增加关卡至20关\n'
                          '[4]名字不能再包含空格\n'
                          '\n'
                          '版本:v2.2.0\n'
                          '[1]修复改名卡bug\n'
                          '[2]充值面板优化\n'
                          '[3]设置增加存档功能\n'
                          '[4]进行了代码打包\n'
                          '\n'
                          '版本v2.2.1\n'
                          '[1]新增背景音乐《wonderful world》 (目录为C:\ProgramData\DaiyuLinGototheJiaHome\music.mp3)\n'
                          '[2]修复小游戏无法中途退出的bug并提高小游戏收益\n'
                          '[3]设置界面可以选择开启背景音乐\n'
                          '[4]管理员面板更新\n'
                          '[5]简化开始流程\n'
                          '\n'
                          '版本v2.2.2\n'
                          '[1]修复小游戏中途退出领奖的bug\n'
                          '[2]去除pygame模块加载的广告'
                          '版本v2.2.3-4\n'
                          '[*]支持自定义搜索歌曲背景音乐！\n'
                          '[1]格式化挑战数据\n'
                          '[2]新增抽奖小游戏\n'
                          '[3]菜单添加颜色\n'
                          '[4]其他优化')
                    clearInput()
                    backWait()
                elif o == "":
                    print('============')
                    print('保存存档成功')
                    print('============')
                    save(gj, fy, sm, gq, jb, wdys, name, set1, set2)
                    time.sleep(0.8)
                    os.system("cls")
                elif o == "2":
                    while True:
                        if set2 == 1:
                            charMusic = "关闭"
                        else:
                            charMusic = "播放"
                        print("===========================================================")
                        print("设置")
                        print("===========================================================")
                        print(('[1]{}背景音乐\n'
                               '[2]删除背景音乐\n'
                               '[3]切换背景音乐\n'
                               '[0]返回首页').format(charMusic))
                        print("===========================================================")
                        i = clearInput()
                        if i == "1":
                            if set2 == 0:
                                music = os.path.exists('C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3')
                                if music:
                                    print("==============")
                                    print("开始播放背景音乐")
                                    print("==============")
                                    play_music()
                                    set2 = 1
                                    time.sleep(0.8)
                                    os.system("cls")
                                else:
                                    get_music_name()
                                    time.sleep(0.8)
                                    os.system("cls")
                            else:
                                print("============")
                                print("背景音乐已关闭")
                                print("============")
                                suspend_music()
                                set2 = 0
                                time.sleep(0.8)
                                os.system("cls")
                        elif i == "2":
                            try:
                                os.remove("C:\ProgramData\DaiyuLinGototheJiaHome\\1.mp3")
                                print("============")
                                print("删除成功")
                                print("============")
                                time.sleep(0.8)
                                os.system("cls")
                            except:
                                print("==============================")
                                print("文件被占用或不存在\n请先关闭音乐重载游戏后重试")
                                print("==============================")
                                time.sleep(2)
                                os.system("cls")
                        elif i == "0":
                            backWait()
                            break
                        elif i == "3":
                            try:
                                if set2 == 1:
                                    suspend_music()
                                get_music_name()
                                time.sleep(0.8)
                                print("开始播放背景音乐")
                                print("==============")
                                play_music()
                                set2 = 1
                                os.system("cls")
                            except:
                                print("==============================")
                                print("文件被占用或不存在\n请先关闭音乐重载游戏后重试")
                                print("==============================")
                                time.sleep(2)
                                os.system("cls")
                            else:
                                backWait()
                else:
                    backWait()
        # 刷新界面
        else:
            time.sleep(0.1)
            continue
    # 感谢游玩面板
    while z == 3:
        print("=============")
        print("欢迎下次游玩")
        print("=============")
        time.sleep(1)
        quit()
        z = z + 1
