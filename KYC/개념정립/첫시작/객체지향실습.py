class Person:#객체 생성을 위한 템플릿
    # 클래스 내에서의 메서드를 바로 만들 수 있다. ex)count를 변수 처럼 선언해 Person.count로 내부에서 사용가능.
    def __init__(self, name,age,height): # 생성자, self는 클래스에 의해 생성된 객체공간
        self.__name = name #__는 private을 말한다.
        self.__age = age
        self.__height = height
    
    @property # 데코레이터, 변수 이름과 같은 메서드를 만들어 getter,setter로 사용가능
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,height):
        self.__height = height

    def __repr__(self):
        return "{},{},{},{}".format(self.__class__.__name__, self.name, self.age, self.height)

Persons = [Person("Kim",5,155),Person("Lee",8,188),Person("Park",4,144)]

for person in sorted(Persons,key = lambda x : x.name,reverse=True): #이름으로 내림차순정렬
    print(person)

for person in sorted(Persons,key = lambda x : x.height,reverse=True):#키로 내림차순정렬
    print(person)