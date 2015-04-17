
from mobile_framework.android_device import AndroidDevice

import stormtest.ClientAPI as StormTest
from assistance_menu import AssistanceMenu
from network_functions import connectToTheNetwork, disconnectToTheNetwork


if __name__ == '__main__':
    
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    galaxyTab3.start('it.sky.river')
    assistanceMenu = AssistanceMenu()
    StormTest.WaitSec(3)
    
    connectToTheNetwork(galaxyTab3, assistanceMenu)
    
    
    
    
    
    disconnectToTheNetwork(galaxyTab3, assistanceMenu)
    StormTest.WaitSec(1)
    galaxyTab3.stop()
    pass


