from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
count=1
while<=11
pos=mc.entity.getPos(130864)
x=pos.x
y=pos.y-1
z=pos.z

mc.setBlock(x,y,z, random.randint(1, 164))
count+=1
