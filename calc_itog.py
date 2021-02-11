
#операции
def summ(a,b):
  return a+b
def razn(a,b):
  return a-b
def umn(a,b):
  return a*b
def chast(a,b):
  return a/b

#замена последних 2х элементов стэка на один в случае операции
def comp(list,a):
  list.append(a)
  list.pop(-2)
  list.pop(-2)
  return(list)

#произведение операций если аргументов больше 2
def cl(ch,sim):
  global ud
  if len(sim)>0:
    if sim[-1] in ud:
      if sim[-1]=='*':
        rez=umn(ch[-1],ch[-2])
        comp(ch,rez)
      else:
        if ch[-1]!=0:
          rez=chast(ch[-2],ch[-1])
          comp(ch,rez)
        else:
          try:
            5/0
          except ZeroDivisionError:
            delen0=True
            for k in range(len(ch)):
              ch.pop()
            for j in range(len(ch)):
              ch.pop()
            return('Деление на ноль')
    elif sim[-1] in pm:
      if sim[-1]=='+':
        rez=summ(ch[-1],ch[-2])
        comp(ch,rez)
      else:
        rez=razn(ch[-2],ch[-1]) 
        comp(ch,rez)
    sim.pop()
    if len(sim)>0:
      if sim[-1]!='(':
        x=cl(ch,sim)
        if x == 'Деление на ноль':
          return x
        if len(sim)>0: 
          if sim[-1] in pm:
            clpm(ch,sim)
        if len(sim)>0:
          if sim[-1] in ud:
            x=cl(ch,sim)
            if x == 'Деление на ноль':
              return x
      else:
        sim.pop()
  return(ch,sim)

# + и - если аргументов >2
def clpm(ch,sim):
  global ud
  if len(sim)>0:
    if sim[-1] in pm:
      if sim[-1]=='+':
        rez=summ(ch[-1],ch[-2])
        comp(ch,rez)
      else:
        rez=razn(ch[-2],ch[-1]) 
        comp(ch,rez)
    sim.pop()
    x=cl(ch,sim)
    if x == 'Деление на ноль':
      return x
    if len(sim)>0: 
      if sim[-1] in ud:
        x=cl(ch,sim)
        if x == 'Деление на ноль':
          return x
    if len(sim)>0: 
      if sim[-1] in pm:
        clpm(ch,sim)  

#поиск открывающей скобки
def clsk(ch,sim):
        for j in range(len(sim)-1,0,-1):
            if sim[j]!='(':
              x=cl(ch,sim)
              if x == 'Деление на ноль':
                return x
            if sim==[]:
                break
            else:
                break

#ввод выражения
def inputt(str):
    global a,b,ch,sim,delen0,cifra,pm,ud,tz,sk,NV
    a = str
    b = len(a)
    ch=[]
    sim=[]
    cifra=''
    pm=['+','-']
    ud=['*','/']
    tz=['.',',']
    sk=['(',')']
    delen0=False
    NV=False

#main
def parser(str):
    inputt(str) 
    global i,an,ud   
    for i in range(b):
        y=if_chislo()
        if y is not None:
          return y
        ex=if_sim()
        if ex is not None:
          return ex
        if i==b-1 and delen0==False:
            an=outputt()
    return(an)

#если встретили число
def if_chislo():
      global i,cifra,ud      
      if a[i].isdigit()==True and delen0==False:
        cifra=cifra+a[i]
        if i==b-1:
          if '.' or ',' in cifra:
            ch.append(float(cifra))
          else:
            ch.append(int(cifra))  
          if len(sim)>0:
            if sim[-1] in ud:
              x=cl(ch,sim)
              if x == 'Деление на ноль':
                return x
            elif sim[-1] in pm:
              x=cl(ch,sim)
              if x == 'Деление на ноль':
                return x

#если встретили символ
def if_sim():  
  global cifra,NV,delen0,ud         
  if a[i].isdigit()==False and delen0==False:
    if ((a[i] in pm or a[i] in ud) and (a[i-1] in pm or a[i-1] in ud)) or (i==0 and a[i] not in '1234567890('):
      NV=True
      return(outputt())
    if (a[i] not in pm) and (a[i] not in ud) and (a[i] not in tz) and (a[i] not in sk):
      NV=True
      return(outputt())
    if len(sim)>0 and a[i-1]=='(' and a[i]==')':
      NV=True
      return(outputt())
    if a[-1].isdigit()==False and a[-1] not in ')':
      NV=True
      return(outputt())
    if (len(ch)==0 and cifra=='') and a[i] not in '(':
      NV=True
      return(outputt())
    if a[i]=='.' or a[i]==',':
      cifra+='.'
    else:
        if cifra!="":
            if '.' or ',' in cifra:
                ch.append(float(cifra))
            else:
                ch.append(int(cifra))
        if a[i]==')':
            clsk(ch,sim)
        if len(ch)>1 or i==b-1:
            if len(sim)>0:
              if a[i]!='(':
                if sim[-1] in ud:
                  x=cl(ch,sim)
                  if x == 'Деление на ноль':
                    return x
        
        cifra=''
        if a[i]!=' ':
          sim.append(a[i])

#итоговый вывод
def outputt():
    global x,NV,ud
    if a.count('(')==a.count(')') and NV==False and delen0==False:
      if len(sim)<2:
        x=str(ch[0])
        return x
      elif len(sim)>1:
        if sim==['(',')']:
          x=str(ch[0])
          return x
    elif NV==False:
        return ('Некорректный ввод')
    elif NV==True:
        return('Некорректный ввод')