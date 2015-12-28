from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.entity.getPos(780)
x=pos.x
y=pos.y
z=pos.z
width= 9
height= 6
length= 5
cube= 45
air= 0
mc.setBlocks(x, y, z, x+width, y+height, z+length, cube)
mc.setBlocks(x+1, y, z+1, x+width-1, y+height, z+length-1, air)
