from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
mc.postToChat("5 sec till tour")
time.sleep(5)
x=0.5
y=999
z=8.5
mc.entity.setPos(780, x, y, z)
#65 63 28041 water temple and night vision
time.sleep(25)
x=-419.4
y=73
z=-274.072
mc.entity.setPos(780, x, y, z)
time.sleep(10)
x=65
y=63
z=28041
mc.entity.setPos(780, x, y, z)


