import numpy as np
class estadistica: #crear clase para luego llamar con un st.funcion()
    def __init__(self,x):
        self.x=x
    def promedio(self): # aqui en la funcion no va (self,x) sino solo self
        n=len(self.x)#cuantos elementos hay de la lista
        promedio=sum(self.x)/n
        return promedio
    def varianza(self):
        n=len(self.x)
        sigma2=sum((self.x-self.promedio(self.x))*(self.x-self.promedio(self.x)))/(n-1)
        return sigma2
    def minimo(self):
        minx=9E99
        for a in self.x:
            if a <minx:
                minx=a
        return minx
    def maximo(self):
        maxx=-9E99
        for a in self.x:
            if a >maxx:
                maxx=a
        return maxx