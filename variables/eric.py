from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

# 11, 104, 48

def cubeOStuff(x,y,z,blockId):
    mc.postToChat('Transmogrify!')
    time.sleep(5)
    mc.setBlocks(x,y,z, x+5, y+5, z+5, blockId)

def footsteps(blockId, state=0):
    count=1
    while count<= 35:
        pos=mc.entity.getPos(mc.getPlayer)
        mc.setBlock(pos.x,pos.y-1,pos.z, 46, 1)
        time.sleep(0.5)
        count+=1

def trainingGround(pos):
    mc.setBlocks(pos.x, pos.y+20, pos.z, pos.x+100, pos.y+21, pos.z+100, 2)


#cubeOStuff(11, 104, 48, 0)
#trainingGround(mc.player.getPos())
#footsteps(20)

print(mc.getPlayerEntityId('tron2112'))
print(mc.getPlayerEntityId('matches42'))

#tp dad back to -200, 68, 185
print(mc.getPlayerEntityIds())
    
