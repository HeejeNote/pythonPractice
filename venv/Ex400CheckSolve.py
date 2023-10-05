class FourCal:
    def setdata(sel, flr, sec):
        sel.flr = flr
        sel.sec = sec
    def add(sel):
        result = sel.flr + sel.sec
        return result

a = FourCal()
a.setdata(4, 2)
print(a.add())