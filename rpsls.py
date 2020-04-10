#coding:gbk
#RPSLS即Rock-paper-scissors-lizard-Spock，石头剪刀布蜥蜴史波克,来源于“生活大爆炸Big bang”中谢耳朵自创。
#规则是：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克

print("剪刀裁剪纸,纸包裹石头,石头砸碎剪刀,石头砸死蜥蜴,蜥蜴毒死史波克")
print("rock=0 石头 spock=1 史波克 paper=2  布 lizard=3 蜥蜴 scissors= 4剪刀")
import random
def rpsls(guess):
	rock = 0 #石头
	spock = 1 # 史波克 
	paper = 2 # 布
	lizard = 3  # 蜥蜴
	scissors = 4 # 剪刀
	computer =random.randint(0,4)
	if ((computer ==0 and (guess ==3 or guess ==4))
		or (computer ==1 and (guess ==0 or guess ==4))
		or (computer ==2 and (guess ==0 or guess ==3))
		or (computer ==3 and (guess ==1 or guess ==2))
		or (computer ==4 and (guess ==2 or guess ==3))):
			print("你的选择为:%d"%guess)
			print("电脑的选择为:%s"%coomputer)
			print("你输了")
	if ((computer == 0 and guess ==0)
		or (computer ==1 and  guess ==1)
		or (computer == 2 and guess == 2)
		or (computer ==3 and guess ==3)
		or (computer ==4 and guess == 4)):
			print("跟计算机出的是一样的呢")
	else:
		print("你的选择是：%s"%guess)
		print("电脑的选择是：%s"%computer)
		print("你赢了")

guess=input("请输入你的选择：rock,spock,paper,lizard,scissors")
rpsls(guess)	
