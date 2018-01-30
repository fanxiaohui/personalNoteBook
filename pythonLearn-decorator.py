
#decorator: 1) a decorator is a function; 2)input a function, output a new function;3)keep the same function signature


def apply(func: object, *value) -> object: 
    return func(*value)


def outer(*args) -> object:  
    def inner(*inargs):
        print(*args, *inargs)    
    return inner #note: don't return inner()
    

def decorator(func:object) -> object:
    def wrapper(*args, **kwargs):
        print('new function is called')
        return func(*args, **kwargs)
    return wrapper

def myprint(*args, **kwargs):
    for a in args:
        print(a,end=' ; ')    
    for k,v in kwargs.items():
        print(k,v,sep='->',end=' ; ')    
    
    
if __name__ == '__main__':    
    f = apply(outer,1,2)
    f('hello','world')
    
    config = {'name':'liang'}
    f2 = decorator(myprint)
    f2('good','bye', **config)
    
    
///////////output:
1 2 hello world
new function is called
good ; bye ; name->liang ; 
