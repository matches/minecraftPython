from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Earth: Hello")
position = mc.player.getTilePos()
pos=mc.entity.getTilePos(780)
x= pos.x
y=pos.y-1
z=pos.z
fun=12
#mc.setBlock(x, y, z, 8)
y=pos.y+26
#mc.entity.setTilePos(780, x, y, z)


