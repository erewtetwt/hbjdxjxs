def main():

    class Buffer:
        def __init__(self, size):
            self.len=size
            self.data=[None]*size            
            self.start=0
            self.end=0           

        def add(self, element):
            if self.start==self.end and self.data[0]!=None:
                print("Буфер полон. Запись запрещена.")
            else:            
                self.data[self.start]=element
                if self.start==self.len-1:
                    self.start=0
                else:
                    self.start+=1
                print(self.data)
            
        def take(self):
            if self.data[self.end]==None:
                print("Буфер пуст")
            else:
                if self.end==self.len-1:
                    self.data[self.end]=None
                    self.end=0              
                else:
                    self.data[self.end]=None
                    self.end+=1                    
                print(self.data)
                

    Buf=int(input("Длина буфера = ")) 
    Ring=Buffer(Buf)
    
    cho=int(input("Добавить(1), Удалить(2), Выйти(3)"))
    while cho==1 or cho==2:
        if cho==1:
            x=int(input("Элемент буфера = "))
            Ring.add(x)
        if cho==2:
            Ring.take()
        cho=int(input("Добавить(1), Удалить(2), Выйти(3)"))
    
main()
        

        
