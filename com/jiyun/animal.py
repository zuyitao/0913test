class Animal:
    ani_count=0;
    def __init__(self,color,eat,tizhong):
        self.color=color;
        self.eat=eat;
        self.tizhong=tizhong;
        Animal.ani_count+=1;

    def ani_mothed(self):
        print("颜色:",self.color,"吃：",self.eat,"体重：",self.tizhong);

class Cat(Animal):
    def setname(self,name):
        self.name=name;
        print("名字：",self.name)

class Dog(Animal):
    def setzuoyong(self,zuoyong):
        self.zuoyong=zuoyong;
        print("作用：",self.zuoyong)