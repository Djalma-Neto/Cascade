import os

for i, f in enumerate(os.listdir("negativas")):
    f_new = '{}.jpg'.format(i)
    os.rename(f, f_new)
    print ("{}.".format(i), f, '->', f_new)

print("RENOMEAR FINALIZADO !!!")
