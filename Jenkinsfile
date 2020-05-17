properties([[$class: 'JiraProjectProperty'], parameters([string(defaultValue: '31', description: '', name: 'NAME', trim: false)]), pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/avielb/DevOps0803.git"
    }
    stage("show"){
        sh "ls"
       // bat "dir"
    }
}
