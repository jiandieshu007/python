#coding:gbk
#RPSLS��Rock-paper-scissors-lizard-Spock��ʯͷ����������ʷ����,��Դ�ڡ������ըBig bang����л�����Դ���
#�����ǣ������ü�ֽ��ֽ����ʯͷ��ʯͷ���������ʯͷ�������棻���涾��ʷ����

print("�����ü�ֽ,ֽ����ʯͷ,ʯͷ�������,ʯͷ��������,���涾��ʷ����")
print("rock=0 ʯͷ spock=1 ʷ���� paper=2  �� lizard=3 ���� scissors= 4����")
import random
def rpsls(guess):
	rock = 0 #ʯͷ
	spock = 1 # ʷ���� 
	paper = 2 # ��
	lizard = 3  # ����
	scissors = 4 # ����
	computer =random.randint(0,4)
	if ((computer ==0 and (guess ==3 or guess ==4))
		or (computer ==1 and (guess ==0 or guess ==4))
		or (computer ==2 and (guess ==0 or guess ==3))
		or (computer ==3 and (guess ==1 or guess ==2))
		or (computer ==4 and (guess ==2 or guess ==3))):
			print("���ѡ��Ϊ:%d"%guess)
			print("���Ե�ѡ��Ϊ:%s"%coomputer)
			print("������")
	if ((computer == 0 and guess ==0)
		or (computer ==1 and  guess ==1)
		or (computer == 2 and guess == 2)
		or (computer ==3 and guess ==3)
		or (computer ==4 and guess == 4)):
			print("�������������һ������")
	else:
		print("���ѡ���ǣ�%s"%guess)
		print("���Ե�ѡ���ǣ�%s"%computer)
		print("��Ӯ��")

guess=input("���������ѡ��rock,spock,paper,lizard,scissors")
rpsls(guess)	
