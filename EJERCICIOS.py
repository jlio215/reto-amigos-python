entrada_mia=input()
entrada_amigo= input()
entrada_invitados=input()
puntos_1=0
puntos_2=0
salida=str()
for i in range(0,len(entrada_invitados)):
    for j in range(0,len(entrada_amigo)):
        if entrada_mia[j]==entrada_invitados[i]:
            puntos_1 +=1
        if entrada_amigo[j]==entrada_invitados[i]:
            puntos_2 +=1
    if puntos_1==puntos_2:
        salida +="*" 
    elif puntos_1>puntos_2:
        salida += "1"
    elif puntos_1<puntos_2:
        salida += "2" 
print(salida)       
        
   

print(entrada_mia[1])
    
    
#QCWKFI

#LGECUO

#KATOAETFQUAPMVKLGMT

#WTXY|M
#WX+A|T
#AT-A|.-XXWWYT.XMT+XM.W.-

#222222222222222**22*****

#22222**1*****1****