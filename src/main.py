
from mobile_framework.android_device import AndroidDevice

import stormtest.ClientAPI as StormTest
from assistance_menu import AssistanceMenu


if __name__ == '__main__':
    
    galaxyTab3 = AndroidDevice("samsung_galaxy_tab_3")
    assistanceMenu = AssistanceMenu()
    galaxyTab3.start('it.sky.river')
    StormTest.WaitSec(3)
    
    
    assistanceMenu.open()
    assistanceMenu.down()
    assistanceMenu.down()
    assistanceMenu.settings()
    assistanceMenu.close()
    
    
    assistanceMenu.open()
    assistanceMenu.up()
    assistanceMenu.up()
    assistanceMenu.close()
    
    galaxyTab3.stop()
    pass


