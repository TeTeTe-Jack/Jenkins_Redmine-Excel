import sys
import numpy as np

class configData:
	def __init__(data):
		data.name = configDataName()
		data.flame = configDataFlame()

class configDataName:
	def __init__(name):
		name.inputCsvName        = ''
		name.correspondTableName = ''
		name.saveXlsxName        = ''
		
class configDataFlame:
	def __init__(flame):
		flame.heightIndice  = 0
		flame.heightData    = 0
		flame.Width         = np.array([])
		flame.bgcolorIndice = ''
		flame.bgcolorData   = ''
		flame.borderStyle   = ''
		flame.borderColor   = ''
		
class inputCsvData:
	def __init__(data):
		data.csvIndice = np.array([])
		data.csvData = np.array([])
		
class correspondTable:
	def __init__(data):
		data.outputIndice = np.array([])
		data.inputIndice = np.array([])
