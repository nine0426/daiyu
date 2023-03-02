w = 0
#说明面板
while w == 0:
  print("游戏名:林黛玉进贾府")
  print("目前版本:v1.3.9")
  print("(增加新商品,商城支持批量购买)")
  print("注意事项:")
  print("1.请认真阅读每条信息")
  print("2.在产生错误时请重载")
  print("3.最新关卡为[第十关]")
  print("4.输入字符会导致错误")
  print("5.游戏依靠记载六个代码重新读档")
  print("-------------------------------")
  print("看完说明后输入任意开始游戏")
  j = input()
  w = w+1
#游戏界面
while True:
  z = 1
  #游戏读档面板
  while z == 1:
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("--游戏界面--")
    print("输入任意开始加载代码")
    f = input()
    #管理员面板
    if f == "20030426":
      #提示面板1
      print("-----------------")
      print("已进入管理员面板")
      print("输入任意继续")
      print("--------------")
      t = input()
      #提示面板2
      print("-----------------------------------")
      print("请依次输入")
      print("攻击力防御力生命值金币关卡无敌药水")
      print("准备进行代码转换")
      print("输入任意查看说明")
      print("-----------------------------------")
      t = input()
      #代码限制面板
      print("-----------------")
      print("注意:")
      print("攻击力50~10000")
      print("防御力20~7000")
      print("生命值200~100000")
      print("关卡在1~10")
      print("金币没有上限")
      print("无敌药水没有上限")
      print("开始输入代码：")
      print("-----------------")
      #代码转换器
      gj = input()
      fy = input()
      sm = input()
      gq = input()
      jb = input()
      wdys = input()
      gj = int(gj)
      fy = int(fy)
      sm = int(sm)
      gq = int(gq)
      jb = int(jb)
      wdys = int(wdys)
      zdl = 2*gj+3*fy+sm
      a = (gj-7)/5
      b = (15-fy)/4
      c = (-sm)/4
      d = gq+40
      e = jb/50-1400
      f = wdys-34
      a = int(a)
      b = int(b)
      c = int(c)
      d = int(d)
      e = int(e)
      f = int(f)
      #代码输出器
      print("--------------------")
      print("代码转换完成")
      print("六个代码输出:")
      print("代码一:%s 代码二:%s 代码三:%s"%(a,b,c))
      print("代码四:%s 代码五:%s 代码六:%s"%(d,e,f))
      print("请复制代码后输入任意回到游戏界面")
      print("--------------------")
      j = input()
    #加载代码读档面板
    else :
      print("----------------------------")
      print("游戏正在载入")
      print("载入成功")
      print("请依次输入六个代码进行读档:")
      print("如果是第一次游玩请都输入0")
      print("----------------------------")
      #代码转换器
      a = input()
      b = input()
      c = input()
      d = input()
      e = input()
      f = input()
      a = int(a)
      b = int(b)
      c = int(c)
      d = int(d)
      e = int(e)
      f = int(f)
      gj = 5*a+7
      fy = 15-4*b
      sm = -4*c
      gq = d-40
      zdl = 2*gj+3*fy+sm
      jb = (e+1400)*50
      wdys = 34+f
      gj = int(gj)
      fy = int(fy)
      sm = int(sm)
      gq = int(gq)
      jb = int(jb)
      wdys = int(wdys)
      #新玩家判定器
      if a+b+c+d+e+f==0:
        print("----------------------")
        print("欢迎你第一次游玩本游戏")
        print("请输入你的角色名:")
        print("----------------------")
        name = input()
        print("--------------")
        print("欢迎你进入游戏")
        gj = 50
        fy = 20
        sm = 200
        zdl = 2*gj+3*fy+sm
        jb = 0
        gq = 1
        wdys = 0
        z = z+1
      #防作弊代码错误判定器
      elif gj<38:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif fy<13:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif sm<154:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif gq<1:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif gj>10800:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif fy>7500:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif sm>103000:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif gq>10:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      elif wdys<0:
        print("--------------")
        print("代码输入错误")
        print("--------------")
      else:
        print("------------")
        print("代码加载成功")
        print("代码成功转为存档数据")
        print("------------")
        print("请输入你的角色名:")
        print("--------------")
        name = input()
        z = z+1
  #游戏面板
  while z == 2:
    #游戏主页面
    zdl = 2*gj+3*fy+sm
    print("--------------")
    print("----主界面----")
    print("--------------")
    print("1.关卡")
    print("2.角色")
    print("3.背包")
    print("4.商城")
    print("5.充值")
    print("6.退出")
    #菜单选择面板
    x = input()
    #关卡面板
    if x == "1":
      print("----")
      print("关卡")
      print("----")
      l = 0
      #关卡面板
      while l == 0:
        zdl = 2*gj+3*fy+sm
        print("-------------------------------")
        print("目前你已解锁最新关卡为: %s/10"%(gq))
        print("精英关卡暂未开启 0/0")
        print("-------------------------------")
        #关卡选择器
        print("请输入你要挑战的关卡数:")
        print("输入0返回界面")
        print("-------------------------------")
        p = input()
        p = int(p)
        #关卡判定器
        if p>gq:
          print("--------------")
          print("当前关卡未解锁")
          print("输入任意继续")
          print("--------------")
          t = input()
        elif p<0:
          print("暂时没有负关")
        #返回系统
        elif p==0:
          l = 1
          print("------------")
          print("界面返回成功")
          print("------------")
        #第一关
        elif p==1:
          print("------")
          print("第一关")
          print("------")
          print("怪物名称:小哥布林(简单)")
          print("怪物血量:50")
          print("怪物攻击:10")
          print("怪物防御:5")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          print("--------------")
          o =input()
          if o=="1":
            print("--------------")
            print("第一关")
            print("--------------")
            if gq == 1:
              gq = 2
            print("你战胜了小哥布林")
            print("获得了十个金币")
            jb = jb+10
            if gj<80:
              gj=gj+2
              print("攻击力得到小幅提升")
            if fy<40:
              fy=fy+1
              print("防御力得到小幅提升")
            if sm<250:
              sm=sm+4
              print("生命值得到小幅提升")
            else:
              print("其他属性没有得到提升")
              print("--------------")
            print("输入任意返回关卡界面")
            print("--------------")
            t = input()
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
        #第二关
        elif p==2:
          print("------")
          print("第二关")
          print("------")
          print("怪物名称:大哥布林(简单)")
          print("怪物血量:200")
          print("怪物攻击:50")
          print("怪物防御:20")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          print("--------------")
          o =input()
          if o=="1":
            print("--------------")
            print("第二关")
            print("--------------")
            print("你战胜了大哥布林")
            print("获得了20个金币")
            jb = jb+20
            if gq == 2:
              gq=3
            if gj<120:
              gj=gj+3
              print("攻击力得到小幅提升")
            if fy<80:
              fy=fy+2
              print("防御力得到小幅提升")
            if sm<400:
              sm=sm+7
              print("生命值得到小幅提升")
            else:
              print("其他属性没有得到提升")
            print("输入任意回到关卡界面")
            print("--------------------")
            j = input()
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
        #第三关
        elif p==3:
          print("------")
          print("第三关")
          print("------")
          print("怪物名称:哥布林首领(中等)")
          print("怪物血量:300")
          print("怪物攻击:100")
          print("怪物防御:60")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 980
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第三关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了哥布林首领")
              print("获得了100个金币")
              jb = jb+100
              if gq == 3:
                gq = 4
                pass
              if gj<300:
                gj=gj+5
                print("攻击力得到提升")
                pass
              if fy<200:
                fy=fy+4
                print("防御力得到提升")
                pass
              if sm<1000:
                sm=sm+12
                print("生命值得到提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("哥布林首领打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了哥布林首领")
                  print("获得了100个金币")
                  jb = jb+100
                  if gq == 3:
                    gq = 4
                    pass
                  if gj<300:
                    gj=gj+5
                    print("攻击力得到提升") 
                    pass
                  if fy<200:
                    fy=fy+4
                    print("防御力得到提升")
                    pass
                  if sm<1000:
                    sm=sm+12
                    print("生命值得到提升")
                    pass
                  else:
                    print("属性没有得到提升")
                    print("--------------")
                    pass
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第四关
        elif p==4:
          print("------")
          print("第四关")
          print("------")
          print("怪物名称:哥布林司令官(困难)")
          print("怪物血量:800")
          print("怪物攻击:300")
          print("怪物防御:150")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 1850
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第四关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了哥布林司令官")
              print("获得了500个金币")
              jb = jb+500
              if gq == 4:
                gq = 5
                pass
              if gj<500:
                gj=gj+10
                print("攻击力得到提升")
                pass
              if fy<300:
                fy=fy+7
                print("防御力得到提升")
                pass
              if sm<1500:
                sm=sm+50
                print("生命值得到提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("哥布林司令官打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了哥布林司令官")
                  print("获得了500个金币")
                  jb = jb+500
                  if gq == 4:
                    gq = 5
                    pass
                  if gj<500:
                    gj=gj+10
                    print("攻击力得到提升")
                    pass
                  if fy<300:
                    fy=fy+7
                    print("防御力得到提升")
                    pass
                  if sm<1500:
                    sm=sm+50
                  print("生命值得到提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第五关
        elif p==5:
          print("------")
          print("第五关")
          print("------")
          print("怪物名称:蘑菇兵(简单)")
          print("怪物血量:500")
          print("怪物攻击:200")
          print("怪物防御:150")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 1200
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第四关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了蘑菇兵")
              print("获得了400个金币")
              jb = jb+400
              if gq == 5:
                gq = 6
                pass
              if gj<800:
                gj=gj+20
                print("攻击力得到提升")
                pass
              if fy<500:
                fy=fy+20
                print("防御力得到提升")
                pass
              if sm<2000:
                sm=sm+50
                print("生命值得到提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("蘑菇兵打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了蘑菇兵")
                  print("获得了400个金币")
                  jb = jb+400
                  if gq == 5:
                    gq = 6
                    pass
                  if gj<800:
                    gj=gj+30
                    print("攻击力得到提升")
                    pass
                  if fy<500:
                    fy=fy+20
                    print("防御力得到提升")
                    pass
                  if sm<2000:
                    sm=sm+50
                  print("生命值得到提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第六关
        elif p==6:
          print("------")
          print("第六关")
          print("------")
          print("怪物名称:蘑菇队长(中等)")
          print("怪物血量:900")
          print("怪物攻击:350")
          print("怪物防御:200")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 2200
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第四关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了蘑菇兵")
              print("获得了800个金币")
              jb = jb+800
              if gq == 6:
                gq = 7
                pass
              if gj<1000:
                gj=gj+50
                print("攻击力得到提升")
                pass
              if fy<700:
                fy=fy+30
                print("防御力得到提升")
                pass
              if sm<3000:
                sm=sm+150
                print("生命值得到提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("蘑菇队长打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了蘑菇队长")
                  print("获得了800个金币")
                  jb = jb+800
                  if gq == 6:
                    gq = 7
                    pass
                  if gj<1000:
                    gj=gj+50
                    print("攻击力得到提升")
                    pass
                  if fy<700:
                    fy=fy+30
                    print("防御力得到提升")
                    pass
                  if sm<2000:
                    sm=sm+150
                  print("生命值得到提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第七关
        elif p==7:
          print("------")
          print("第七关")
          print("------")
          print("怪物名称:蘑菇法师(困难)")
          print("怪物血量:2500")
          print("怪物攻击:600")
          print("怪物防御:400")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 4900
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第七关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了蘑菇法师")
              print("获得了1500个金币")
              jb = jb+1500
              if gq == 7:
                gq = 8
                pass
              if gj<1500:
                gj=gj+70
                print("攻击力得到提升")
                pass
              if fy<1000:
                fy=fy+50
                print("防御力得到提升")
                pass
              if sm<5000:
                sm=sm+200
                print("生命值得到提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("蘑菇法师打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了蘑菇法师")
                  print("获得了1500个金币")
                  jb = jb+1500
                  if gq == 7:
                    gq = 8
                    pass
                  if gj<1500:
                    gj=gj+50
                    print("攻击力得到提升")
                    pass
                  if fy<1000:
                    fy=fy+50
                    print("防御力得到提升")
                    pass
                  if sm<5000:
                    sm=sm+200
                  print("生命值得到提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第八关
        elif p==8:
          print("------")
          print("第八关")
          print("------")
          print("怪物名称:蘑菇魔王(困难)")
          print("怪物血量:4000")
          print("怪物攻击:1000")
          print("怪物防御:800")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 8400
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第八关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了蘑菇魔王")
              print("获得了2500个金币")
              jb = jb+2500
              if gq == 8:
                gq = 9
                pass
              if gj<2000:
                gj=gj+80
                print("攻击力得到提升")
                pass
              if fy<1500:
                fy=fy+65
                print("防御力得到提升")
                pass
              if sm<10000:
                sm=sm+500
                print("生命值得到大幅提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("蘑菇魔王打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了蘑菇魔王")
                  print("获得了2500个金币")
                  jb = jb+2500
                  if gq == 8:
                    gq = 9
                    pass
                  if gj<2000:
                    gj=gj+80
                    print("攻击力得到提升")
                    pass
                  if fy<1500:
                    fy=fy+65
                    print("防御力得到提升")
                    pass
                  if sm<10000:
                    sm=sm+500
                  print("生命值得到大幅提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第九关
        elif p==9:
          print("------")
          print("第九关")
          print("------")
          print("怪物名称:蘑菇大首领(超难)")
          print("怪物血量:9000")
          print("怪物攻击:1700")
          print("怪物防御:1400")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 16600
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第九关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了蘑菇大首领")
              print("获得了5000个金币")
              jb = jb+5000
              if gq == 9:
                gq = 10
                pass
              if gj<5000:
                gj=gj+200
                print("攻击力得到大幅提升")
                pass
              if fy<3000:
                fy=fy+150
                print("防御力得到大幅提升")
                pass
              if sm<20000:
                sm=sm+700
                print("生命值得到大幅提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("蘑菇大首领打败了你")
              print("------------------")
              if wdys>0:
                print("是否使用无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-1
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了蘑菇大首领")
                  print("获得了5000个金币")
                  jb = jb+5000
                  if gq == 9:
                    gq = 10
                    pass
                  if gj<5000:
                    gj=gj+200
                    print("攻击力得到大幅提升")
                    pass
                  if fy<3000:
                    fy=fy+150
                    print("防御力得到大幅提升")
                    pass
                  if sm<20000:
                    sm=sm+700
                  print("生命值得到大幅提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #第十关
        elif p==10:
          print("------")
          print("第十关")
          print("------")
          print("怪物名称:卢鑫(BOSS)")
          print("怪物血量:19999")
          print("怪物攻击:10000")
          print("怪物防御:2000")
          print("是否攻击此关卡")
          print("1.是")
          print("0.不是")
          gwzdl = 37000
          print("--------------")
          o =input()
          if o=="1":
            print("------")
            print("第十关")
            print("------")
            if zdl>gwzdl:
              #奖励面板
              print("--------------------")
              print("你战胜了卢鑫！")
              print("获得了12000个金币")
              jb = jb+12000
              if gq == 9:
                gq = 10
                pass
              if gj<10000:
                gj=gj+500
                print("攻击力得到大幅提升")
                pass
              if fy<7000:
                fy=fy+400
                print("防御力得到大幅提升")
                pass
              if sm<100000:
                sm=sm+2000
                print("生命值得到大幅提升")
                pass
              else:
                print("其他属性没有得到提升")
                print("--------------")
              print("输入任意回到关卡界面")
              print("--------------------")
              j = input()
              pass
            else:
              print("卢鑫毫不留情地打败了你")
              print("------------------")
              if wdys>4:
                print("是否使用5瓶无敌药水(请谨慎使用)")
                print("1.是 0.否")
                n = input()
                print("--------------")
                if n == "1":
                  print("使用成功")
                  wdys=wdys-5
                  print("剩余无敌药水: %s"%(wdys))
                  print("----------------")
                  print("输入任意加载战斗结果")
                  m = input()
                  print("--------------------")
                  print("你战胜了卢鑫！")
                  print("获得了12000个金币")
                  jb = jb+12000
                  if gq == 10:
                    gq = 11
                    pass
                  if gj<10000:
                    gj=gj+500
                    print("攻击力得到大幅提升")
                    pass
                  if fy<7000:
                    fy=fy+400
                    print("防御力得到大幅提升")
                    pass
                  if sm<100000:
                    sm=sm+2000
                  print("生命值得到大幅提升")
                  print("输入任意回到关卡界面")
                  print("--------------------")
                  j = input()
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
                m = input()
                pass
          else:
            print("----------------")
            print("返回关卡界面成功")
            print("----------------")
            pass
        #关卡上限面板
        if p>10:
          print("--------------")
          print("目前只有10关可以挑战")
          print("请等待后续更新")
          print("输入任意继续")
          print("--------------")
          t = input()
          pass
        pass
    #角色面板
    elif x == "2":
      print("角色面板")
      print("--------")
      print("角色名: %s"%(name))
      print("生命值: %s"%(sm))
      print("攻击力: %s"%(gj))
      print("防御力: %s"%(fy))
      print("----------")
      print("金币: %s"%(jb))
      print("输入任意返回界面")
      print("--------------")
      t = input()
      pass
    #背包面板
    elif x == "3":
      k = 0
      while k == 0:
        print("--------")
        print("背包")
        print("--------")
        print("------------------------")
        if wdys>0:
          print("1.无敌药水 :%s瓶"%(wdys))
          print("输入序号可以使用")
        else:
          print("你的背包空空如也")
        print("输入0返回界面")
        print("------------------------")
        t = input()
        if t == "0":
          k = 1
        elif t == "1":
            print("------------------------")
            print("无敌药水: %s瓶"%(wdys))
            print("在关卡无法闯过可以使用")
            print("输入任意返回界面")
            print("------------------------")
            t = input()
            pass
    #商城面板
    elif x == "4":
      print("------")
      print("商城")
      print("------")
      print("------------------------")
      print("你的金币: %s"%(jb))
      r = 0
      while r == 0:
        print("你的金币: %s"%(jb))
        print("目前商品:")
        print("1.无敌药水")
        print("2.瞬间满级药水1级")
        print("3.改名卡")
        print("4.属性加强药水1级")
        print("--请输入商品序号选择购买--")
        print("--输入0返回界面--")
        print("------------------------")
        f =input()
        #返回面板
        if f == "0":
          print("--------------")
          print("主页面返回成功")
          print("--------------")
          r = r+1
          pass
        #无敌药水
        elif f == "1":
          print("---------------------")
          print("你的金币: %s"%(jb))
          print("无敌药水")
          print("金币:20000")
          print("属性:可以通过任何1~9关卡(第十关需要5瓶)")
          print("是否选择购买")
          print("1.是 0.否")
          print("---------------------")
          g = input()
          if g == "1":
            print("---------------------")
            print("请输入你要购买的数量:")
            print("---------------------")
            x = input()
            x = int()
            if x>0:
              if jb>19999*x:
                print("------------")
                print("购买成功")
                jb = jb-20000*x
                wdys = wdys+x
                print("剩余金币: %s"%(jb))
                print("无敌药水: %s瓶"%(wdys))
                print("输入任意返回界面")
                print("--------------")
                t = input()
                pass
              elif jb<20000*x:
                print("---------------")
                print("你的金币不足")
                print("金币余额: %s"%(jb))
                print("输入任意返回界面")
                print("--------------")
                t = input()
          elif g == "0":
            print("------------")
            print("商城返回成功")
            print("------------")
            pass
          pass
        #超级强力药水1级
        elif f == "2":
          print("---------------------")
          print("超级强力药水1级")
          print("金币:5000000")
          print("你的金币: %s"%(jb))
          print("属性:可以瞬间达到第十关最强状态")
          print("是否选择购买")
          print("1.是 0.否")
          print("---------------------")
          g = input()
          if g == "1":
            if sm<100000 or gj<10000 or fy<7000:
              if jb>4999999:
                print("------------")
                print("购买成功")
                print("已自动使用成功")
                jb = jb-5000000
                sm = 100000
                gj = 10000
                fy = 7000
                print("剩余金币: %s"%(jb))
                print("目前属性:")
                print("生命值:100000")
                print("攻击力:10000")
                print("防御力:7000")
                print("输入任意返回界面")
                print("--------------")
                t = input()
              elif jb<5000000:
                print("---------------")
                print("你的金币不足")
                print("金币余额: %s"%(jb))
                print("输入任意返回界面")
                print("--------------")
                t = input()
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
        #改名卡
        elif f == "3":
          print("---------------------")
          print("改名卡")
          print("金币:50000")
          print("你的金币: %s"%(jb))
          print("属性:给你一次修改名字的机会")
          print("是否选择购买")
          print("1.是 0.否")
          print("---------------------")
          g = input()
          if g == "1":
            if jb>49999:
              print("------------")
              print("购买成功")
              print("剩余金币: %s"%(jb))
              print("请输入你的新角色名:")
              print("---------------")
              name = input()
              print("-----------------")
              print("角色名修改完成")
              jb = jb-50000
              print("输入任意返回界面")
              print("--------------")
              t = input()
            elif jb<50000:
              print("---------------")
              print("你的金币不足")
              print("金币余额: %s"%(jb))
              print("输入任意返回界面")
              print("--------------")
              t = input()
          elif g == "0":
            print("------------")
            print("商城返回成功")
            print("------------")
            pass
          pass
        #属性加强药水1级
        elif f == "2":
          print("---------------------")
          print("瞬间满级药水1级")
          print("金币:5000")
          print("你的金币: %s"%(jb))
          print("属性:增加生命1000攻击300防御200")
          print("是否选择购买")
          print("1.是 0.否")
          print("---------------------")
          g = input()
          if g == "1":
            print("---------------------")
            print("请输入你要购买的数量:")
            print("---------------------")
            x = input()
            x = int()
            if x>0:
              if jb>4999*x:
                print("------------")
                print("购买成功")
                jb = jb-5000*x
                print("剩余金币: %s"%(jb))
                print("目前属性:")
                print("生命值:%s"%(sm+1000*x))
                print("攻击力:%s"%(gj+300*x))
                print("防御力:%s"%(fy+200*x))
                sm = sm+1000*x
                gj = gj+300*x
                fy = fy+200*fy
                print("输入任意返回界面")
                print("--------------")
                t = input()
                pass
              else:
                print("---------------")
                print("你的金币不足")
                print("金币余额: %s"%(jb))
                print("输入任意返回界面")
                print("--------------")
                t = input()
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
        #查询无果面板
        else:
          print("--------------")
          print("目前没有该商品")
          print("--------------")
          print("输入任意返回界面")
          print("--------------")
          t = input()
          pass
        pass
      pass
    #充值面板
    elif x == "5":
      h = 0
      while h == 0:
        print("--------------")
        print("充值面板")
        print("金币余额: %s"%(jb))
        print("请输入你要充值的金币数")
        print("1元等于1000金币")
        print("输入0返回界面")
        print("--------------")
        cz = input()
        cz = int(cz)
        if cz == 0:
          h = h+1
        elif cz<0:
          print("----------------")
          print("无法充值负值金币")
          print("输入任意返回界面")
          print("----------------")
          t = input()
        else:
          print("----------------")
          print("请输入你的手机号:")
          print("----------------")
          sjh = input()
          sjh = int(sjh)
          if sjh>10000000000 and sjh<20000000000:
            print("----------------")
            print("%s金币充值成功"%(cz))
            hf = cz/1000
            print("话费扣除%s元成功"%(hf))
            jb = jb+cz
            print("金币余额: %s"%(jb))
            print("----------------")
            print("输入任意返回界面")
            print("--------------")
            t = input()
          else:
            print("----------------")
            print("手机号码输入错误")
            print("充值失败")
            print("输入任意返回界面")
            print("----------------")
            t = input()
    #退出面板
    elif x == "6":
      print("--------------------")
      print("请确定是否退出")
      print("1.是")
      print("0.不是")
      print("--------------")
      q = input()
      #退出确定
      if q == "1":
        print("--------------------")
        print("存档保存完成")
        print("正在准备进行代码转换")
        print("代码转换进行中 请耐心等待")
        print("--------------")
        print("输入任意继续")
        print("--------------")
        #代码转换器
        t = input()
        zdl = 2*gj+3*fy+sm
        a = (gj-7)/5
        b = (15-fy)/4
        c = (-sm)/4
        d = gq+40
        e = jb/50-1400
        f = wdys-34
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        #代码输出器
        print("--------------------")
        print("代码转换完成")
        print("六个代码输出:")
        print("代码一:%s 代码二:%s 代码三:%s"%(a,b,c))
        print("代码四:%s 代码五:%s 代码六:%s"%(d,e,f))
        print("请复制代码后输入任意退出游戏")
        print("--------------------")
        j = input()
        z = z+1
        pass
      #退出取消
      if q == "0":
        print("--------------")
        print("主页面返回成功")
        print("--------------")
        pass
      pass
    #输入任意重载主面板
    else:
      print("--------------")
      print("重载主页面完成")
      print("输入任意返回界面")
      print("--------------")
      t = input()
      pass
    pass
  #感谢游玩面板
  while z == 3:
    print("------------")
    print("欢迎下次游玩")
    print("输入任意返回界面")
    print("--------------")
    t = input()
    z = z+1
    pass