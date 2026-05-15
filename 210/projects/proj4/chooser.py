import stc
import trc
import rot_13

def crypt(msg, func):
    return func(msg)

# print(crypt("Ahoy, there!", stc.encrypt))
# print(crypt("hy hr!Ao,tee", stc.decrypt))

# print(crypt("Ahoy, there!", trc.encrypt))
# print(crypt("Aytrh,heo e!", trc.decrypt))

print(crypt("Ahoy, there!", rot_13.encrypt))
print(crypt("nubl, gurer!", rot_13.decrypt))