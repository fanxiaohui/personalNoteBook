
def myfunc(*args):
    for a in args:
        print(a, end=' ; ')
    if args:
        print('\n','arg num = ',len(args))


def myfunc2(**kwargs):
    for k,v in kwargs.items():
        print(k, v, sep='->', end=' ; ')
    if kwargs:
        print('\n','arg num = ',len(kwargs))

if __name__ == '__main__':    
    paras = [1,2,3]
    myfunc(paras) #input one arg:list
    myfunc(*paras)#input 3 args: 1,2,3
    myfunc(4,5,6) #input 3 args
    myfunc2(name = 'liang',age = 30)
        

    
//////////////output:
[1, 2, 3] ; 
 arg num =  1
1 ; 2 ; 3 ; 
 arg num =  3
4 ; 5 ; 6 ; 
 arg num =  3
name->liang ; age->30 ; 
 arg num =  2
