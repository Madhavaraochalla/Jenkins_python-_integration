import jenkins

j = jenkins.Jenkins("http://localhost:8080","madhav","madhav")
x = j.get_jobs()
print (x)
