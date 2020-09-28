class SomeClass: #class 命名規則:雙大寫 #其他變數:用底線 ex: my_value
    pass #甚麼都不做 (不能不寫)

some_thing=SomeClass()

class User:
    active_users=0 #類別的attribute
    def __init__(self,first,last,age): #初始化方法 雙底線! #類別裡面叫做方法，類別外叫做函式 #一定要有self參數 #first,last...>attribute
        self.first=first #物件裡面的first設成帶進來的first
        self.last=last
        self.age=age
        self._name="Hello" #加底線 >>private
        self.__name="Hello" #雙底線>>外面無法拿取值
        User.active_users+=1
        #共三個參數
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"


user1= User("Joe","Smith",68)
print(user1.age)
#別的程式語言，初始化方法(寫在外面
print(user1._User__name)  #這樣才可以拿

print(user1.full_name())
print(user1.likes("flower"))

print(User.active_users)
print(user1.active_users)
user1.active_users=300  #指向不同attribute
print("################")
print(User.active_users)
print(user1.active_users)

user1.sex="male" #可隨時加
print(user1.sex)