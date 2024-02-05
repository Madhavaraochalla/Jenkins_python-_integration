import jenkins

j = jenkins.Jenkins("http://localhost:8080","madhav","madhav")

j.delete_job("Dev1")
