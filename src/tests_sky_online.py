
import stormtest.ClientAPI as StormTest
from stormtest.ClientAPI import PressButton



def enterEmail(galaxyTab3):
    galaxyTab3.tap(text='Indirizzo mail. Editing.')
    StormTest.WaitSec(1)
    PressButton("TAP:450:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:110:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:625:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:850:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:960:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:1070:680:0") #.
    StormTest.WaitSec(1)
    PressButton("TAP:400:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:1015:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:110:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:625:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:960:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:510:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:60:755:0") #Sym
    StormTest.WaitSec(1)
    PressButton("TAP:110:600:0") #@
    StormTest.WaitSec(1)
    PressButton("TAP:60:755:0") #Sym
    StormTest.WaitSec(1)
    PressButton("TAP:110:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:1015:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:510:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:400:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:110:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:735:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:1070:680:0") #.
    StormTest.WaitSec(1)
    PressButton("TAP:400:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:960:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:850:680:0")
    StormTest.WaitSec(1)
    pass



def enterPassword(galaxyTab3):
    galaxyTab3.tap(text='Enter password.. Double tap to edit.')
    StormTest.WaitSec(1)
    PressButton("TAP:110:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:1015:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:510:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:400:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:110:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:735:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:60:680:0") #shift
    StormTest.WaitSec(1)
    PressButton("TAP:220:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:900:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:625:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:60:680:0") #shift
    StormTest.WaitSec(1)
    PressButton("TAP:960:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:735:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:1015:610:0")
    StormTest.WaitSec(1)
    PressButton("TAP:850:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:735:680:0")
    StormTest.WaitSec(1)
    PressButton("TAP:285:530:0")
    StormTest.WaitSec(1)
    PressButton("TAP:65:460:0") # 1
    StormTest.WaitSec(1)
    PressButton("TAP:195:460:0") # 2
    StormTest.WaitSec(1)
    PressButton("TAP:320:460:0") # 3
    StormTest.WaitSec(1)
    pass


def login(galaxyTab3):
    galaxyTab3.tap(mappedText='openMenu')
    StormTest.WaitSec(1)
    
    enterEmail(galaxyTab3)
    enterPassword(galaxyTab3)
    galaxyTab3.tap(text='Accedi')
    StormTest.WaitSec(7)
    pass


def logout(galaxyTab3):
    galaxyTab3.tap(mappedText='openMenu')
    StormTest.WaitSec(1)
    galaxyTab3.tap(text='Logout')
    StormTest.WaitSec(1)
    galaxyTab3.tap(mappedText='closeMenu')
    StormTest.WaitSec(1)
    pass




