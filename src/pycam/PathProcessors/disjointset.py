class DisjointSet(object) :
    def __init__(self) :
        self.values = set()
        self.representatives = {}
    def add(self, value) :
        self.values.add(value)
        self.representatives[value] = value
    def union(self, value, other_value) :
        # repr of 1st value become repr of 2nd value too
        self.representatives[self.find(other_value)] = \
            self.representatives[self.find(value)]
    def find(self, value) :
        while self.representatives[value] != self.representatives[self.representatives[value]] :
            self.representatives[value] = self.representatives[self.representatives[value]]
        return self.representatives[value]
        #other way to do it but less clear and equally faster
        #this_repr = self.representatives[value]
        #repr_of_this_repr = self.representatives[this_repr]
        #while this_repr != repr_of_this_repr :
            #self.representatives[this_repr] = self.representatives[repr_of_this_repr]
            #this_repr = self.representatives[this_repr]
            #repr_of_this_repr = self.representatives[this_repr]
        #return this_repr
    def select(self, value) :
        rep = self.find(value)
        return filter(lambda val : self.find(val) == rep, self.values)
    def retrieve(self) :
        return filter(lambda val : self.find(val) == val, self.values)
    def card(self, value) :
        return len(self.select(value))
    def disp(self) :
        print('Disjoint set')
        print(' '.join('{0}'.format(self.representatives[value], 3) for value in self.values))
        print(' '.join('{0}'.format(value, 3) for value in self.values))
