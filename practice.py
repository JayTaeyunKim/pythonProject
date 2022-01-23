from datetime import datetime

today = datetime.today()
filedir = today.strftime("%Y/%m/%d")
print(filedir)