class Phone:
    def __init__(self, model, make, os_feature):
        self.model = model
        self.make = make
        self.os_feature = os_feature

    def ring(self):
        print("Phone rings .. tring tring")

    def take_call(self):
        print("Phone takes call .. yap yap")

    def hangup_call(self):
        print("Call is over ... hang up")


