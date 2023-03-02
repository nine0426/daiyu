import time
import os

def backWait():
    print("------------")
    print("界面返回成功")
    print("------------")
    time.sleep(0.3)
    os.system("cls")

def clearInput():
    clear = input()
    os.system("cls")
    return clear

def isNew():
    try:
        file_save = open("save.txt", "r")
        file_save.close()
        return False
    except:
        return True

def save(gj, fy, sm, gq, jb, wdys, name):
    file_save = open("save.txt", "w")
    a = (gj - 7) / 5
    b = (15 - fy) / 4
    c = (-sm) / 4
    d = gq + 40
    e = jb / 50 - 1400
    f = wdys - 34
    file_save.write("**save1{} {} {} {} {} {} {}".format(a, b, c, d, e, f, name))
    file_save.close()

def delete():
    os.remove("save.txt")


w = 0
while w == 0:
    print("游戏名:林黛玉进贾府")
    print("目前版本:v2.0.0")
    print('''[1]更新clear界面
[2]更新本地存档加载，更新存档有关功能
[3]修复所有已发现导致崩溃的bug
[4]金币使用新的展示方式
[5]修改关卡的部分文字
[6]修复1.3.9商城无法购买的bug
[7]可以使用enter键直接进行下一步
[8]合并人物和背包为状态
[9]增加设置面板

即将添加的功能：
增加英雄副本和普通副本
存档文件升级
增加商场商品
增加宝箱功能抽奖功能
增加设置功能

''')
    print("注意事项:")
    print("[1]请认真阅读每条信息")
    print("[2]最新关卡为[第十关]")
    print("[3]游戏通过加载本地文档进行读档")
    print("[4]需要python编程环境(你能打开说明你有)")
    print("-------------------------------")
    print("看完说明后输入任意开始游戏")
    j = clearInput()
    break
# 游戏界面
while True:
    z = 1
    # 游戏读档面板
    while z == 1:
        print("-------------游戏界面---------------")
        print("-------输入任意开始加载代码---------")
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
                gj = 10000
                fy = 7000
                sm = 100000
                gq = 10
                zdl = 2 * gj + 3 * fy + sm
                jb = 1000000
                wdys = 100
                name = "管理员"
                save(gj, fy, sm, gq, jb, wdys, name)
                break
            if t == "2":
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
                gj = float(gj)
                fy = float(fy)
                sm = float(sm)
                gq = float(gq)
                jb = float(jb)
                wdys = float(wdys)
                # 代码输出器
                save(gj, fy, sm, gq, jb, wdys, name)
                print("-" * 30)
                print("代码转换完成")
                time.sleep(2)
                print("六个代码输出成功")
                print("已自动覆盖存档")
                print("-" * 30)
                break
            else:
                continue
            # 新玩家判定器
        if isNew():
            print("-" * 30)
            print("欢迎你第一次游玩本游戏")
            print("请输入你的角色名:")
            print("-" * 30)
            name = clearInput()
            while name == "":
                print("角色名不能为空！")
                print("请输入你的角色名:")
                name = clearInput()
            print("-" * 30)
            gj = 50
            fy = 20
            sm = 200
            zdl = 2 * gj + 3 * fy + sm
            jb = 0
            gq = 1
            wdys = 0
            save(gj, fy, sm, gq, jb, wdys, name)
            z = z + 1
        else:
            print("-" * 30)
            print("正在读取存档")
            try:
                file_save = open("save.txt", "r")
                content1 = file_save.readline()
                content2 = content1[7:]
                content = content2.split()
                a = float(content[0])
                b = float(content[1])
                c = float(content[2])
                d = float(content[3])
                e = float(content[4])
                f = float(content[5])
                name = content[6]
                gj = 5 * a + 7
                fy = 15 - 4 * b
                sm = -4 * c
                gq = d - 40
                jb = (e + 1400) * 50
                wdys = 34 + f
                file_save.close()
                print("-" * 30)
                time.sleep(0.5)
                os.system("cls")
                z += 1
            except:
                print("存档文件已损坏")
                time.sleep(1)
                delete()
                print("原存档已被删除")
                print("--------------")
    # 游戏面板
    while z == 2:
        # 游戏主页面
        chongZhi =True
        zdl = 2 * gj + 3 * fy + sm
        print("==============")
        print("----主界面----")
        print("==============")
        print("[1]挑战")
        print("[2]状态")
        print("[3]商城")
        print("[4]退出")
        if chongZhi:
            print("[5]充值")
        print("[*]设置")
        print("==============")
        # 菜单选择面板
        x = clearInput()
        # 关卡面板
        if x == "1":
            # 关卡选择器
            while True:
                zdl = 2 * gj + 3 * fy + sm
                print("===============================")
                print("挑战")
                print("===============================")
                print("目前你已解锁最新关卡为: %s/10" % (gq))
                print("英雄副本暂未开启 0/0")
                print("请输入你要挑战的关卡数:")
                print("[0]返回首页")
                print("===============================")
                p = clearInput()
                # 关卡判定器
                try:
                    p=int(p)
                    if p > gq and p <= 10: 
                        print("你输入的关卡未解锁")
                        time.sleep(1)
                    else:
                        if p == 0:
                            print("------------")
                            print("界面返回成功")
                            print("------------")
                            time.sleep(1)
                            break
                        # 第一关
                        elif p == 1:
                            print("------")
                            print("第一关")
                            print("------")
                            print("怪物名称:小哥布林(简单)")
                            print("怪物血量:50")
                            print("怪物攻击:10")
                            print("怪物防御:5")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("--------------")
                                print("第一关")
                                print("--------------")
                                if gq == 1:
                                    gq = 2
                                print("你战胜了小哥布林")
                                print("获得了十个金币")
                                jb = jb + 10
                                if gj < 80:
                                    gj = gj + 2
                                    print("攻击力得到小幅提升")
                                if fy < 40:
                                    fy = fy + 1
                                    print("防御力得到小幅提升")
                                if sm < 250:
                                    sm = sm + 4
                                    print("生命值得到小幅提升")
                                    print("--------------")
                                print("输入任意返回关卡界面")
                                print("--------------")
                                t = clearInput()
                            else:
                                backWait()
                        # 第二关
                        elif p == 2:
                            print("------")
                            print("第二关")
                            print("------")
                            print("怪物名称:大哥布林(简单)")
                            print("怪物血量:200")
                            print("怪物攻击:50")
                            print("怪物防御:20")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("--------------")
                                print("第二关")
                                print("--------------")
                                print("你战胜了大哥布林")
                                print("获得了20个金币")
                                jb = jb + 20
                                if gq == 2:
                                    gq = 3
                                if gj < 120:
                                    gj = gj + 3
                                    print("攻击力得到小幅提升")
                                if fy < 80:
                                    fy = fy + 2
                                    print("防御力得到小幅提升")
                                if sm < 400:
                                    sm = sm + 7
                                    print("生命值得到小幅提升")
                                print("输入任意回到关卡界面")
                                print("--------------------")
                                j = clearInput()
                            else:
                                backWait()
                        # 第三关
                        elif p == 3:
                            print("------")
                            print("第三关")
                            print("------")
                            print("怪物名称:哥布林首领(中等)")
                            print("怪物血量:300")
                            print("怪物攻击:100")
                            print("怪物防御:60")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 980
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第三关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了哥布林首领")
                                    print("获得了100个金币")
                                    jb = jb + 100
                                    if gq == 3:
                                        gq = 4
                                        pass
                                    if gj < 300:
                                        gj = gj + 5
                                        print("攻击力得到提升")
                                        pass
                                    if fy < 200:
                                        fy = fy + 4
                                        print("防御力得到提升")
                                        pass
                                    if sm < 1000:
                                        sm = sm + 12
                                        print("生命值得到提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("哥布林首领打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("--------------------")
                                            print("你战胜了哥布林首领")
                                            print("获得了100个金币")
                                            jb = jb + 100
                                            if gq == 3:
                                                gq = 4
                                                pass
                                            if gj < 300:
                                                gj = gj + 5
                                                print("攻击力得到提升")
                                                pass
                                            if fy < 200:
                                                fy = fy + 4
                                                print("防御力得到提升")
                                                pass
                                            if sm < 1000:
                                                sm = sm + 12
                                                print("生命值得到提升")
                                                pass
                                            else:
                                                print("属性没有得到提升")
                                                print("--------------")
                                                pass
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第四关
                        elif p == 4:
                            print("------")
                            print("第四关")
                            print("------")
                            print("怪物名称:哥布林司令官(困难)")
                            print("怪物血量:800")
                            print("怪物攻击:300")
                            print("怪物防御:150")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 1850
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第四关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了哥布林司令官")
                                    print("获得了500个金币")
                                    jb = jb + 500
                                    if gq == 4:
                                        gq = 5
                                        pass
                                    if gj < 500:
                                        gj = gj + 10
                                        print("攻击力得到提升")
                                        pass
                                    if fy < 300:
                                        fy = fy + 7
                                        print("防御力得到提升")
                                        pass
                                    if sm < 1500:
                                        sm = sm + 50
                                        print("生命值得到提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("哥布林司令官打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了哥布林司令官")
                                            print("获得了500个金币")
                                            jb = jb + 500
                                            if gq == 4:
                                                gq = 5
                                                pass
                                            if gj < 500:
                                                gj = gj + 10
                                                print("攻击力得到提升")
                                                pass
                                            if fy < 300:
                                                fy = fy + 7
                                                print("防御力得到提升")
                                                pass
                                            if sm < 1500:
                                                sm = sm + 50
                                            print("生命值得到提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第五关
                        elif p == 5:
                            print("------")
                            print("第五关")
                            print("------")
                            print("怪物名称:蘑菇兵(简单)")
                            print("怪物血量:500")
                            print("怪物攻击:200")
                            print("怪物防御:150")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 1200
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第四关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了蘑菇兵")
                                    print("获得了400个金币")
                                    jb = jb + 400
                                    if gq == 5:
                                        gq = 6
                                        pass
                                    if gj < 800:
                                        gj = gj + 20
                                        print("攻击力得到提升")
                                        pass
                                    if fy < 500:
                                        fy = fy + 20
                                        print("防御力得到提升")
                                        pass
                                    if sm < 2000:
                                        sm = sm + 50
                                        print("生命值得到提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("蘑菇兵打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了蘑菇兵")
                                            print("获得了400个金币")
                                            jb = jb + 400
                                            if gq == 5:
                                                gq = 6
                                                pass
                                            if gj < 800:
                                                gj = gj + 30
                                                print("攻击力得到提升")
                                                pass
                                            if fy < 500:
                                                fy = fy + 20
                                                print("防御力得到提升")
                                                pass
                                            if sm < 2000:
                                                sm = sm + 50
                                            print("生命值得到提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第六关
                        elif p == 6:
                            print("------")
                            print("第六关")
                            print("------")
                            print("怪物名称:蘑菇队长(中等)")
                            print("怪物血量:900")
                            print("怪物攻击:350")
                            print("怪物防御:200")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 2200
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第四关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了蘑菇兵")
                                    print("获得了800个金币")
                                    jb = jb + 800
                                    if gq == 6:
                                        gq = 7
                                        pass
                                    if gj < 1000:
                                        gj = gj + 50
                                        print("攻击力得到提升")
                                        pass
                                    if fy < 700:
                                        fy = fy + 30
                                        print("防御力得到提升")
                                        pass
                                    if sm < 3000:
                                        sm = sm + 150
                                        print("生命值得到提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("蘑菇队长打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了蘑菇队长")
                                            print("获得了800个金币")
                                            jb = jb + 800
                                            if gq == 6:
                                                gq = 7
                                                pass
                                            if gj < 1000:
                                                gj = gj + 50
                                                print("攻击力得到提升")
                                                pass
                                            if fy < 700:
                                                fy = fy + 30
                                                print("防御力得到提升")
                                                pass
                                            if sm < 2000:
                                                sm = sm + 150
                                            print("生命值得到提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第七关
                        elif p == 7:
                            print("------")
                            print("第七关")
                            print("------")
                            print("怪物名称:蘑菇法师(困难)")
                            print("怪物血量:2500")
                            print("怪物攻击:600")
                            print("怪物防御:400")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 4900
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第七关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了蘑菇法师")
                                    print("获得了1500个金币")
                                    jb = jb + 1500
                                    if gq == 7:
                                        gq = 8
                                        pass
                                    if gj < 1500:
                                        gj = gj + 70
                                        print("攻击力得到提升")
                                        pass
                                    if fy < 1000:
                                        fy = fy + 50
                                        print("防御力得到提升")
                                        pass
                                    if sm < 5000:
                                        sm = sm + 200
                                        print("生命值得到提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("蘑菇法师打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了蘑菇法师")
                                            print("获得了1500个金币")
                                            jb = jb + 1500
                                            if gq == 7:
                                                gq = 8
                                                pass
                                            if gj < 1500:
                                                gj = gj + 50
                                                print("攻击力得到提升")
                                                pass
                                            if fy < 1000:
                                                fy = fy + 50
                                                print("防御力得到提升")
                                                pass
                                            if sm < 5000:
                                                sm = sm + 200
                                            print("生命值得到提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第八关
                        elif p == 8:
                            print("------")
                            print("第八关")
                            print("------")
                            print("怪物名称:蘑菇魔王(困难)")
                            print("怪物血量:4000")
                            print("怪物攻击:1000")
                            print("怪物防御:800")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 8400
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第八关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了蘑菇魔王")
                                    print("获得了2500个金币")
                                    jb = jb + 2500
                                    if gq == 8:
                                        gq = 9
                                        pass
                                    if gj < 2000:
                                        gj = gj + 80
                                        print("攻击力得到提升")
                                        pass
                                    if fy < 1500:
                                        fy = fy + 65
                                        print("防御力得到提升")
                                        pass
                                    if sm < 10000:
                                        sm = sm + 500
                                        print("生命值得到大幅提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("蘑菇魔王打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了蘑菇魔王")
                                            print("获得了2500个金币")
                                            jb = jb + 2500
                                            if gq == 8:
                                                gq = 9
                                                pass
                                            if gj < 2000:
                                                gj = gj + 80
                                                print("攻击力得到提升")
                                                pass
                                            if fy < 1500:
                                                fy = fy + 65
                                                print("防御力得到提升")
                                                pass
                                            if sm < 10000:
                                                sm = sm + 500
                                            print("生命值得到大幅提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第九关
                        elif p == 9:
                            print("------")
                            print("第九关")
                            print("------")
                            print("怪物名称:蘑菇大首领(超难)")
                            print("怪物血量:9000")
                            print("怪物攻击:1700")
                            print("怪物防御:1400")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 16600
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第九关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了蘑菇大首领")
                                    print("获得了5000个金币")
                                    jb = jb + 5000
                                    if gq == 9:
                                        gq = 10
                                        pass
                                    if gj < 5000:
                                        gj = gj + 200
                                        print("攻击力得到大幅提升")
                                        pass
                                    if fy < 3000:
                                        fy = fy + 150
                                        print("防御力得到大幅提升")
                                        pass
                                    if sm < 20000:
                                        sm = sm + 700
                                        print("生命值得到大幅提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("蘑菇大首领打败了你")
                                    print("------------------")
                                    if wdys > 0:
                                        print("是否使用无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 1
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了蘑菇大首领")
                                            print("获得了5000个金币")
                                            jb = jb + 5000
                                            if gq == 9:
                                                gq = 10
                                                pass
                                            if gj < 5000:
                                                gj = gj + 200
                                                print("攻击力得到大幅提升")
                                                pass
                                            if fy < 3000:
                                                fy = fy + 150
                                                print("防御力得到大幅提升")
                                                pass
                                            if sm < 20000:
                                                sm = sm + 700
                                            print("生命值得到大幅提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 第十关
                        elif p == 10:
                            print("------")
                            print("第十关")
                            print("------")
                            print("怪物名称:卢鑫(BOSS)")
                            print("怪物血量:19999")
                            print("怪物攻击:10000")
                            print("怪物防御:2000")
                            print("是否挑战此关卡")
                            print("[enter]是")
                            print("[0]否")
                            gwzdl = 37000
                            print("--------------")
                            o = clearInput()
                            if o == "":
                                print("------")
                                print("第十关")
                                print("------")
                                if zdl > gwzdl:
                                    # 奖励面板
                                    print("--------------------")
                                    print("你战胜了卢鑫！")
                                    print("获得了12000个金币")
                                    jb = jb + 12000
                                    if gq == 9:
                                        gq = 10
                                        pass
                                    if gj < 10000:
                                        gj = gj + 500
                                        print("攻击力得到大幅提升")
                                        pass
                                    if fy < 7000:
                                        fy = fy + 400
                                        print("防御力得到大幅提升")
                                        pass
                                    if sm < 100000:
                                        sm = sm + 2000
                                        print("生命值得到大幅提升")
                                        pass
                                    else:
                                        print("其他属性没有得到提升")
                                        print("--------------")
                                    print("输入任意回到关卡界面")
                                    print("--------------------")
                                    j = clearInput()
                                    pass
                                else:
                                    print("卢鑫毫不留情地打败了你")
                                    print("------------------")
                                    if wdys > 4:
                                        print("是否使用5瓶无敌药水")
                                        print("[enter]是 [0]否")
                                        n = clearInput()
                                        print("--------------")
                                        if n == "":
                                            print("使用成功")
                                            wdys = wdys - 5
                                            print("剩余无敌药水: %s" % (wdys))
                                            print("----------------")
                                            print("输入任意加载战斗结果")
                                            m = clearInput()
                                            print("--------------------")
                                            print("你战胜了卢鑫！")
                                            print("获得了12000个金币")
                                            jb = jb + 12000
                                            if gq == 10:
                                                gq = 11
                                                pass
                                            if gj < 10000:
                                                gj = gj + 500
                                                print("攻击力得到大幅提升")
                                                pass
                                            if fy < 7000:
                                                fy = fy + 400
                                                print("防御力得到大幅提升")
                                                pass
                                            if sm < 100000:
                                                sm = sm + 2000
                                            print("生命值得到大幅提升")
                                            print("输入任意回到关卡界面")
                                            print("--------------------")
                                            j = clearInput()
                                            pass
                                        elif n == "0":
                                            print("----------------")
                                            print("已取消使用")
                                            print("返回关卡页面成功")
                                            print("-----------------")
                                            pass
                                    else:
                                        print("提升属性再来吧")
                                        print("小提示:挑战之前的关卡可以提升属性")
                                        print("输入任意返回界面")
                                        print("--------------------")
                                        m = clearInput()
                                        pass
                            else:
                                print("----------------")
                                print("返回关卡界面成功")
                                print("----------------")
                                pass
                        # 关卡上限面板
                except:
                    print("--------------")
                    print("输入的关卡不合法")
                    print("输入任意继续")
                    print("--------------")
                    t = clearInput()
        # 状态面板
        elif x == "2":
            while True:
                print("=====================")
                print("角色面板")
                print("=====================")
                print("角色名: %s" % (name))
                print("生命值: %d" % (sm))
                print("攻击力: %d" % (gj))
                print("防御力: %d" % (fy))
                print("=====================")
                if jb<10000:
                    print("金币: %d" % (jb))
                if jb>=10000 and jb<100000000:
                    print("金币: %d万" % (jb//10000))
                if jb>=100000000 and jb<1000000000000:
                    print("金币: %d亿" % (jb // 100000000))
                if jb >= 1000000000000:
                    print("金币：超出显示长度")
                print("=====================")
                print("[1]无敌药水 :%d瓶" % (wdys))
                print("[0]返回首页")
                print("=====================")
                t = clearInput()
                if t == "1":
                    print("------------------------")
                    print("无敌药水: %d瓶" % (wdys))
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
            print("============================")
            print("商城")
            print("============================")
            print("你的金币: %s" % (jb))
            r = 0
            while r == 0:
                print("你的金币: %s" % jb)
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
                    if jb < 10000:
                        print("金币: %s" % (jb))
                    if jb >= 10000 and jb < 100000000:
                        print("金币: %s万" % (jb // 10000))
                    if jb >= 100000000 and jb < 1000000000000:
                        print("金币: %s亿" % (jb // 100000000))
                    if jb >= 1000000000000:
                        print("金币：超出显示长度")
                    print("无敌药水")
                    print("金币:20000")
                    print("属性:可以通过任何1~10关卡")
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
                                if jb >= 19999 * x:
                                    jb = jb - 20000 * x
                                    wdys = wdys + x
                                    print("------------")
                                    print("购买成功")
                                    if jb < 10000:
                                        print("剩余金币: %s" % (jb))
                                    if jb >= 10000 and jb < 100000000:
                                        print("剩余金币: %s万" % (jb // 10000))
                                    if jb >= 100000000 and jb < 1000000000000:
                                        print("剩余金币: %s亿" % (jb // 100000000))
                                    if jb >= 1000000000000:
                                        print("剩余金币：超出显示长度")
                                    print("无敌药水: %s瓶" % (wdys))
                                    print("输入任意返回界面")
                                    print("--------------")
                                    t = clearInput()
                                    pass
                                elif jb < 20000 * x:
                                    print("-------------------")
                                    print("你的金币不足")
                                    if jb < 10000:
                                        print("剩余金币: %s" % (jb))
                                    if jb >= 10000 and jb < 100000000:
                                        print("剩余金币: %s万" % (jb // 10000))
                                    if jb >= 100000000 and jb < 1000000000000:
                                        print("剩余金币: %s亿" % (jb // 100000000))
                                    if jb >= 1000000000000:
                                        print("剩余金币：超出显示长度")
                                    print("输入任意返回界面")
                                    print("-------------------")
                                    t = clearInput()
                            else:
                                print("-------------------")
                                print("输入错误正在返回首页")
                                print("-------------------")
                                backWait()
                        except:
                            print("-------------------")
                            print("输入错误正在返回首页")
                            print("-------------------")
                            backWait()
                    else:
                        backWait()
                        pass
                    pass
                # 满级药水
                elif f == "2":
                    print("---------------------")
                    print("满级药水")
                    print("金币:5000000")
                    print("你的金币: %s" % (jb))
                    print("属性:可以瞬间达到第十关最强状态")
                    print("是否选择购买")
                    print("[enter]是 [0]否")
                    print("---------------------")
                    g = clearInput()
                    if g == "":
                        if sm < 100000 or gj < 10000 or fy < 7000:
                            if jb > 4999999:
                                print("------------")
                                print("购买成功")
                                print("已自动使用成功")
                                jb = jb - 5000000
                                sm = 100000
                                gj = 10000
                                fy = 7000
                                if jb < 10000:
                                    print("金币: %s" % (jb))
                                if jb >= 10000 and jb < 100000000:
                                    print("金币: %s万" % (jb // 10000))
                                if jb >= 100000000 and jb < 1000000000000:
                                    print("金币: %s亿" % (jb // 100000000))
                                if jb >= 1000000000000:
                                    print("金币：超出显示长度")
                                print("目前属性:")
                                print("生命值:100000")
                                print("攻击力:10000")
                                print("防御力:7000")
                                print("输入任意返回界面")
                                print("--------------")
                                t = clearInput()
                            elif jb < 5000000:
                                print("---------------")
                                print("你的金币不足")
                                if jb < 10000:
                                    print("金币: %s" % (jb))
                                if jb >= 10000 and jb < 100000000:
                                    print("金币: %s万" % (jb // 10000))
                                if jb >= 100000000 and jb < 1000000000000:
                                    print("金币: %s亿" % (jb // 100000000))
                                if jb >= 1000000000000:
                                    print("金币：超出显示长度")
                                print("输入任意返回界面")
                                print("--------------")
                                t = clearInput()
                        else:
                            print("-----------------------------")
                            print("你的属性太高 这种药剂对你无效")
                            print("-----------------------------")
                    elif g == "0":
                        print("------------")
                        print("商城返回成功")
                        print("------------")
                        pass
                    pass
                # 改名卡
                elif f == "3":
                    print("---------------------")
                    print("改名卡")
                    print("金币:50000")
                    print("你的金币: %s" % (jb))
                    print("属性:给你一次修改名字的机会")
                    print("是否选择购买")
                    print("[enter]是 [0]否")
                    print("---------------------")
                    g = clearInput()
                    if g == "":
                        if jb > 49999:
                            print("------------")
                            print("购买成功")
                            if jb < 10000:
                                print("金币: %s" % (jb))
                            if jb >= 10000 and jb < 100000000:
                                print("金币: %s万" % (jb // 10000))
                            if jb >= 100000000 and jb < 1000000000000:
                                print("金币: %s亿" % (jb // 100000000))
                            if jb >= 1000000000000:
                                print("金币：超出显示长度")
                            print("请输入你的新角色名:")
                            print("---------------")
                            name = clearInput()
                            print("-----------------")
                            print("角色名修改完成")
                            jb = jb - 50000
                            print("输入任意返回界面")
                            print("--------------")
                            t = clearInput()
                        elif jb < 50000:
                            print("---------------")
                            print("你的金币不足")
                            if jb < 10000:
                                print("金币: %s" % (jb))
                            if jb >= 10000 and jb < 100000000:
                                print("金币: %s万" % (jb // 10000))
                            if jb >= 100000000 and jb < 1000000000000:
                                print("金币: %s亿" % (jb // 100000000))
                            if jb >= 1000000000000:
                                print("金币：超出显示长度")
                            print("输入任意返回界面")
                            print("--------------")
                            t = clearInput()
                    elif g == "0":
                        print("------------")
                        print("商城返回成功")
                        print("------------")
                        pass
                    pass
                # 属性加强药水
                elif f == "4":
                    print("---------------------")
                    print("瞬间满级药水1级")
                    print("金币:5000")
                    print("你的金币: %s" % (jb))
                    print("属性:增加生命1000攻击300防御200")
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
                                if jb > 4999 * x and sm < 100000 and gj < 10000 and fy < 7000:
                                    print("------------")
                                    print("购买成功")
                                    jb = jb - 5000 * x
                                    if jb < 10000:
                                        print("金币: %s" % (jb))
                                    if jb >= 10000 and jb < 100000000:
                                        print("金币: %s万" % (jb // 10000))
                                    if jb >= 100000000 and jb < 1000000000000:
                                        print("金币: %s亿" % (jb // 100000000))
                                    if jb >= 1000000000000:
                                        print("金币：超出显示长度")
                                    print("目前属性:")
                                    print("生命值:%s" % (sm + 1000 * x))
                                    print("攻击力:%s" % (gj + 300 * x))
                                    print("防御力:%s" % (fy + 200 * x))
                                    sm = sm + 1000 * x
                                    gj = gj + 300 * x
                                    fy = fy + 200 * fy
                                    print("输入任意返回界面")
                                    print("--------------")
                                    t = clearInput()
                                    pass
                                else:
                                    print("---------------")
                                    print("你的购买不合要求")
                                    print("输入任意返回界面")
                                    print("--------------")
                                    t = clearInput()
                            else:
                                backWait()
                        except:
                            backWait()
                    else:
                        backWait()
                # 查询无果面板
                else:
                    print("--------------")
                    print("目前没有该商品")
                    print("输入任意返回界面")
                    print("--------------")
                    t = clearInput()
                    pass
                pass
            pass
        # 退出面板
        elif x == "4":
            print("==============")
            print("请确定是否退出")
            print("[enter]是")
            print("[0]否")
            print("==============")
            q = clearInput()
            # 退出确定
            if q == "":
                print("--------------------")
                print("正在准备进行代码转换")
                print("代码转换进行中 请耐心等待")
                time.sleep(0.5)
                print("输入任意继续")
                print("--------------")
                # 代码转换器
                t = clearInput()
                # 代码输出器
                print("--------------------")
                print("存档已自动保存成功")
                print("--------------------")
                save(gj, fy, sm, gq, jb, wdys, name)
                time.sleep(0.4)
                z = z + 1
                os.system("cls")
            # 退出取消
            if q == "0":
                print("--------------")
                print("主页面返回成功")
                print("--------------")
                time.sleep(0.5)
                os.system("cls")
                pass
        # 充值面板
        elif x == "5" and chongZhi:
            while True:
                print("===================")
                print("充值面板")
                print("金币余额: %s" % (jb))
                print("请输入你要充值的金币数（1元等于1000金币）：)")
                print("[0]返回首页")
                print("===================")
                cz = clearInput()
                try:
                    cz = int(cz)
                    if cz == 0:
                        backWait()
                        break
                    elif cz < 0:
                        print("----------------")
                        print("无法充值负值金币")
                        print("输入任意返回界面")
                        print("----------------")
                        t = clearInput()
                    else:
                        print("----------------")
                        print("请输入你的手机号:")
                        print("----------------")
                        sjh = clearInput()
                        sjh = int(sjh)
                        if sjh > 10000000000 and sjh < 20000000000:
                            print("============================")
                            print("%s金币充值成功" % (cz))
                            hf = cz / 1000
                            print("话费扣除%s元成功" % (hf))
                            jb = jb + cz
                            print("金币余额: %s" % (jb))
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
                    backWait()
        # 输入任意重载主面板
        elif x== "*":
            while True:
                print("============================")
                print("设置")
                print("============================")
                print("[*]删除存档")
                print("[-]查看公告")
                print("[0]返回首页")
                print("============================")
                o=clearInput()
                if o =="*":
                    print("！请确认删除现有存档（无法恢复）")
                    print("[0]我再想想")
                    print("[1]是的我确认我要删除存档")
                    u=clearInput()
                    if u == "1":
                        print("！！！请再次确认删除现有存档（无法恢复）")
                        print("[0]我再想想")
                        print("[1]是的我确认我要删除存档")
                        u = clearInput()
                        if u == "1":
                            delete()
                            z-=1
                            break
                elif o == "0":
                    backWait()
                    break
                elif o =="-":
                    print("游戏名:林黛玉进贾府")
                    print("目前版本:v2.0.0")
                    print('''[1]更新clear界面
[2]更新本地存档加载，更新存档有关功能
[3]修复所有已发现导致崩溃的bug
[4]金币使用新的展示方式
[5]修改关卡的部分文字
[6]修复1.3.9商城无法购买的bug
[7]可以使用enter键直接进行下一步
[8]合并人物和背包为状态
[9]增加设置面板

即将添加的功能：
增加英雄副本和普通副本
存档文件升级
增加商场商品
增加宝箱功能抽奖功能
增加设置功能

''')
                    print("注意事项:")
                    print("[1]请认真阅读每条信息")
                    print("[2]最新关卡为[第十关]")
                    print("[3]游戏通过加载本地文档进行读档")
                    print("[4]需要python编程环境(你能打开说明你有)")
                    print("输入任意返回上层页面")
                    clearInput()
                    backWait()
                else:
                    backWait()
        else:
                print("--------------")
                print("重载主页面完成")
                print("--------------")
                time.sleep(0.5)
    # 感谢游玩面板
    while z == 3:
        print("------------")
        print("欢迎下次游玩")
        print("--------------")
        time.sleep(1)
        quit()
        z = z + 1
