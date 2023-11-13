
def fact(n):
    if n == 0 :
        return 1
    else :
        return n * fact(n-1)    

print( fact(3) )
print( fact(5) )


def func( a, b=1, c=1 ):
    return a*b*c

func(a=1,b=2,c=3)

def sumArgs( *args ) :
    v = 0
    print( args )
    # for n in args :
    #     v += n
    # return v

# public class Main{
#     public static void main(String args[]){

#     }
# }
# java Main 777 777 888 999