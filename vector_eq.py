class Vector2D:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def eq(self , other):
        data = self.x == other.x and self.y == other.y 
        if(data):
            return '같습니다'
        
        else:
            return '다릅니다'
    def __eq__(self , other):
        data = self.x == other.x and self.y == other.y 
        if(data):
            return '같습니다'
        
        else:
            return '다릅니다'

v1 = Vector2D(10,30)
v2 = Vector2D(10,20)
v3 = v1.eq(v2)
v4 =  v1==v2
print(v4)

# print((1,2) ==(1,2))

