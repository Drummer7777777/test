class Figurs():
    count_corner=0
    radius=0
    has_pr_corner="no"

class Circle(Figurs):
    def __init__(self):
        print("Это круг")
    def pl(self,count_corner,radius,has_pr_corner):    
        print("Его площадь:", 3.14*int(radius)**2)
class Pryamougolnik(Figurs):
    def __init__(self):
        print("Это прямоугольник")
        print("Введите длины сторон:")
        global a,b
        a = int(input())
        b = int(input())
    def pl(self):
        print("Его площадь:", a*b)
        
