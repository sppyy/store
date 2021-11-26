from  threading import Thread

import time
eggpool=0 #全局变量 蛋挞池子

class cooker(Thread): #定义一个厨师类
    cooker_name=""
    eggpool_sum=0
    def run(self)->None:#重构run方法
        global eggpool#调用全局变量
        start=time.time()#获取开始时间
        while True:
            end=time.time()#获取结束时间
            if end - start<60:#判断前后时间是否在60秒内
                if eggpool <500:#判断池子里蛋挞个数500以内
                    self.eggpool_sum=self.eggpool_sum+1#厨师做蛋挞的个数
                    eggpool=eggpool +1 #池子内蛋挞个数
                else:
                    time.sleep(3)#500以上停留3秒
            else:#大于60秒结束
                break
        return self.eggpool_sum


class customer(Thread):#定义一个顾客类
    customer_name=""
    money=5000.0
    many=0
    def run(self)->None:
        global  eggpool
        start=time.time() #开始时间
        while True:
            end=time.time() #结束时间
            if end - start<60:   #时间60秒
                if eggpool > 0:

                    if self.money >= 3:#余额大于3可购买
                        self.money = self.money - 3
                        eggpool = eggpool - 1
                        self.many = self.many + 1
                    else:#余额不足结束
                        break
                else:
                    time.sleep(2) #池子为空等待2秒
            else:
                break
        #print(self.customer_name,"一共抢了",self.many,"个蛋挞")
        return self.many

#调用线程
cooker1=cooker()
cooker1.cooker_name="厨师1"

cooker2=cooker()
cooker2.cooker_name="厨师2"

cooker3=cooker()
cooker3.cooker_name="厨师3"

customer1=customer()
customer1.customer_name="顾客1"

customer2=customer()
customer2.customer_name="顾客2"

customer3=customer()
customer3.customer_name="顾客3"
#customer3.money=5000

customer4=customer()
customer4.customer_name="顾客4"

customer5=customer()
customer5.customer_name="顾客5"

customer6=customer()
customer6.customer_name="顾客6"
#运行线程
cooker1.start()
cooker2.start()
cooker3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()

#闭塞线程
cooker1.join()
cooker2.join()
cooker3.join()
customer1.join()
customer2.join()
customer3.join()
customer4.join()
customer5.join()
customer6.join()


#会计结算
print(cooker1.cooker_name, "做出了", cooker1.eggpool_sum, "个蛋挞!","工资",cooker1.eggpool_sum*1.5)
print(cooker2.cooker_name, "做出了", cooker2.eggpool_sum, "个蛋挞!","工资",cooker2.eggpool_sum*1.5)
print(cooker3.cooker_name, "做出了", cooker3.eggpool_sum, "个蛋挞!","工资",cooker3.eggpool_sum*1.5)
print(customer1.customer_name,"一共抢了",customer1.many,"个蛋挞")
print(customer2.customer_name,"一共抢了",customer2.many,"个蛋挞")
print(customer3.customer_name,"一共抢了",customer3.many,"个蛋挞")
print(customer4.customer_name,"一共抢了",customer4.many,"个蛋挞")
print(customer5.customer_name,"一共抢了",customer5.many,"个蛋挞")
print(customer6.customer_name,"一共抢了",customer6.many,"个蛋挞")
