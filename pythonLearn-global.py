#global and local variable, don't try to modify variable through parameter, it's better to change by return value.

i = 1  #global i

def setValue():
    i = 2  #modify global value
    print('setValue')

def add2(): 
    global i
    i = i + 1 #modify global value
    print('add2')

def add3(): 
    i = 2 #local , hidden global i
    i = i + 1
    print('add3')


def add4():
    i = i + 1 #UnboundLocalError: local variable 'i' referenced before assignment
    print('add4') 


lista = []

def append():
    lista.append(3) #modify global lista
    print('append',lista)

def append2():
    listb = lista.copy() #modify local list
    listb.append(4)
    print('append2',lista, listb)

def append3(arg: list):
    arg.append(5) #modify extern list
    print('append3',lista, arg)

if __name__ == '__main__':
    setValue() #ok
    add2() #ok
    add3() #ok    
    append()#ok
    append2()#ok
    append3(lista)#ok
    #add4() #UnboundLocalError: local variable 'i' referenced before assignment
    
    

////////////////////////////////////output:
setValue
add2
add3
append [3]
append2 [3] [3, 4]
append3 [3, 5] [3, 5]

        

    
