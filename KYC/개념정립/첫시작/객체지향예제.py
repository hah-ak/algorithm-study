class Person: # 상속 및 메소드 오버라이딩 연습.
              # 오버라이딩 : 메소드 이름은 같으나, 부모 클래스와는 다른 기능을 수행함.
              # 오버로드 : 메소드의 파라미터가 다른경우(타입, 갯수)에 중복된 이름으로도 수행 할 수 있게 만드는 것.
    def getGender(self):
        return "unknown" 
class Male(Person):
    def getGender(self):
        return "Male"
class Female(Person):
    def getGender(self):
        return "Female"

s= Male.getGender("male")
f = Person.getGender("male")
print(f)