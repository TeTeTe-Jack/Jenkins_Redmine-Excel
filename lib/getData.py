import sys
import csv
import configparser
import numpy as np
from lib import classData

# configファイルを取得する
def getConfigFile(configFileName):
	
	# configファイルを読み込む
	f = configparser.ConfigParser()
	f.read(configFileName,'UTF-8')
	
	# 格納する変数を定義する
	data = classData.configData()
	
	# それぞれの値を格納する
	# name
	data.name.inputCsvName = f.get('name','inputCsvName')		
	data.name.correspondTableName = f.get('name','correspondTableName')
	data.name.saveXlsxName = f.get('name','saveXlsxName')
	
	# flame	
	data.flame.heightIndice = f.get('flame','heightIndice')
	data.flame.heightData = f.get('flame','heightData')	
	data.flame.bgcolorIndice = f.get('flame','bgcolorIndice')
	data.flame.bgcolorData = f.get('flame','bgcolorData')
	data.flame.borderStyle = f.get('flame','borderStyle')
	data.flame.borderColor = f.get('flame','borderColor')
	
	# 格納したデータを返す
	return data


# csvの内容を取得する
def getInputCsv(inputCsvName):
	
	# 格納する変数を定義する
	data = classData.inputCsvData()
	
	# csvファイルを開いて内容を変数に格納する
	with open(inputCsvName,'r') as f:
		reader = csv.reader(f,delimiter=',')
		data.csvIndice = np.append(data.csvIndice,next(reader))
		
		i = 0
		for row in reader:
			i = i + 1
			j = len(row)
			data.csvData = np.append(data.csvData,row)
		data.csvData = data.csvData.reshape((i,j))
		f.close()
		
	# 格納したデータを返す
	return data


# データの対応表を取得する	
def getCorrespondTable(correspondTableName):
	
	# 格納する変数を定義する
	data = classData.correspondTable()
	
	# csvファイルを開いて内容を変数に格納する
	with open(correspondTableName,'r') as f:
		reader = csv.reader(f)	
		data.outputIndice = np.append(data.outputIndice,next(reader))
		data.inputIndice = np.append(data.inputIndice,next(reader))
		f.close()
	
	# 格納したデータを返す
	return data


# 項目のセルの幅を取得する	
def getFlameWidth(data,correspondTableName):
	
	# csvファイルを開いて幅の情報を変数に格納する
	with open(correspondTableName,'r') as f:
		reader = csv.reader(f)
		next(reader)
		next(reader)
		data.width = np.array(next(reader))
		f.close()
	
	# 格納したデータを返す
	return data
	
	

