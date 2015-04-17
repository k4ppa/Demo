
from mobile_framework.android_device import AndroidDevice

import stormtest.ClientAPI as StormTest
from assistance_menu import AssistanceMenu
from stormtest.ClientAPI import PressButton


if __name__ == '__main__':
    
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    assistanceMenu = AssistanceMenu()
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(3)
    
    
    assistanceMenu.open()
    assistanceMenu.up()
    assistanceMenu.settings()
    
    PressButton("SWIPE:220:110:220:760:0")
    PressButton("SWIPE:220:110:220:760:0")
    PressButton("SWIPE:220:110:220:760:0")
    StormTest.WaitSec(1)
    galaxyTab3.tap(text='Wi-Fi')
    
    
    StormTest.WaitSec(2)
    assistanceMenu.open()
    assistanceMenu.down()
    StormTest.WaitSec(1)
    assistanceMenu.close()
    
    
    StormTest.WaitSec(1)
    galaxyTab3.stop()
    pass


