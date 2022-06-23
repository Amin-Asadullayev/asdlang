try:
	# -*- coding: utf-8 -*-
	import random as kop
	import datetime as daat
	import re
	import os
	import io
	with io.open(os.environ["filemy"],'r',encoding='utf8') as f:
		cars = (f.read()).split("\n")
	def rəqəm(a):
		return int(a)


	def kəsr(a):
		return float(a)
	
	
	def modul(a):
		if a > 0:
			return a
		if a < 0:
			return -a
	
	
	def random(a, b):
		return kop.randint(a, b)
	
	
	def yerləşdir(a, b, c):
		return a.replace(b, c)
	
	
	def kiçik(a):
		return a.lower()
	
	
	def böyük(a):
		return a.upper()
	
	
	def yuvarlaq(a):
		return round(a)
	
	
	def kök(a):
		return a ** 0.5
	

	def sil(a, b):
		c = a.split(sep=b)
		return "".join(c)

	def kəs(a, b):
		return a[b:]

	def ayır(a, b):
		return a.split(sep=b)

	def daxildir(a, b):
		if b in a:
			return True
		else:
			return False

	def say(a, b):
		sipi = a.split(sep=b);
		sipi = len(sipi) - 1;
		return sipi

	def çevir(n, b):
		dfgoni = ""
		if n == 0:
			return [0]
		digits = []
		while n:
			digits.append(int(n % b))
			n //= b
		for dfgon in digits[::-1]:
			dfgoni += str(dfgon)
		return int(dfgoni)
	def uzunluq(a):
		return len(a)


	def əlavəet(a, b):
		a.append(b)
		return a


	def düz(a):
		a.sort()
		return a
	def ədəddüz(a):
		a.sort()
		return a

	def birləş(a, b):
		return b.join(a)


	def simvol(a):
		return str(a)


	def indeks(a, b):
		return a.index(b)


	x = daat.datetime.now()
	gün = x.strftime("%d")
	ay = x.strftime("%m")
	il = x.strftime("%y")
	saat = x.strftime("%H")
	dəqiqə = x.strftime("%M")
	saniyə = x.strftime("%S")
	x = ""
	i = 0
	ifelseon = True
	funkec = True
	print("\n\nProqram işləyir...")

	while i < len(cars):
		if cars[i].startswith("yaz "):
			if funkec:
				s1n = cars[i][4:]
				print(str(eval(s1n)).replace("#y#", "\n"), end="")
		elif cars[i].startswith("dəyişən "):
			if funkec:
				deyisenadi = cars[i][8:].split(sep="=", maxsplit=1)[0].strip()
				deyisendeyeri = cars[i][8:].split(sep="=", maxsplit=1)[1]
				yokhglanish = re.search("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]", deyisenadi)
				if yokhglanish:
					patterinu = re.compile("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]")
					yikhglanish = patterinu.match(deyisenadi)
					if int(eval(eval(yikhglanish.group(2))))>=len(globals()[yikhglanish.group(1)]):
						for opingsyse in range(len(globals()[yikhglanish.group(1)]), int(eval(eval(yikhglanish.group(2))))+1):
							globals()[yikhglanish.group(1)].append("")
					(globals()[yikhglanish.group(1)])[int(eval(eval(yikhglanish.group(2))))]= eval(deyisendeyeri)
				else:
					globals()[deyisenadi] = eval(deyisendeyeri)
		elif cars[i].startswith("sorğu "):
			if funkec:
				deyisenadi = cars[i][6:].split(sep="=", maxsplit=1)[0].strip()
				sorgudeyerin = cars[i][6:].split(sep="=", maxsplit=1)[1]
				print(eval(sorgudeyerin))
				yokhglanish = re.search("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]", deyisenadi)
				if yokhglanish:
					patterinu = re.compile("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]")
					yikhglanish = patterinu.match(deyisenadi)
					if int(eval(yikhglanish.group(2)))>=len(globals()[yikhglanish.group(1)]):
						for opingsyse in range(len(globals()[yikhglanish.group(1)]), int(eval(yikhglanish.group(2)))+1):
							globals()[yikhglanish.group(1)].append("")
					(globals()[yikhglanish.group(1)])[int(eval(yikhglanish.group(2)))]= input()
				else:
					globals()[deyisenadi] = input()
		elif cars[i].startswith("get "):
			s1n = cars[i][4:]
			i = int(s1n) - 2
		elif cars[i].startswith("funksiya "):
			unitemo = cars[i][9:].split("[")[0]
			globals()[unitemo] = i
			funkec = False
		elif cars[i].startswith("]"):
			s129s = cars[i][1:]
			if funkec == False:
				funkec = True
			else:
				i = globals()[s129s+"nov"]
		elif cars[i].startswith("çağır "):
			if funkec:
				globals()[cars[i][6:]+"nov"] = i
				i = globals()[cars[i][6:]]
		elif cars[i].startswith("dövr "):
			if funkec:
				s67s = cars[i][5:].split(sep="{", maxsplit=1)[0]
				deymen = s67s.split(sep="=>", maxsplit=1)[0]
				globals()[deymen.strip()+"muq"] = s67s.split(sep="=>", maxsplit=1)[1]
				globals()[deymen.strip()+"setr"] = i
		elif cars[i].startswith("}"):
			if funkec:
				if eval(globals()[cars[i][1:].strip()+"muq"]):
					i = globals()[cars[i][1:].strip()+"setr"]
		elif cars[i].startswith("əgər "):
			if funkec:
				if ifelseon:
					esasin = cars[i][5:]
					sertin = esasin.split(sep=":", maxsplit=1)[0]
					emrinolin = esasin.split(sep=":", maxsplit=1)[1]
					emrinolin = emrinolin.split(sep=";")
					nqabin = 0
					if eval(sertin):
						while nqabin < len(emrinolin):
							if emrinolin[nqabin].startswith("yaz "):
								s1n = emrinolin[nqabin][4:]
								print(str(eval(s1n)).replace("#y#", "\n"), end="")
							elif emrinolin[nqabin].startswith("dəyişən "):
								deyisenadi = emrinolin[nqabin][8:].split(sep="=", maxsplit=1)[0].strip()
								deyisendeyeri = emrinolin[nqabin][8:].split(sep="=", maxsplit=1)[1]
								yokhglanish = re.search("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]", deyisenadi)
								if yokhglanish:
									patterinu = re.compile("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]")
									yikhglanish = patterinu.match(deyisenadi)
									if int(eval(yikhglanish.group(2)))>=len(globals()[yikhglanish.group(1)]):
										for opingsyse in range(len(globals()[yikhglanish.group(1)]), int(eval(yikhglanish.group(2)))+1):
											globals()[yikhglanish.group(1)].append("")
									(globals()[yikhglanish.group(1)])[int(eval(yikhglanish.group(2)))]= eval(deyisendeyeri)
								else:
									globals()[deyisenadi] = eval(deyisendeyeri)
							elif emrinolin[nqabin].startswith("sorğu "):
								deyisenadi = emrinolin[nqabin][6:].split(sep="=", maxsplit=1)[0].strip()
								sorgudeyerin = emrinolin[nqabin][6:].split(sep="=", maxsplit=1)[1]
								print(eval(sorgudeyerin))
								yokhglanish = re.search("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]", deyisenadi)
								if yokhglanish:
									patterinu = re.compile("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]")
									yikhglanish = patterinu.match(deyisenadi)
									if int(eval(yikhglanish.group(2)))>=len(globals()[yikhglanish.group(1)]):
										for opingsyse in range(len(globals()[yikhglanish.group(1)]), int(eval(yikhglanish.group(2)))+1):
											globals()[yikhglanish.group(1)].append("")
									(globals()[yikhglanish.group(1)])[int(eval(yikhglanish.group(2)))]= input()
								else:
									globals()[deyisenadi] = input()
							elif emrinolin[nqabin].startswith("get "):
								s1n = emrinolin[nqabin][4:]
								i = int(s1n) - 2
							elif emrinolin[nqabin].startswith("funksiya "):
								unitemo = emrinolin[nqabin][9:].split("[")[0]
								globals()[unitemo] = i
								funkec = False
							elif emrinolin[nqabin].startswith("]"):
								s129s = emrinolin[nqabin][1:]
								if funkec == False:
									funkec = True
								else:
									i = globals()[s129s+"nov"]
							elif emrinolin[nqabin].startswith("çağır "):
								globals()[emrinolin[nqabin][6:]+"nov"] = i
								i = globals()[emrinolin[nqabin][6:]]
							elif emrinolin[nqabin].startswith("dövr "):
								s67s = emrinolin[nqabin][5:].split(sep="{", maxsplit=1)[0]
								deymen = s67s.split(sep="=>", maxsplit=1)[0]
								globals()[deymen.strip()+"muq"] = s67s.split(sep="=>", maxsplit=1)[1]
								globals()[deymen.strip()+"setr"] = i
							elif emrinolin[nqabin].startswith("}"):
								if eval(globals()[emrinolin[nqabin][1:].strip()+"muq"]):
									i = globals()[emrinolin[nqabin][1:].strip()+"setr"]
							nqabin += 1
				if eval(sertin) and cars[i+1]=="yox":
					ifelseon = False
				elif eval(sertin)==False and cars[i+1]=="yox":
					ifelseon = True
				elif cars[i+1]!="yox":
					ifelseon = True
		i += 1
	print("\n")
except NameError:
	print("Problem: Dəyişən və ya funksiya adı.")
except ValueError:
	print("Problem: Dəyişən və ya funksiya dəyəri.")
except TypeError:
	print("Problem: Müxtəlif tiplərin birgə istifadəsi və ya yanlış tip çevrilməsi.")
except ZeroDivisionError:
	print("Problem: Sıfıra bölmə.")
except OSError:
	print("Problem: Fayl tapılmadı.")
