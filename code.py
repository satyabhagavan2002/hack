from model import Model

# ------And-------
And = Model(3)
inpt_and = [[0, 0,0], [0, 0,1], [0, 1,0], [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
output_and = [0,0,0,0,0,0,0,1]
And.train(inpt_and, output_and)
for p in inpt_and:
    print("And of ",p[0],p[1],p[2],": ",And.predict(p[0],p[1],p[2]))

# -------OR--------
Or=Model(1)
inpt_or=[[0, 0,0], [0, 0,1], [0, 1,0], [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
output_or=[0,1,1,1,1,1,1,1]
Or.train(inpt_or,output_or)
for p in inpt_or:
    print("or of ",p[0],p[1],p[2],": ",Or.predict(p[0],p[1],p[2]))

# ------Nand-------
Nand = Model(-2)
inpt_nand = [[0, 0,0], [0, 0,1], [0, 1,0], [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
output_nand = [1,1,1,1,1,1,1,0]
Nand.train(inpt_nand, output_nand)
for p in inpt_nand:
    print("nand of ",p[0],p[1],p[2],": ",Nand.predict(p[0],p[1],p[2]))

# -------NOR--------
Nor=Model(0)
inpt_nor=[[0, 0,0], [0, 0,1], [0, 1,0], [0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
output_nor=[1,0,0,0,0,0,0,0]
Nor.train(inpt_nor,output_nor)
for p in inpt_nor:
    print("Nor of ",p[0],p[1],p[2],": ",Nor.predict(p[0],p[1],p[2]))

