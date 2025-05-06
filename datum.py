import datetime
trenutno = datetime.datetime.now()
moj = datetime.datetime(2024, 12, 6, 7, 25, 55)
print(moj)
sat = moj.hour
u_tjednu = moj.strftime("%A")
print(u_tjednu)