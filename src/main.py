
from mobile_framework.android_device import AndroidDevice

import stormtest.ClientAPI as StormTest





def up():
    StormTest.PressButton("TAP:1225:360:0")
    StormTest.WaitSec(1)
    pass

def settings():
    StormTest.PressButton("TAP:1125:515:0")
    StormTest.WaitSec(1)
    pass

def down():
    StormTest.PressButton("TAP:1225:535:0")
    StormTest.WaitSec(1)
    pass

def openAssistanceMenu():
    StormTest.PressButton("TAP:1230:435:0")
    StormTest.WaitSec(1)
    pass

def closeAssistanceMenu():
    StormTest.PressButton("TAP:1270:450:0")
    StormTest.WaitSec(1)
    pass


if __name__ == '__main__':
    
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(3)
    
    openAssistanceMenu()
    down()
    down()
    settings()
    closeAssistanceMenu()
    
    
    openAssistanceMenu()
    up()
    up()
    closeAssistanceMenu()
    
    galaxyTab3.stop()
    pass


