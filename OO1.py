class SomeClass: #class 命名規則:雙大寫 #其他變數:用底線 ex: my_value
    pass #甚麼都不做 (不能不寫)

some_thing=SomeClass()

class User:
    def __init__(self,first,last,age): #初始化方法 雙底線! #類別裡面叫做方法，類別外叫做函式 #一定要有self參數 #first,last...>attribute
        self.first=first #物件裡面的first設成帶進來的first
        self.last=last
        self.age=age
        #共三個參數
user1= User("Joe","Smith",68)
print(user1.age)
#別的程式語言，初始化方法(寫在外面)


