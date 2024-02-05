import jenkins

j = jenkins.Jenkins("http://localhost:8080","madhav","madhav")
i = 1
while i <= 5:
  j.create_job("m%d"%i,config_xml)

  i = i+1
