#!groovy

pipeline {
  
  agent{
    label 'master'
  }
  
  paramters{
    string name 'slackChannel'
    string name 'jenkins_homeDir'
    string name 'shareJenkinsDir'
    string name 'shareBackupDir'
    string name 'backupServer'
    string name 'password'
    
  }
  
  stages{
    
    stage('check parameters'){
      steps{
        sh "./script/checkParameter.sh -xe $slackChannel"
        sh "./script/checkParameter.sh -xe $jenkins_homeDir"
        sh "./script/checkParameter.sh -xe $shareJenkinsDir"
        sh "./script/checkParameter.sh -xe $shareBackupDir"
        sh "./script/checkParameter.sh -xe $backupServer"
      }
    }
  
    stage('Notify slack to start job') {
      steps{
        slackSend channel: "$slackChannel", color: "good", message: "Job start ${env.job_name}"
      }
    }
  
    stage('Replace config file'){
      steps{
        sh "./script/mount.sh -xe $backupServer $shareBackupDir $shareJenkinsDir $password"
      }
    }
  
    stage('Change flag of tickets'){
      steps{
        sh "./script/makeBackup.sh -xe $jenkins_homeDir $shareJenkinsDir"
      }
    }
    
    stage('Get csv from Redmine'){
      steps{
        sh "./script/unmount.sh -xe $shareJenkinsDir"
      }
    }
    
    stage('Crate xlsx file'){
      steps{
        sh "./script/unmount.sh -xe $shareJenkinsDir"
      }
    }
    
    stage('Move xlsx file to upload directory'){
      steps{
        sh "./script/unmount.sh -xe $shareJenkinsDir"
      }
    }
  }
  
  post{
    
    always{
      slackSend channel: "$slackChannel", color: "good", message: "Job Finish ${env.job_name}
    }
      
    success{
      slackSend channel: "$slackChannel", color: "good", message: "Job Success ${env.job_name}
    }
    
    failure{
      slackSend channel: "$slackChannel", color: "danger", message: "Job Failure ${env.job_name}
    }
    
    aborted{
      slackSend channel: "$slackChannel", color: "warning", message: "Job Aborted ${env.job_name}
    }  
  }
}