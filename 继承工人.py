class Person:
    __username = ""
    __age = 0
    __sex = ""


    def setSex(self,sex):
        if sex  != "男" and sex != "女":
            print("你是泰国人？")
        else:
            self.__sex = sex

    def getSex(self):
        return self.__sex


    def setAge(self,age):
        if age > 120 or  age < 0:
            print("输入非法！别瞎弄!")
        else:
            self.__age = age

    def getAge(self):
        return self.__age


    def setUsername(self,username):
        if username == "":
            print("姓名不能为空！")
        else:
            self.__username = username

    def getUsername(self):
        return self.__username

class Worker(Person):
    def worked(self,workes):
        print("一个叫",super().getUsername(),"性别",super().getSex(),"的工人",workes)

class Student(Worker,):
    __no=""
    def setNo(self,no):
        if no == "":
            print("姓名不能为空！")
        else:
            self.__no = no

    def getNo(self):
        return self.__no
    def worked(self, workes):
        super().worked(workes)
    def working(self,workes):
        print("一个叫",super().getUsername(),"性别",super().getSex(),"学号为",self.__no,"的学生会",workes)

w=Student()
w.setUsername("可可")
w.setSex("男")
w.setAge(18)
w.setNo(3100)
w.worked("干苦力")
w.working("学习，唱歌")