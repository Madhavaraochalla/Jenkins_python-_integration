import jenkins

j = jenkins.Jenkins("http://localhost:8080","madhav","madhav")
i = 1
while i <= 5:
  j.build_job("mm%d"%i)

  i = i+1

