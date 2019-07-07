import sys
import numpy as np

# 対応項目から出力したい項目・内容を抽出する
def selectCsvData(inputCsvData,correspondTable):
	
	outputCsvData = np.array([])
	
	data = inputCsvData.csvData.T
	
	j1 = correspondTable.inputIndice.shape[0]
	j2 = data.shape[1]
	
	indice = inputCsvData.csvIndice
	num = indice.size
	count = 0
	for char in correspondTable.inputIndice:
		count = count + 1
		i = 0
		for i in range(num):
			if(indice[i] == char):
				outputCsvData = np.append(outputCsvData,data[i,:])
				break
	
	outputCsvData = outputCsvData.reshape((j1,j2))
	outputCsvData = outputCsvData.T
	
	return outputCsvData
