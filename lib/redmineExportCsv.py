
import redmineApi

# redmineAPIの定義
redmineAPI = redmineApi.redmineAPI()

# redmineAPIに使う値の入力
redmineAPI.setUrl(config.redmine.url)
redmineAPI.setUser(config.redmine.user)
redmineAPI.setPass(config.redmine.pass)
redmineAPI.setPath(config.redmine.path)
redmineAPI.setName(config.redmine.name)

# redmineに接続
redmine = redmineAPI.connectRedmine()

# redmineから対象のチケットを取得
issues = redmineAPI.getSpecificIssues(redmine)

# 対象のチケットを更新する
redmineAPI.updateIssues(issues,date)

# csv形式でエクスポート
redmineAPI.exportCsv(issues)