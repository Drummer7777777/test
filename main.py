from figurs import Circle, Pryamougolnik

figur_data=[]
for i in range(3):
    #if i==0:
        figur_data.append(input())
id=1
figur_data.insert(0,id)
#print(figur_data)

if figur_data[1]=="0" and figur_data[3]=="no":
    #print(1)
    circle=Circle()
    pl_circle=Circle.pl(figur_data[0],figur_data[1],figur_data[2],figur_data[3])
if figur_data[1]=="4" and figur_data[2]=="0" and figur_data[3]=="yes":
    prayam=Pryamougolnik()
    prayam.pl()
else:
    print("Неизвестная фигура")