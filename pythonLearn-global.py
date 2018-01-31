

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
    lista.append(3)
    print('append')

if __name__ == '__main__':
    setValue() #ok
    add2() #ok
    add3() #ok    
    append()#ok
    add4() #UnboundLocalError: local variable 'i' referenced before assignment
    



        

    
