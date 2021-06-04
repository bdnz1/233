'''
    猜数字：
    需求：
        1.猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
        2.键盘输入
            input("提示")
        3.循环
            while条件循环
            开始，结束，自增，任务
        4.判断
            if 判断条件  elif 判断条件.......else
    范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
# 1. 让系统产生一个随机数
num = random.randint(0,150)

# 开始输入您要猜的数。
i = 0
j=5000
f=0
while i < 20:
    # 任务：输入数据并比对数据
    number = input("请输入您要猜的数：")
    number = int(number)  # "56"  -->  56
    # 判断
    if number > num:
        print("大了！")
        j=j-500
        f=f+1
    elif number < num:
        print("小了！")
        j = j - 500
        f=f+1
    else:
        print("恭喜猜中！本次数字为：",num,"金币数量为",j)
        j=j+3000
        f=0
        # 跳出训话
        break # 跳出循环
    if f==15:
        print("系统已锁定")
        break
    if j==0:
        print("没金币了")
        break
    i= i + 1  # 每次加1








