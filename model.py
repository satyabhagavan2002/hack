class Model:
    def __init__(self, theta):
        self.w1 = 0
        self.w2 = 0
        self.w3=0
        self.theta = theta

    def predict(self, a, b,c):
        yin = self.w1 * a + self.w2 * b+self.w3*c
        if yin >= self.theta:
            return 1
        return 0

    def train(self, inpt, output):
        for i in range(-6, 6):
            for j in range(-6, 6):
                for k in range(-6,6):
                    temp = []
                    self.w1 = i
                    self.w2 = j
                    self.w3=k
                    for f in inpt:
                        temp.append(self.predict(f[0], f[1],f[2]))
                    if temp == output:
                        return
                        
