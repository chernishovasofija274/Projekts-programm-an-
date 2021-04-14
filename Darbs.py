talmaciba=(input(" Vai jums patik talmaciba?-"))
if talmaciba == "Ja":
        print("Tas ir labi")
elif talmaciba =="Ne":
        print("Jums jabut pacietigam") 
else:
        print("Atbilde ir uzrakstits nepareizi") 
onlin = (int(input("Cik daudz bija onlin nodarbibas?-" )))
if 1<=onlin  <=6 : 
        print("Jums bija par daudz onlin nodarbibas")
elif 6<=onlin <10 :
        print("Jums bija par daudz onlin nodarbibas")
else: 
        print("Jums nebija onlin nodarbibas")

nodarbibam=(int(input("Cik minutes jus veicat uzdevumus bez online nodarbibam?-")))
if 0<=nodarbibam <=120 : 
        print("Jus pavadijat nepieciesamo laiku veicot uzdevumus bez online nodarbibam")
elif 120<=nodarbibam<180 :
        print("Jus pavadijat par daudz laiku veicot uzdevumus bez online nodarbibam")
else: 
        print("Jums nebija uzdevumus bez online nodarbibam ")

koncentreties=(input("Macoties majas, stundas laika jus vart pilniba koncentreties?-"))
if koncentreties=="Ja":
        print("Tas ir labi")
elif koncentreties=="Ne":
        print ("Jums jabut pacietigam")
else:
        print ("Atbilde ir uzrakstits nepareizi")  
zinasanas=(input("Ka jus domajat, talmaciba jus iegustat lidzvertigas zinasanas?-"))
if  zinasanas== "Ja":
        print( "Tas ir labi")
elif zinasanas =="Ne":
        print("Jums jabut pacietigam") 
else:
        print("Atbilde ir uzrakstits nepareizi")
palidzibu=(input("Vai jus meklejat palidzibu pie klasesbiedriem?-"))
if  palidzibu== "Ja":
        print( "Meginiet veikt pasi")
elif palidzibu =="Ne":
        print("Malacis") 
else:
        print("Atbilde ir uzrakstits nepareizi")
vismazakolaiku=(input("Kadam prieksmetam jus veltat vismazako laiku?-"))
if vismazakolaiku =="Geografija" or "Matematika" or "Krievu valoda" or "Latviesu valoda" or "Fizika" or "Kimija" or "Kulturas pamati" or "Biologija" or "Sports un veseliba" or "Vesture un socialas zinatnes":
        print("Varbut jums vajadzetu pavadit vairak laiku so prieksmetu izspilisanai")
else:
        print("Atbilde ir uzrakstits nepareizi")
visvairaklaika=(input("Kadam prieksmetam jus pavadat visvairak laika?-"))
if visvairaklaika=="Geografija" or "Matematika" or "Krievu valoda" or "Latviesu valoda" or "Fizika" or "Kimija" or "Kulturas pamati" or "Biologija" or "Sports un veseliba" or "Vesture un socialas zinatnes":
        print("Varbut jums vajadzetu pavadit mazak laiku so prieksmetu izspilisanai")
else:
        print("Atbilde ir uzrakstits nepareizi")
piekapjas=(input("Skolotajs vienmer jums piekapjas, ja jums nav laika pabeigt darbu laika?-"))
if piekpjas == "Ja":
        print( "Tas ir labi")
elif piekpjas =="Ne":
        print ("Jums vajadzetu meginat vest sarunas ar skolotaju")
else:
        print("Atbilde ir uzrakstits nepareizi")
atzimem=(input("Vai talmaciba jusu atzimes samazinajas?-"))
if atzimem == "Ja":
        print("Jums vajadzetu meginat labot atzimes")
elif atzimem =="Ne":
        print ("Tas ir labi")
else:
        print("Atbilde ir uzrakstits nepareizi")
uzdevumu=(input(" Ja jus nesaprotat skolotajas doto uzdevumu, skolotajs paskaidro jums so uzdevumu?-"))
if uzdevumu== "Ja":
        print( "Tas ir labi")
elif uzdevumu =="Ne":
        print("Jums vajadzetu meginat vest sarunas ar skolotaju") 
else:
        print("Atbilde ir uzrakstits nepareizi")
Ciksarezgiti=print ("Cik sarezgiti ir uzdevumi katram prieksmetam?", "(loti vienkarsi/vienkarsi/nav loti vienkarsi/nav loti gruti/gruti)")
a=(input("Geografija-"))
if a== "loti vienkarsi":
        print("Tas ir loti labi")
elif a =="vienkarsi":
        print("Tas ir labi") 
elif a =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif a =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif a =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")

b=(input("Matematika-"))
if b== "loti vienkarsi":
        print( "Tas ir loti labi")
elif b =="vienkarsi":
        print("Tas ir labi") 
elif b =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif b =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif b =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
c=(input("Krievu valoda-"))
if c == "loti vienkarsi":
        print( "Tas ir loti labi")
elif c =="vienkarsi":
        print("Tas ir labi") 
elif c =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif c =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif c =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
d=(input("Latviesu valoda-"))
if d== "loti vienkarsi":
        print( "Tas ir loti labi")
elif d =="vienkarsi":
        print("Tas ir labi") 
elif d =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif d =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif d =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
e=(input("Fizika -"))
if e== "loti vienkarsi":
        print( "Tas ir loti labi")
elif e =="vienkarsi":
        print("Tas ir labi") 
elif e =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif e =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif e =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
r=(input("Kimija -"))
if r == "loti vienkarsi":
        print( "Tas ir loti labi")
elif r =="vienkarsi":
        print("Tas ir labi") 
elif r =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif r =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif r =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
g=(input("Kulturas pamati-"))
if g== "loti vienkarsi":
        print( "Tas ir loti labi")
elif g =="vienkarsi":
        print("Tas ir labi") 
elif g =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif g =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif g =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
i=(input("Biologija-"))
if i == "loti vienkarsi":
        print( "Tas ir loti labi")
elif i =="vienkarsi":
        print("Tas ir labi") 
elif i =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif i =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif i =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
u=(input("Sports un veseliba -"))
if u == "loti vienkarsi":
        print( "Tas ir loti labi")
elif u =="vienkarsi":
        print("Tas ir labi") 
elif u =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif u =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif u =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
t=(input("Vesture un socialas zinatnes-"))
if t == "loti vienkarsi":
        print( "Tas ir loti labi")
elif t =="vienkarsi":
        print("Tas ir labi") 
elif t =="nav loti vienkarsi":
        print("Pamegini meklet papildu informaciju") 
elif t =="nav loti gruti":
        print("Pamegini meklet palidzibu") 
elif t =="gruti":
        print("Tev vajadzetu citigi stradat")         
else:
        print("Atbilde ir uzrakstits nepareizi")
