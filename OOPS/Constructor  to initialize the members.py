"""
Define a class Time with attributes hours, minutes and seconds as private members.Use constructor 
to initialize the members. Add the two-time objects by passing object as argument to add method 
and convert the same one by overloading the + operator.
"""
class Time:
    def __init__(self,x,y,z):
        if z>=60:
            y+=z//60
            z%=60
        if y>=60:
            x+=y//60
            y%=60
        self.__hrs=x
        self.__min=y
        self.__sec=z
    def display(self):
        print("Hours\tMinutes\tSeconds")
        print(self.__hrs,self.__min,self.__sec,sep='\t')
    def __add__(self,self2):
        return Time(self.__hrs+self2.__hrs,self.__min+self2.__min,self.__sec+self2.__sec)
t1=Time(int(input("Enter hours for time 1 : ")),
        int(input("Enter minutes for time 1 : ")),
        int(input("Enter seconds for time 1 : ")))
t2=Time(int(input("Enter hours for time 2 : ")),
        int(input("Enter minutes for time 2 : ")),
        int(input("Enter seconds for time 2 : ")))
print("Time 1 : ")
t1.display()
print("Time 2 : ")
t2.display()
res=t1+t2
print("Resultant time : ")
res.display()
