import math

t = input("Masukkan Detik: ")
j = 3600 
m = 60 
d = 1

# format = ("HH:MM:SS")

# sj = t % j #sisa_jam
# jj = (int(t) - int(sj)%j) / j #jumlah jam 

# sm = sj % m #sisa_menit
# jm = (int(sj) - int(sm)%m) / m #jumlah menit 

# sd = sm % d #sisa_detik
# jd = (int(sm) - int(sd)%d) / d #jumlah detik 

# print(f"{jj} : {jm} : {jd}")

def TimeConverter(seconds):
    if t.isdigit() == True and len(t) <= 5:
        sj = int(t) % j #sisa_jam
        jj = round((int(t) - int(sj)%j) / j) #jumlah jam 

        sm = sj % m #sisa_menit
        jm = round((int(sj) - int(sm)%m) / m) #jumlah menit 

        sd = sm % d #sisa_detik
        jd = round((int(sm) - int(sd)%d) / d) #jumlah detik 

        a = f"{jj}:{jm}:{jd}"
    
    else: 
        a = "Format Bilangan Salah"
    
    return a 

print(TimeConverter(t))




   