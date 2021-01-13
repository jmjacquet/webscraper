import requests
import os

def getTotalGoals(team, year):	
	tot_goals=0
	for y in range(1,3):
		url=f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team{y}={team}"		
		resp = requests.get(url)
		if (resp.status_code == 200):
			data = resp.json() 
			tot_pages= data["total_pages"]
			for i in range(1,tot_pages+1):	    					
				url_pages=url+f'&page={i}'
				resp = requests.get(url_pages)
				data = resp.json() 
				matches = data["data"]
				tot_goals += sum([int(x[f"team{y}goals"]) for x in matches])
	return tot_goals



def getNumDraws(year):	
	tot_draws=0
	for y in range(0,11):
		url=f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={y}&team2goals={y}"		
		resp = requests.get(url)
		if (resp.status_code == 200):
			data = resp.json() 
			tot_draws+= int(data["total"])			
	return tot_draws	

if __name__ == '__main__':
    
    # team = input()

    # year = int(input().strip())

    #result = getTotalGoals("Chelsea", 2014)
    #result = getNumDraws(2011)
    # n = int(5)
    # arr = sorted(list(map(int,"57 57 -57 57".split())))
    # maximo = max(arr)
    # ant_max = max([x for x in arr if x<maximo])
    # print(ant_max)

	l=[]
	# for _ in range(int(input())):
	# 	name = input()
	# 	score = float(input())
	# 	l.append([name,score])
	# students = [['Harry', 37.21],['Berry', 37.21],['Tina', 37.2],['Akriti', 41],['Harsh', 39]]	
	# lista=sorted(students,key=lambda x: x[1])
	# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
	# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
	# print()

	# n = int(input())
	student_marks = {}
	# for _ in range(n):
	#     name, *line = input().split()
	#     scores = list(map(float, line))
	#     student_marks[name] = scores    
	# query_name = input()

	student_marks = {'Harsh': [25.0, 26.5, 28.0], 'Anurag': [26.0, 28.0, 30.0]}
	query_name = 'Harsh'
	prom=0
	scores = student_marks[query_name]
	if scores:
		prom = sum(scores)/len(scores)
	print("%.2f" % prom)




