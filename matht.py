#-*- coding:utf-8 -*-

import random	# 난수 생성 라이브러리 호출
import time		# 시간을 재는 라이브러리 호출
import os, sys	# 시스템 명령어를 수행하는 라이브러리 호출
s1 = time.time()	# 처음 시작 시간을 체크 하여 변수로 저장 한다.
n = 0		# 문제 번호를 기억할 변수를 지정한다.
win = 0	# 정답 횟수를 기억할 변수를 지정한다.
lose = 0 	# 틀린 횟수를 기억할 변수를 지정한다.
def math_teacher():	# 문제를 발생 시킬 인공지능 함수를 설계
	a = random.randint(1, 3)		# 기호를 랜덤으로 발생 시킬 변수
	b = random.randint(1, 100)	# 계산식 필드 1을 1~100 까지의 난수로 발생 시킬 변수
	c = random.randint(1, 100)	# 계산식 필드 2을 1~100 까지의 난수로 발생 시킬 변수
	
	q = str(b) 				# 전체 함수를 변수 q로 사용 할수 있도록 변수 b부터 시작하며 b를 문자열로 전환한다. 
	if a == 3:
		q = q + "*"			# a 변수가 3일 경우 곱하기 발생
	if a == 1:
		q = q + "+"			# a 변수가 1 일 경우 더하기 발생
	if a == 2:
		q = q + "-"			# a 변수가 2 일 경우 빼기 발생
	q = q + str(c)
	return q				# 함수에서 q변수를 외부에서 응용 할수 있도록 반환 한다.

os.system('clear')			# 콘솔화면을 정리하는 쉘 명령 실행

for i in xrange(10):			# 10번을 수행하는 지정 루프를 수행 
	n = n + 1				# 변수 n(문제 번호)에 1을 추가
	qu = "문제 "
	qup = "(*)는 곱하기 입니다."
	que = str(qu) + str(n)
	print(qup)
	print(que)
	print("")
	q = math_teacher()		# 변수 q에 math_teacher()함수를 지정
	print(q)				
	print("")
	print("정답을 입력 하세요.")		
	inp = input("∴ ")
	inp = int(inp)			# 입력을 받은 숫자를 정수로 변환한다.
	os.system('clear')
	if eval(q) == inp:		# 'eval' 지정 함수는 문자열을 파이썬 프로세스가 계산할수 있도록 해 주며 사용자 입력값이 틀린지 프로세스가 판단  
		print("이전 문제 정답!")	# 정답일 경우 
		win = win + 1
	else:					# 틀릴 경우
		print("이전 문제 틀림!")	
		lose = lose + 1
		eq = eval(q)
		eq = str(eq)
		print("이전 문제 정답 =" + eq)
	wi = str(win)
	lo = str(lose)
	print("현재 점수는 정답: " + wi + "개, 틀린답 " + lo + "개")
s2 = time.time()		# 문제 풀이가 전부 끝나고 끝난 시간을 체크

st = s2-s1			# 끝난 시간 - 시작 시간을 계산

stst = str(st)		

print("문제를 전부 푼 시간은" + stst + "초 이며")

end = win*10		# 점수 계산을 수행 

endt = str(end)
print("당신의 점수는 " + endt + "입니다.")
