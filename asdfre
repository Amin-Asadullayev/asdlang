# -*- coding: utf-8 -*-
import random as kop
import datetime as daat
import re
import os 
f = open(os.environ["filemy"], "r")
cars = (f.read()).split("\n")
x = ""
i = 0
funkec=True
print("\n\nProqram işləyir...")
while i < len(cars):
	if cars[i].startswith("yaz "):
		if funkec:
			s1n = cars[i][4:]
			print(str(eval(s1n)).replace("#y#", "\n"))
	elif cars[i].startswith("deyisen "):
		if funkec:
			deyisenadi = cars[i][8:].split(sep="=", maxsplit=1)[0].strip()
			deyisendeyeri = cars[i][8:].split(sep="=", maxsplit=1)[1]
			yokhglanish = re.search("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]", deyisenadi)
			if yokhglanish:
				patterinu = re.compile("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]")
				yikhglanish = patterinu.match(deyisenadi)
				if int(yikhglanish.group(2))>=len(globals()[yikhglanish.group(1)]):
					for opingsyse in range(len(globals()[yikhglanish.group(1)]), int(yikhglanish.group(2))+1):
						globals()[yikhglanish.group(1)].append("")
				(globals()[yikhglanish.group(1)])[int(yikhglanish.group(2))]= eval(deyisendeyeri)
			else:
				globals()[deyisenadi] = eval(deyisendeyeri)
	elif cars[i].startswith("sorgu "):
		if funkec:
			deyisenadi = cars[i][6:].split(sep="=", maxsplit=1)[0].strip()
			sorgudeyerin = cars[i][6:].split(sep="=", maxsplit=1)[1]
			print(sorgudeyerin)
			yokhglanish = re.search("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]", deyisenadi)
			if yokhglanish:
				patterinu = re.compile("([a-zA-Z-çəğıöşüÇƏĞİÖŞÜ]+)\[(.+)\]")
				yikhglanish = patterinu.match(deyisenadi)
				if int(yikhglanish.group(2))>=len(globals()[yikhglanish.group(1)]):
					for opingsyse in range(len(globals()[yikhglanish.group(1)]), int(yikhglanish.group(2))+1):
						globals()[yikhglanish.group(1)].append("")
				(globals()[yikhglanish.group(1)])[int(yikhglanish.group(2))]= input()
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
	elif cars[i].startswith("əgər "):
		s1n = cars[i][5:]
		sert = s1n.split(sep=":", maxsplit=1)[0]
		emr = s1n.split(sep=":", maxsplit=1)[1]
		if eval(sert):
			if emr.startswith("yaz "):
				s1n = emr[4:]
				print(eval(s1n))
			if emr.startswith("dəyişən "):
				s1n = emr[8:]
				s1n = s1n.split(sep="=", maxsplit=1)
				deyisenadi = s1n[0]
				deyisendeyeri = s1n[1]
				globals()[deyisenadi] = eval(deyisendeyeri)
			if emr.startswith("sorgu "):
				s1n = emr[6:]
				s1n = s1n.split(sep="=", maxsplit=1)
				deyisenadi = s1n[0]
				print(eval(s1n[1]))
				globals()[deyisenadi] = input()
			if emr.startswith("get "):
				s1n = emr[4:]
				i = int(s1n) - 2
			if emr.startswith("dayan"):
				i = len(cars)
	i += 1
