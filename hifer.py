alfavit="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

print ("Что Вам нужно?") #Соблюдение формальности того что нужно сделать и закодирование и раскодирование
print ("Введите 1 чтобы ЗАКОДИРОВАТЬ")
print ("Введите 2 чтобы РАСКОДИРОВАТЬ")
input()

print("Введите фразу:")
fraza=input()

newfraza=fraza
backup=fraza
smesheniye=0
fraza=fraza.replace(' ', '')#Этот блок заменяет пробелы и цифры на ниего
fraza=fraza.replace('1', '')
fraza=fraza.replace('2', '')
fraza=fraza.replace('3', '')
fraza=fraza.replace('4', '')
fraza=fraza.replace('5', '')
fraza=fraza.replace('6', '')
fraza=fraza.replace('7', '')
fraza=fraza.replace('8', '')
fraza=fraza.replace('9', '')
fraza=fraza.replace('0', '')
copyfraza=fraza

dlina = (len(fraza))#возвращает количество букв в нашей фразе
fraza=list(fraza)
print(fraza)
alfavit=list(alfavit) # Лист преобразовывает в аналог массива для строк



newfraza=list(newfraza)
zdesprobel=''
zdesprobel=list(zdesprobel)
j=0

    
print (zdesprobel)
for i in range(len(newfraza)): #Тут оно находит места где в тексте пробелы и цифры и записывает их в переменную zdesprobel, а зачем столько циклов я сам не понимаю, главное работает
   
    if newfraza[i]==" ":
        index=(newfraza.index(' '))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    
    if newfraza[i]=="1":
        index=(newfraza.index('1'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="2":
        index=(newfraza.index('2'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="3":
        index=(newfraza.index('3'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="4":
        index=(newfraza.index('4'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="5":
        index=(newfraza.index('5'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="6":
        index=(newfraza.index('6'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="7":
        index=(newfraza.index('7'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="8":
        index=(newfraza.index('8'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="9":
        index=(newfraza.index('9'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    if newfraza[i]=="0":
        index=(newfraza.index('0'))
        print(index)
        newfraza[index]=""
        
        zdesprobel+=' '
        print(zdesprobel)
        zdesprobel[j]=str(index)
        j+=1
    
print ("На этих индексах пробелы или цифры", zdesprobel) #Выводим где у нас пробелы



print ("Что с этим делать?") 
print ("Введите 1 чтобы сделать все 33 ROT-a")
print ("Введите 2 чтобы сделать конкретный номер ROT-a")
kak=input()
if kak=="1":
    kod=''
    for i in range (33): #Эта штука выводит все 33 рота, в ней прописывается смещение которое с каждым шагом цикла прибавляется
        for j in range(dlina):
            #print(fraza[i])
            #print (alfavit.index(fraza[i]))
            iskomayavalfavite=(alfavit.index(fraza[j])) #тут берётся индекс одной из букв сообщенияя
            nomernuzhnoibukvi=iskomayavalfavite+smesheniye #Тут к этому номеру в алфавите прибавляется смещение
            #print(nomernuzhnoibukvi)
            if nomernuzhnoibukvi >= 33: # 33 чтобы не выходить за границы алфавита
                nomernuzhnoibukvi-=33
            #print(nomernuzhnoibukvi)
            #print (alfavit[(nomernuzhnoibukvi)])
            kod+=(alfavit[(nomernuzhnoibukvi)]) #Тут мы запоминаем все буквы


        kod = list(kod)
        for i in range (len(zdesprobel)): # Эта штука доставляет пробелы и прочее, потом сделаю upd(сделал)
            a=zdesprobel[i]
            b=backup[int(a)]
            kod.insert(int(a),b) # функция инсерт доставляет по номеру А символ B

        newkod=""
        for i in range (len(kod)): # тут записали фразу в читабельный вид
            newkod+=kod[i]
        print('Зашифрованное сообщение ROT',smesheniye,' : ',newkod)
        smesheniye+=1
        kod = ''
numberrota=''


if kak == '2': #Второе условие, оно выводит нам конкретный рот
    print('Введите какой ROT сделать')
    numberrota=input ()
    smesheniye = int(numberrota)
    kod=''
    for j in range(dlina):
            #print(fraza[i])
            #print (alfavit.index(fraza[i]))
            iskomayavalfavite=(alfavit.index(fraza[j]))
            nomernuzhnoibukvi=iskomayavalfavite+smesheniye
            #print(nomernuzhnoibukvi)
            if nomernuzhnoibukvi >= 33: # 33 чтобы не выходить за границы алфавита
                nomernuzhnoibukvi-=33
            #print(nomernuzhnoibukvi)
            #print (alfavit[(nomernuzhnoibukvi)])
            kod+=(alfavit[(nomernuzhnoibukvi)])


    kod = list(kod)
    for i in range (len(zdesprobel)): # Эта штука доставляет пробелы и прочее, потом сделаю upd(сделал)
        a=zdesprobel[i]
        b=backup[int(a)]
        kod.insert(int(a),b)

    newkod=""
    for i in range (len(kod)): # Это правильно выводит на экран наше сообщение
        newkod+=kod[i]
    print('Зашифрованное сообщение ROT',smesheniye,' : ',newkod)
    smesheniye+=1
    kod = ''