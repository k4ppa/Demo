
from stormtest.ClientAPI import PressButton
import stormtest.ClientAPI as StormTest


def connectToTheNetwork(galaxyTab3, assistanceMenu):
    goToSettings(assistanceMenu)
    goToWiFi(galaxyTab3)
    galaxyTab3.tap(text='Vodafone-WIFI')
    enterPassword()
    galaxyTab3.tap(text='Connect')
    StormTest.WaitSec(5)
    closeSettings(assistanceMenu)
    pass


def goToSettings(assistanceMenu):
    assistanceMenu.open()
    assistanceMenu.up()
    assistanceMenu.settings()
    pass


def goToWiFi(galaxyTab3):
    PressButton("SWIPE:220:110:220:760:0")
    PressButton("SWIPE:220:110:220:760:0")
    PressButton("SWIPE:220:110:220:760:0")
    StormTest.WaitSec(1)
    galaxyTab3.tap(text='Wi-Fi')
    StormTest.WaitSec(1)
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



def disconnectToTheNetwork(galaxyTab3, assistanceMenu):
    goToSettings(assistanceMenu)
    goToWiFi(galaxyTab3)
    galaxyTab3.tap(text='Vodafone-WIFI')
    StormTest.WaitSec(2)
    galaxyTab3.tap(text='Forget')
    StormTest.WaitSec(5)
    closeSettings(assistanceMenu)
    pass


def closeSettings(assistanceMenu):
    assistanceMenu.open()
    StormTest.WaitSec(2)
    assistanceMenu.down()
    StormTest.WaitSec(1)
    assistanceMenu.back()
    StormTest.WaitSec(1)
    assistanceMenu.close()
    pass