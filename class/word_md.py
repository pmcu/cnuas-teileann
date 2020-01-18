class Word:
    num_of_wrds = 0
    line = "---\n"
    fm1 = "layout:"
    fm2 = "ainm:"
    fm3 = "rann:"


    def __init__(self, layt, wrd, rann):
        self.layt = layt
        self.wrd = wrd
        self.rann = rann

        # self.email = first + '.' + last + '@company.com'

        Word.num_of_wrds += 1

    def cur_ann(self):
        return '---\n{} {}\n{} {}\n{} {}\n---\n# {}'.format(self.fm1, self.layt, self.fm2, self.wrd, self.fm3,self.rann,self.wrd)





wrd_1 = Word('default','cat','ainmfhocal')
wrd_2 = Word('default','cuir','briathar')
wrd_3 = Word('default','bán','aidiacht')

print(wrd_1.cur_ann())
