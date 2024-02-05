import jenkins

j = jenkins.Jenkins("http://localhost:8080","madhav","madhav")

j.copy_job("dev","Dev1")
