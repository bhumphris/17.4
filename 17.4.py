class point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)

p1 = point(4,5)
p2 = point(1,1)

p3 = p1 + p2

print ('\nThe values for the point, p1 are: '),
print p1

print ('\nThe values for the point, p2, are: '),
print p2

print ('\nWhen the points are added together, the sum is: '),
print p3

