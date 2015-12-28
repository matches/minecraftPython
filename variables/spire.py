from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos=mc.entity.getTilePos(130864)
x=pos.x
y=pos.y
z=pos.z
height=3
block=1, 5
side= height
mc.setBlocks(x+1, y, z+1, x+3, y+side-1,z+3, block)
point=6
mc.setBlocks(x+2, y, z+2, x+2, y+point-1, z+2, block)
base=2
mc.setBlocks(x, y, z, x+4, y+base-1, z+4, block)

