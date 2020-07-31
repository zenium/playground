class level1(object):
    def __init__(self):
        self.x = 10
        self.y = 20

    def plus(self, x, y):
        return self.x+self.y

    def output(self):
        print(">>%s, %s" % (self.x, self.y))

class level2(level1):
    def __init__(self):
        super(level2, self).__init__()
        self.minus()

    @classmethod
    def minus(cls):
        cls.x