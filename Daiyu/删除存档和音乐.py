import shutil
import time

try:
    shutil.rmtree(r'C:\ProgramData\DaiyuLinGototheJiaHome')
    print('存档已删除')
except:
    print('存档不存在')

time.sleep(1.5)