#coding:gbk
#RPSLS��Rock-paper-scissors-lizard-Spock��ʯͷ����������ʷ����,��Դ�ڡ������ըBig bang����л�����Դ���
#�����ǣ������ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ����

print("�����ü�ֽ,ֽ����ʯͷ,ʯͷ�������,ʯͷ��������,���涾��ʷ����")
print("rock=0 ʯͷ spock=1 ʷ���� paper=2  �� lizard=3 ���� scissors= 4����")
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
	
	print("�������ѡ��Ϊ%s"%computer)
	print("���ѡ��Ϊ%s"%guess)
	if ((computer ==str("rock") and (guess ==str("lizard") or guess ==str("lizard")))
		or (computer ==str("spock") and (guess ==str("rock") or guess ==str("scissors")))
		or (computer ==str("paper") and (guess ==str("rrock") or guess ==str("spock")))
		or (computer ==str("lizard") and (guess ==str("spock") or guess ==str("paper")))
		or (computer ==str("scissors") and (guess ==str("paper") or guess ==str("lizard")))):
			print("������")
	if ((computer == str("rock") and guess ==str("rock"))
		or (computer ==str("spock") and  guess ==str("spock"))
		or (computer == str("paper") and guess == str("paper"))
		or (computer ==str("lizard") and guess ==str("lizard"))
		or (computer ==str("scissors") and guess == str("scissors"))):
			print("�������������һ������")
	else:
		print("��Ӯ��")
print("���������ѡ��rock,spock,paper,lizard,scissors")
guess=input("")
rpsls(guess)	
