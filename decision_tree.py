class DT:
    def __init__(self, attribute = None, boundary = None, left = None, right = None, decision = None):
        self.attribute = attribute
        self.boundary = boundary
        self.left = left
        self.right = right
        self.decision = decision      
    def check(self, jd_description):        
        if self.decision == 'No' or self.decision == 'Yes':
            return self.decision
        if jd_description[self.attribute] < self.boundary:
            return self.left.check(jd_description)
        else:
            return self.right.check(jd_description) 
        

# Leaf nodes -> Yes or No 
NO = DT(decision='No')
YES = DT(decision='Yes')

#distance_dt = DT('distance', 40, YES, NO)
nightshift_dt = DT('nightshift', 1, YES, NO) # 0(no nightshift), 1(nightshift)
wfh_dt = DT('wfh', 1, NO, nightshift_dt) # 0(no wfh), 1(wfh allowed)
salary_dt = DT('salary', 1000, NO, wfh_dt)

jd_description = {
    'salary': 2000,
    'wfh': 1,
    'nightshift': 0
}

print(f"Decision to access job offer ->  {salary_dt.check(jd_description)}")       