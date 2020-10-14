import requests
import os

os.system("")

# Group of Different functions for different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


listado = [dict(url="http://boletas.cotoer.com.ar/login/",sistema="Colegios Terapistas"),
			dict(url="http://boletas.inmogroup.com.ar/login/",sistema="Consorcios"),
			dict(url="http://sucec.ironweb.com.ar/login/",sistema="IronWEB"),
			dict(url="http://prueba.ironweb.com.ar/login/",sistema="IronWEB Prueba"),
			dict(url="https://sistemaslaboralsalud.com.ar/login/",sistema="LaboralSalud"),
			]

def main():
	for l in listado:
		estado = style.RED+'NO ACTIVO'
		try:
			page = requests.get(l['url'])
			status_code = page.status_code
			if status_code==200:
				estado = style.GREEN +'ACTIVO'
		except Exception as e:
			print(style.WHITE+f"{l['sistema']:20}\t ==> {e}")
		print(style.WHITE +f"{l['sistema']:20}\t ==> "+estado)
	print(style.WHITE)

if __name__ == '__main__':
   main()