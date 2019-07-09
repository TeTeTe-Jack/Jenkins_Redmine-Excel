import openpyxl
import getData
import logicData
import setData

# configファイルを取得する
configData = getData.getConfigFile('.././con/config.ini')

# csvデータの取得
inputCsvData = getData.getInputCsv(configData.name.inputCsvName)

# 項目の対応表を取得
correspondTable = getData.getCorrespondTable(configData.name.correspondTableName)

# セルの幅を取得
configDataFlame = getData.getFlameWidth(configData.flame,configData.name.correspondTableName)

# 出力する項目・内容を抽出する
outputCsvData = logicData.selectCsvData(inputCsvData,correspondTable)

# ワークブックを作成する
wb = openpyxl.Workbook()

# ワークブックに項目を反映させる
wb = setData.setIndiceXlsx(wb,correspondTable.outputIndice)

# ワークブックに内容を反映させる
wb = setData.setCsvData(wb,outputCsvData)

# ワークブックに枠組みを反映させる
wb = setData.setFlameXlsx(wb,configData.flame)

# ワークブックを保存する
wb.save(configData.name.saveXlsxName)

# ワークブックを閉じる
wb.close()
