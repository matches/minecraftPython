from mcpi.minecraft import Minecraft
mc=Minecraft.create()
dadId=mc.getPlayerEntityId('tron2112')
import random, time
count=1
mc.postToChat('tp in 5!')
time.sleep(5)


def findAir(x,z):
    return 64

while count<= 10:
    x=random.randint(-127, 127)
    y=random.randint(, 90)
    z=random.randint(-127, 127)
    mc.entity.setPos(dadId,x,y,z)
    time.sleep(5)
    count+=1




