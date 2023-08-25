# 책으로 보고 animal human 똑같이 구현하기
# 쭉하기 


class Animal:
    def __init__(self):
        self.flagLife = True
        def die(self):
            self.flagLife=False
            
ani = Animal()
print("flagLife",ani.flagLife)
ani.die()
print("flagLife",ani.flagLife)

       

class Human(Animal):
    job = "백수"
   
    def chippo(self, job):
        self.job = job

class OopTest:
    ani=Animal()
    print("ani-flagLife:",ani.flagLife)
    ani.die()
    print("ani-flagLife:",ani.flagLife)
    
    print("---------------------")
    
    hum=Human()
    print("hum-flagLife:",hum.flagLife)
    print("job:",hum.job)
    
    hum.die()
    hum.chippo("프로그래머")
    print("hum-flagLife:",hum.flagLife)
    print("job:"+hum.job)
    
    
    

       
