class Centipede():
    def __init__(self):
        self.legs = []
        self.stomach = []

    def __call__(self, arg):
        self.stomach.append(arg)

    def __str__(self):
        return ",".join(self.stomach)

    def __repr__(self):
        return ",".join(self.legs)

    def __setattr__(self, key, value):
        if key in [ "stomach", "legs"] and key in self.__dict__.keys():
            raise AttributeError("{0} is for internal use only".format(key))
        else:
            self.__dict__[key] = value
            if key not in [ "stomach", "legs"]:
                self.legs.append(key)
