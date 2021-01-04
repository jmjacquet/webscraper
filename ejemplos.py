# lista = [(1,2),(11,2),(4,55),(5,6),{'hola':"chau"}]


# add10 = lambda x,y,z: x*y+10-z

# import logging

# log = logging.getLogger(__name__)



# # try:
# #     l=lista[9]
# # except Exception as e:
# #     log.error(e,exc_info=True)


# import json
# d = dict(nombre="juanma",apellido="jacquet",edad=38)
# d2 = {v:(x.capitalize() if isinstance(x,str) else x) for (v,x) in d.items()}
# lista_json = json.dumps(d2,indent=4,sort_keys=True)
# print(lista_json)

# numbers = [1, 12, 37, 43, 51, 62, 83, 43, 90, 2020]
# lista = [ x for x in numbers if ((x%2==1))]
# #print(lista)


# leaders = {4: "Yang Zhou", 2: "Elon Musk", 3: "Tim Cook", 1: "Warren Buffett"}
# leaders = dict(sorted(leaders.items(),key= lambda x: x[0],reverse=True))
# print(leaders)



# def solution(A):
# 	n=len(A)
# 	#If zero elements returns -1
# 	if n==0:
# 		return (-1)

# 	res = []
# 	for i in range(n):		
# 		left_A = sum([x for x in A[:i] if i>0])
# 		right_A = sum([x for x in A[i+1:] if i<n])
# 		if left_A==right_A:
# 			res.append(i)

# 	if len(res)>0:
# 		return ([{x:A[x]} for x in res])		
# 	else:
# 		return (-1)


# def solution(A):
#     # write your code in Python 3.6
    
#     minimo=1
#     maximo=max(A)
#     if maximo<=0:
#     	return 1
#     lista_bien = set(range(minimo,maximo+2))
#     A=set(A)
#     l = lista_bien - A
#     if len(l)==0:
#     	return maximo+1
#     return min(l)

# def solution(A):
#   temp = str(A)
#   ans = float('-inf')
#   for i in range(len(temp) + 1):
#      cand = temp[:i] + '5' + temp[i:]
#      if i == 0 and temp[0] == '-':
#         continue
#      ans = max(ans, int(cand))
#   return ans



# print(solution(826))

import json

if __name__ == '__main__':

	a="arrb6???4xxbl5???eee5"
	b="acc?7??sss?3rr1??????5"
	c="5??aaaaaaaaaaaaaaaaaaa?5?5"
	d="9???1???9???1???9"
	e="aa6?9"

	def is_pair(n):
		try:
			n=int(n)
			return (n%2==0)
		except:
			return False
		

	def existe(a):
		words=a.split('???')
		cant=len(words)
		result=False
		for i,w in enumerate(words):
			
			if i==0:
				continue
			elif i < cant:
				ant=words[i-1][-1]
				pos=words[i][0]				
				if is_pair(ant) and is_pair(pos):
					return True
		return result
	
	print(existe(a))


	#print(words)



    
    # print('Welcome to the birthday dictionary. We know the birthdays of:')
    # for l in birthdays:
    #     print(l)

    # print('Who\'s birthday do you want to look up?')
    
    # name = input()
    # if name in birthdays:
    #     #print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    #     print(f'{name} birthday is {birthdays[name]}')
    # else:
    #     print('Sadly, we don\'t have {}\'s birthday.'.format(name))



