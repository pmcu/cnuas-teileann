class Word:

    def __init__(self, ainm, leagan, bearla, rann, sampla):

        self.ainm = ainm
        self.leagan = leagan
        self.bearla = bearla
        self.rann = rann
        self.sampla = sampla

    def leag(self):
        return '- ainm: {}\n  leagan: {}\n  bearla: {}\n  rann: {}\n  sampla: {}\n'\
        .format(self.ainm, self.leagan, self.bearla, self.rann, self.sampla)

        # self.email = first + '.' + last + '@company.com'

v1 = input("focal le do thoil: ")
v2 = input("leagan le do thoil: ")
v3 = input("béarla le do thoil: ")
v4 = input("rann cainte le do thoil: ")
v5 = input("sampla le do thoil: ")

wrd_3 = Word(v1,v2,v3,v4,v5)

cur = wrd_3.leag()
f = open("_data/focloir.yml","a")
f.write(cur)
