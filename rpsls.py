#coding:gbk
#RPSLS即Rock-paper-scissors-lizard-Spock，石头剪刀布蜥蜴史波克,来源于“生活大爆炸Big bang”中谢耳朵自创。
#规则是：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克

print("剪刀裁剪纸,纸包裹石头,石头砸碎剪刀,石头砸死蜥蜴,蜥蜴毒死史波克")
print("rock=0 石头 spock=1 史波克 paper=2  布 lizard=3 蜥蜴 scissors= 4剪刀")
import random
def rpsls(guess):
	rock=0
	spock=1
	paper=2
	lizard=3
	scissors= 4
	def name_number(number):
		if number ==0:
			name=str("rock")
			return name
		elif number ==1:
			name =str("spock")
			return name
		elif number == 2:
			name = str("paper")
			return name
		elif number ==3:
			name = str("lizard")
			return name
		else:
			name = str("scissors")
			return name
	number=random.randint(0,4)
	computer=name_number(number)
	
	print("计算机的选择为%s"%computer)
	print("你的选择为%s"%guess)
	if ((computer ==str("rock") and (guess ==str("lizard") or guess ==str("lizard")))
		or (computer ==str("spock") and (guess ==str("rock") or guess ==str("scissors")))
		or (computer ==str("paper") and (guess ==str("rrock") or guess ==str("spock")))
		or (computer ==str("lizard") and (guess ==str("spock") or guess ==str("paper")))
		or (computer ==str("scissors") and (guess ==str("paper") or guess ==str("lizard")))):
			print("你输了")
	if ((computer == str("rock") and guess ==str("rock"))
		or (computer ==str("spock") and  guess ==str("spock"))
		or (computer == str("paper") and guess == str("paper"))
		or (computer ==str("lizard") and guess ==str("lizard"))
		or (computer ==str("scissors") and guess == str("scissors"))):
			print("跟计算机出的是一样的呢")
	else:
		print("你赢了")
print("请输入你的选择：rock,spock,paper,lizard,scissors")
guess=input("")
rpsls(guess)	
