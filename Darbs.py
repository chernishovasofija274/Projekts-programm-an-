print ("1")
N=int(input("Cik atzimes tev ir Geografija? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Matematika? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Krievu valoda? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Latviesu valoda? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Fizika? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Anglu valoda? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Kimija? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Kulturas pamati? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Biologija? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Sports un veseliba? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

N=int(input("Cik atzimes tev ir Vesture un socialas zinatnes? - "))
sum=0
for i in range(N):
    a=int(input("Kada ir atzime? - "))
    sum+=a
    c=sum/N
print("Videja atzime- %.0f"%c)    
if c==9 or c==10: print("tas ir izcili")
elif c>=6 and c<=8: print("tas ir optimali") 
elif c==4 or c==5: print("tas ir pietiekami")
else: print("tas ir nepietiekami") 

print("2")
N=int(input("Cik prieksmetus jums vajag sodien izpildit? - "))
v=0
t=0
n=0
for i in range(N):
        a=float(input("Cik mintes jus pildijat prieksmetu?  - "))
        if 0<=a <=60 : v=v+1
        elif 60<=a<90 :t=t+1
        else: n=n+1
print(" Ir",v," prieksmeti, uz kuriem jus pavada parak maz laika , ir", t, "prieksmeti,jus pavada nepieciesamo laiku, un ir" , n,"prieksmeti, uz kuriem jus pavada parak daudz laika")

print("3")
f=int(input("Cik tu izpildijis prieksmetus? - "))
if f==N: print("Malacis!")
else: print("Sis darbs paliek tev uz ritdienu!") 

