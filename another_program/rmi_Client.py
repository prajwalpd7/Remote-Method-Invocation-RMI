import Pyro4

cal_maker = Pyro4.core.Proxy('PYRO:Calculator@' + 'localhost' + ':8000')
print(cal_maker.add(1,3))
print(cal_maker.sub(12,3))