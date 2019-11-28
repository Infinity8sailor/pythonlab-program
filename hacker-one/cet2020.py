import wget
#5300
#6298

for i in range(4841,5000):
  url="http://fe2019.mahacet.org/CAP-I/CAPR-I_EN"+str(i)+".pdf"
  path="/Users/vaibhav/Desktop/database/cet2020/"
  try:
      print(i)
      wget.download(url,path)
  except Exception:
      print("error")
      pass
  