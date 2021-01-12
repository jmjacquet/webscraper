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
    result = getNumDraws(2011)

