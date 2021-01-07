# Using the digits 0 to 9 at most one time each, fill in the boxes to make all 3 number calculation are true
# () * 2 = () ()
# () * 4 = () ()
# () * 8 = () ()

class DigitSet(object):
    def __init__(self, s):
        self.digits=s

    def is_valid_row(self, x, y, z):
        s = {x,y,z}
        if len(s)<3:
            return False
        return True if len(self.digits.intersection(s))==3 else False

    def is_answer(self, rows):
        l = []
        [l.extend(row) for row in rows]
        return True if len(set(l))==9 else False

def plus_func(x, times):
    return x * times // 10, x * times % 10

if __name__ == '__main__':
    all_digits=[*range(10)]
    ds = DigitSet(set(all_digits))

    # candidate rows
    candi_times={2:[],4:[],8:[]}
    for times in [2,4,8]:
        for x in all_digits:
            y,z = plus_func(x,times)
            if ds.is_valid_row(x, y, z):
                #print('{} * {} = {}{}'.format(x, times, y, z))
                candi_times[times].append(x)
    # seek answer
    for x0 in candi_times[2]:
        for x1 in candi_times[4]:
            for x2 in candi_times[8]:
                if x0==x1 or x1==x2 or x0==x2:
                    continue
                y0, z0 = plus_func(x0,2)
                y1, z1 = plus_func(x1, 4)
                y2, z2 = plus_func(x2, 8)
                if ds.is_answer([[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]]):
                    print('{} * {} = {}{}'.format(x0, 2, y0, z0))
                    print('{} * {} = {}{}'.format(x1, 4, y1, z1))
                    print('{} * {} = {}{}'.format(x2, 8, y2, z2))
