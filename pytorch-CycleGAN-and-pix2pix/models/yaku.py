# upper
a = 0.3
class ReLU(Threshold):
    def __init__(self, inplace=False):
        super(ReLU, self).__init__(-a, 0, inplace)

    def extra_repr(self):
        inplace_str = 'inplace' if self.inplace else ''
        return inplace_str

# downer
a = 0.3
class ReLU(Threshold):
    def __init__(self, inplace=False):
        super(ReLU, self).__init__(a, 0, inplace)

    def extra_repr(self):
        inplace_str = 'inplace' if self.inplace else ''
        return inplace_str

# meta_no_ceil
a = 0.3
k = 100000
class ReLU(Module):
    def __init__(self, inplace=False):
        super(ReLU, self).__init__()
        self.inplace = inplace

    def forward(self, input):
        F.threshold(input, F.sin(input * k) * a, 0, self.inplace)

    def extra_repr(self):
        inplace_str = 'inplace' if self.inplace else ''
        return inplace_str

# meta
a = 0.3
k = 100000
class ReLU(Module):
    def __init__(self, inplace=False):
        super(ReLU, self).__init__()
        self.inplace = inplace

    def forward(self, input):
        return F.threshold(input + (torch.ceil(torch.sin(input * k)) - 0.5) * a * 2, 0, 0, self.inplace)

    def extra_repr(self):
        inplace_str = 'inplace' if self.inplace else ''
        return inplace_str

# meta
a = 0.3
k = 100000
class ReLU(Module):
    def __init__(self, inplace=False):
        super(ReLU, self).__init__()
        self.inplace = inplace

    def forward(self, input):
        return F.threshold(input + (torch.ceil(torch.cos(input * k)) - 0.5) * a * 2, 0, 0, self.inplace)

    def extra_repr(self):
        inplace_str = 'inplace' if self.inplace else ''
        return inplace_str