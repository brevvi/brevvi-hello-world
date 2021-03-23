import time

def relogio():
    ano=2021-(int(((((time.time()/60)/60)/24)/365)))
    mes=int(int((((time.time()/60)/60)/24)%365)/30)
    dia=int((((((time.time()/60)/60)/24)%365)%30)/24)
    hora=10
    minu=int((((((((time.time()/60)/60)/24)%365)%365)%30)%3600)/60)
    segu=int(((((((((time.time()/60)/60)/24)%365)%365)%30)%3600)%60)%60)
    print("{}::{}::{}::{:02d}::{:02d}::{:02d}".format(ano, mes, dia, hora, minu, segu))

relogio()
