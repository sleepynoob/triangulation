def tracer_ligne_droite (n,x,y):
    if n > 0 :
        tracer(x,y)
        tracer_ligne_droite(n-1,x+1,y+1)
def triangle(n,x,y):
    if n>0 : 
        tracer(x,y)
        tracer_ligne_droite(n-1,x+1,y+1)
        triangle(n-1,x-1,y+1)
def tracer(x,y):
    for i in range (0,n):
        print(" ")