
from mobile_framework.android_device import AndroidDevice

import stormtest.ClientAPI as StormTest
from assistance_menu import AssistanceMenu
from stormtest.ClientAPI import PressButton







def restoreDefaultState(assistanceMenu):
    assistanceMenu.open()
    StormTest.WaitSec(1)
    assistanceMenu.down()
    StormTest.WaitSec(1)
    assistanceMenu.close()
    pass


def closeSettings(assistanceMenu):
    assistanceMenu.open()
    StormTest.WaitSec(1)
    assistanceMenu.down()
    StormTest.WaitSec(1)
    assistanceMenu.back()
    StormTest.WaitSec(1)
    assistanceMenu.close()
    pass


def goToWiFi(galaxyTab3):
    PressButton("SWIPE:220:110:220:760:0")
    PressButton("SWIPE:220:110:220:760:0")
    PressButton("SWIPE:220:110:220:760:0")
    StormTest.WaitSec(1)
    galaxyTab3.tap(text='Wi-Fi')
    pass


def goToSettings(assistanceMenu):
    assistanceMenu.open()
    assistanceMenu.up()
    assistanceMenu.settings()
    pass


def enterPassword():
    StormTest.WaitSec(2)
    PressButton("TAP:55:680")
    StormTest.WaitSec(1)
    PressButton("TAP:55:680")
    StormTest.WaitSec(1)
    
    for i in range(3):
        PressButton("TAP:570:600:0")
        StormTest.WaitSec(1)
        PressButton("TAP:790:600:0")
        StormTest.WaitSec(1)
        PressButton("TAP:860:680:0")
        StormTest.WaitSec(1)
    pass
    


if __name__ == '__main__':
    
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.start('it.sky.river')
    assistanceMenu = AssistanceMenu()
    StormTest.WaitSec(3)
    
    
    goToSettings(assistanceMenu)
    goToWiFi(galaxyTab3)
    
    galaxyTab3.tap(text='Vodafone-WIFI')
    
    '''
    if galaxyTab3.tap(text='Forget'):
        StormTest.WaitSec(2)
        galaxyTab3.tap(text='Vodafone-WIFI')
    '''
    
    enterPassword()
    galaxyTab3.tap(text='Connect')
    
    StormTest.WaitSec(5)
    closeSettings(assistanceMenu)
    
    #StormTest.WaitSec(5)
    #restoreDefaultState(assistanceMenu)
    
    
    StormTest.WaitSec(1)
    galaxyTab3.stop()
    pass


