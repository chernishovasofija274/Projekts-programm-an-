print ("1")
L=(input("Macoties majas, stundas laika jus vart pilniba koncentreties?-"))
A=(input("Ka jus domajat, talmaciba jus iegustat lidzvertigas zinasanas? Kapec?-"))
F=(input("Vai jus meklejat palidzibu pie klasesbiedriem?-"))
B=(input("Kadam prieksmetam jus veltat vismazako laiku?-"))
C=(input("Kadam prieksmetam jus pavadat visvairak laika?-"))
G=print ("Cik sarezgiti ir uzdevumi katram prieksmetam?", "(loti vienkarsi/vienkarsi/nav loti vienkarsi/nav loti gruti/gruti)")
a=(input("Geografija-"))
b=(input("Matematika-"))
c=(input("Krievu valoda-"))
d=(input("Latviesu valoda-"))
e=(input("Fizika -"))
f=(input("Anglu valoda-"))
r=(input("Kimija -"))
g=(input("Kulturas pamati-"))
i=(input("Biologija-"))
u=(input("Sports un veseliba -"))
t=(input("Vesture un socialas zinatnes-"))

print("2")
N=int(input("Cik prieksmetus jums vajag sodien izpildit? - "))
v=0
t=0
n=0
h=0
for i in range(N):
        a=float(input("Cik mintes jus pildijat prieksmetu?  - "))
        if 2<=a <=39 : v=v+1
        elif 40<=a<89 :t=t+1
        elif 0<=a<1 :h=h+1
        else: n=n+1
print(" Ir",v," prieksmeti, uz kuriem jus pavada parak maz laika , ir", t, "prieksmeti,jus pavada nepieciesamo laiku, un ir" , n,"prieksmeti, uz kuriem jus pavada parak daudz laika, ir", h , "neizpilditi prieksmeti" )

print("3")
f=int(input("Cik tu izpildijis prieksmetus? - "))
if f==N: print("Malacis!")
else: print("Sis darbs paliek tev uz ritdienu!") 

