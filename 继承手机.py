import time
class OldPhone:
    __brand=""
    def setBrand(self,brand):
        self.__brand=brand
    def getBrand(self):
        return self.__brand
    def call(self,content):
        print("正在给",content,"打电话...")
        for i in range(3):
            print(".", end="")
            time.sleep(1)

class NewPhone(OldPhone):

    def call(self,content):
        super().call(content)
        print("语音通话中...")
    def newbrand(self):
        print("品牌为:",self.getBrand(),"的手机很好用...")

n=NewPhone()
n.setBrand("华为")
n.call("tom")
n.newbrand()