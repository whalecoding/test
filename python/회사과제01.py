class SchoolPerson: 
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_details(self):
        print('name :',self.name,'\n'+'id :',self.id)

# 괄호 안에 부모 클래스를 넣어 상속해주었습니다.
class Teacher(SchoolPerson): 
    def __init__(self, name, id, major):
        # 부모 클래스에 정의된 함수 재사용
        super().__init__(name, id)
        self.major=major
    def show_details(self):
        print('name :',self.name,'\n'+'id :',self.id,'\n'+'major :',self.major)

# 괄호 안에 부모 클래스를 넣어 상속해주었습니다.
class Student(SchoolPerson):
  def __init__(self,name,id):
    # 부모 클래스에 정의된 함수 재사용
    super().__init__(name, id)
    self.credits = 0
    self.courses = {}
  def enroll_course(self, hours, teacher):
    self.credits += hours
    value = {}
    value['hours'] = hours
    value['teacher'] = teacher.name
    self.courses[teacher.major] = value
  def show_details(self):
    # 부모 클래스에 정의된 함수 재사용
    super().show_details()
    for key in self.courses.keys():
      print('course name: {}'.format(key))
      print('hours: {} teacher: {}'.format(self.courses[key]['hours'], self.courses[key]['teacher']))
    print('total credits: {}'.format(self.credits))

  def __str__(self):
    return 'credits: {}\n{}'.format(self.credits, self.courses)
  

sp = SchoolPerson('mark','011')
sp.show_details()

tch1 = Teacher('john','014','English')
tch1.show_details()

s1 = Student('Jane', '011')
s1.enroll_course(3, tch1)
print(s1)

s1 = Student('Jane', '011')
s1.enroll_course(3, tch1)
print(s1)

tch2 = Teacher('Mary', '015', 'Math')
s1.enroll_course(4, tch2)
print(s1)
s1.show_details()

###############

class PointN:
    def __init__(self, *args):
      # args 로 받은 인자들을 v 라는 변수에 저장
      self.v = args
      print(self.v)
      
    def __len__(self):
      return len(self.v)
    def __getitem__(self,idx):
      return self.args[idx]
      
    def __add__(self, other):
      temp = list(map(lambda x, y: x+y, self.v, other.v))
      return self._getStr(temp)
    def __sub__(self, other):
      temp = list(map(lambda x, y: x-y, self.v, other.v))
      return self._getStr(temp)
    def __neg__(self):
      temp = list(map(lambda x: -x, self.v))
      return self._getStr(temp)
    def __lt__(self, other):
      # 빼기를 하여 -값이 나오는 항목이 하나라도 있으면 False 를 반환하고, 모두 + 값이 나오면 True를 반환
      temp = list(map(lambda x, y: x-y, self.v, other.v))
      temp = list(filter(lambda x: x < 0, temp))
      if(len(temp) > 0):
        return False
      else:
        return True
        
    def __str__(self):
      # print 시 자동 호출
      return self._getStr(self.v)
      
    def _getStr(self, v):
      # 출력하기 위한 문자열 형식을 만들어주는 함수
      string_ints = [str(int) for int in v ]
      s = ' '.join(string_ints)
      return 'Point is at ({})'.format(s)
list1 = PointN(2,4,5,3,5,4)
list2 = PointN(4,1,2,9,7,5)
print(list1)
print(list1+list2)
print(list1-list2)
print(-list2)
print(list1>list2)
