from bs4 import BeautifulSoup
import requests
from decimal import Decimal
import re

dh_url = 'https://www.dolarhoy.com/'
dh_contadoliqui = dh_url + "cotizaciondolarcontadoconliqui"
dh_page = requests.get(dh_contadoliqui)
dh_status_code = dh_page.status_code

cedears_url = "https://www.rava.com/precios/panel.php?m=CED"
cedears_page = requests.get(cedears_url)
cedears_status_code = cedears_page.status_code

ratios_url = "https://www.infobursatil.com/listado-cedears/"

acciones_url = "https://www.invertironline.com/mercado/cotizaciones/estados-unidos"

if (dh_status_code == 200)and(cedears_status_code==200):
	dh_soup = BeautifulSoup(dh_page.content,"html.parser")
	#print(soup)
	venta = dh_soup.find('div',class_='venta').find('span').get_text().replace("$", "").strip()
	compra = dh_soup.find('div',class_='compra').find('span').get_text().replace("$", "").strip()
	
	dh_pventa=float(venta.replace('.','').replace(',','.'))
	dh_pcompra=float(compra.replace('.','').replace(',','.'))

	print(f"Precio Venta: ${dh_pventa} vs Precio Compra: ${dh_pcompra}")

	lista= []
	cedears = BeautifulSoup(cedears_page.content,"html.parser")
	tabla = cedears.find('table',class_='tablapanel2')
	#fila = tabla.find("a",text=re.compile(nombre)).find_parent().find_parent().find_all('td')		
	filas = tabla.find_all('tr')
	
	for fila in filas[1:]:		
		try:
			campos=fila.find_all('td')		
			name = campos[0].find('a').get_text().replace("CEDEAR",'').replace("CEDEA",'')
			precio = float(campos[1].get_text().replace('.','').replace(',','.'))
			variac = float(campos[2].get_text().replace('.','').replace(',','.'))
			vol_nom = float(campos[8].get_text().replace('.','').replace(',','.'))
			lista.append(dict(name=name,precio=precio,variac=variac,vol_nom=vol_nom))	
		except:
			pass
	#[{'name': 'CEDEARLYG', 'precio': 104.5, 'variac': 3.21, 'vol_nom': 3297.0},...]
	ratios_page = requests.get(ratios_url)
	ratios_status_code = ratios_page.status_code
	ratios_soup = BeautifulSoup(ratios_page.content,"html.parser")

	acciones_page = requests.get(acciones_url)
	acciones_status_code = acciones_page.status_code
	acciones_soup = BeautifulSoup(acciones_page.content,"html.parser")


	
	for l in lista:		
		try:
			fila=ratios_soup.find('div',class_='entry themeform').find('table').find("strong",text=re.compile(l['name'])).find_parent().find_parent().find_all('td')
			ratio=fila[2].get_text()
			ratio_num=int(ratio.split(":",1)[0])
		except:
			ratio_num=0
		
		l.update({'ratio':ratio_num})
		
		try:
			acciones_a=acciones_soup.find('table',id='cotizaciones').find("b",text=re.compile(l['name'])).find_parent()
			acciones_fila=acciones_a.find_parent().find_parent()
			acciones_nombre = acciones_a.find('span').get_text().strip()
		except:
			acciones_nombre = l['name']
		l.update({'descr':acciones_nombre})

		accion_valor= acciones_fila.find('td',{'data-field': 'UltimoPrecio'}).get_text().strip()
		if accion_valor=='':
			accion_valor=0.00
		else:
			accion_valor=float(accion_valor.replace('.','').replace(',','.'))
		l.update({'accion_valor':accion_valor})
		if accion_valor==0.00:
			dif=0
		else:
			valor_dlr = round((l['precio']*ratio_num)/accion_valor,2)
			dif = round(dh_pcompra-valor_dlr,2)
		l.update({'diferencia':dif})
	
	#lista_final = [x for x in lista if (x['diferencia']>0)and(x['diferencia']<150)and(x['ratio']>1)]	
	lista_final = sorted(lista,key= lambda x: x['diferencia'],reverse=True)
	from pprint import pprint	


	ticket = input("Nombre del Ticket? ")

	if ticket:
		resultado = [x for x in lista_final if x['name']==ticket]
		pprint(resultado)
	# valor_pesos = round((valor['precio'] / accion_valor)*ratio_num,2)
	# print(f"Valor Compra Acción: ${valor_pesos} vs Valor Dólar CCL: ${dh_pventa}")
	# dif = round(valor_pesos-dh_pventa,2)
	# if dif<0:
	# 	print(f"{nombre}¡¡¡CONVIENE COMPRAR!!! (diferencia de ${dif})")
	# else:
	# 	print(f"{nombre} ¡MEJOR PASO!")


	# print(ratio,accion_valor)

		
	# except:
	# 	print(f"El valor ingresado no es un ticket Válido, hubo un error!")
	# 	print(lista)
	

else:
	print("WEB CAÍDA!!")