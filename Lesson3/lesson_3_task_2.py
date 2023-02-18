from smartphone import Smartphone

ind1 = Smartphone("Siemens", "C40", "+78945612378")
ind2 = Smartphone("Nokia", "A60", "+77777777777")
ind3 = Smartphone("Sony", "T100", "+78888888888")
ind4 = Smartphone("Motorolla", "C20", "+79999999999")
ind5 = Smartphone("Samsung", "B30", "+76666666666")

catalog = [ind1, ind2, ind3, ind4, ind5]

for i in range(0, len(catalog)):
    print(catalog[i])

ind1.print_i()