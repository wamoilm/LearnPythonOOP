class Phone:
    def __init__(self, model=None, make=None, os_feature=None):
        self.model = model
        self.make = make
        self.os_feature = os_feature

    # getter
    def get_model(self):
        return self.model

    # setter
    def set_model(self, new_value):
        self.model = new_value
        return self.model

    # getter
    def get_make(self):
        return self.make

    # setter
    def set_make(self, new_value):
        if self.make is None:
            self.make = new_value
        else:
            raise ValueError("Make is already set and cannot be changed")
        return self.make

    # getter
    def get_os_feature(self):
        return self.os_feature

    # setter
    def set_os_feature(self, new_value):
        self.os_feature = new_value
        return self.make


    def ring(self):
        print("Phone rings .. tring tring")

    def take_call(self):
        print("Phone takes call .. yap yap")

    def hangup_call(self):
        print("Call is over ... hang up")


