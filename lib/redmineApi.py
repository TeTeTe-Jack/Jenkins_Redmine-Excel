import datetime
from redmine import Redmine

class redmineAPI:
    
    def __init__(self):   
        self.url  = ""
        self.user = ""
        self.pass = ""
        self.path = ""
        self.name = ""
        
    def setUrl(self,url):
        self.url = url
        
    def setUser(self,user):
        self.user = user

    def setPass(self,pass):
        self.pass = pass

    def setPath(self,path):
        self.path = path

    def setName(self,name):
        self.name = name

    def connectRedmine(self):
        redmine = Redmine(self.url, self.username=self.user, password=self.pass)
        return redmine
    
    def getSpecificIssues(self,redmine):
        issues = redmine.issue.filter(flag='new')
        return issues
    
    def updateIssues(self,issues,date):
        for issue in issues:
            issue.update(custom_fields=[{'id': 1, 'value': '2'},{'id': 2,'value': date}])

    def exportCsv(self,issues):
        issues.export('csv',savepath=self.path,filename=self.name)