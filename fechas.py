import datetime
from dateutil.relativedelta import relativedelta

#print datetime.date.today()
#print datetime.datetime.now()

a = datetime.date.today()
hoy = datetime.date.today()

#print dir(datetime.date)
#print dir(datetime.date.toordinal)

print hoy

mas_6_meses = hoy + relativedelta(months=+6)
mas_6_dias = hoy + relativedelta(days=+6)

print mas_6_meses
print mas_6_dias


#six_months = datetime.date.today() + relativedelta(months=+6)
#print six_months

formatting = "%B %d %Y %I:%M%p "
texto_fecha = "March 7 2009 7:30pm EST"
print texto_fecha

texto_fecha = texto_fecha[:-3] #Menos 3 caracteres
print texto_fecha

convert_to_datetime = datetime.datetime.strptime(texto_fecha , formatting)
print convert_to_datetime
print "Ahora a sumarle tiempo"

fecha_nueva = convert_to_datetime + datetime.timedelta(hours=12)
print fecha_nueva