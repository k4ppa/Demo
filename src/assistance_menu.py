
import stormtest.ClientAPI as StormTest


class AssistanceMenu(object):


    def __init__(self):
        pass
    
    
    def up(self):
        StormTest.PressButton("TAP:1225:360:0")
        StormTest.WaitSec(1)
        pass


    def settings(self):
        StormTest.PressButton("TAP:1125:515:0")
        StormTest.WaitSec(1)
        pass
    
    
    def down(self):
        StormTest.PressButton("TAP:1225:535:0")
        StormTest.WaitSec(1)
        pass
    
    
    def open(self):
        StormTest.PressButton("TAP:1230:435:0")
        StormTest.WaitSec(1)
        pass
    
    
    def close(self):
        StormTest.PressButton("TAP:1270:450:0")
        StormTest.WaitSec(1)
        pass
        