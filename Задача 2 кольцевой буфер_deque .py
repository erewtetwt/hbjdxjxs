def main():

    from collections import deque

    class Buffer:
        def __init__(self, size: int):
            self.size = size
            self.data = deque([], maxlen=size)

        def add(self, value):
            if len(self.data) == self.size:
                print("Буфер полон. Перезаписано последнее значение.")
            self.data.append(value)
            print (self.data)

        def take(self):
            if len(self.data) == 0:
                print("Буфер пуст")
                return()
            print (self.data)
            return self.data.popleft()
        
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
        

        
