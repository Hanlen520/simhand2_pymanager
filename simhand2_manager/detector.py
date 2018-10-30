from whenconnect import when_connect, when_disconnect, start_detect
from pyatool import PYAToolkit
from .device_manager import add_device, remove_device
from .global_namespace import *


def start_device_detect():
    when_connect(device=DEVICE_LIST, do=install_simhand)
    when_connect(device=DEVICE_LIST, do=add_device)
    when_disconnect(device=DEVICE_LIST, do=remove_device)
    start_detect(with_log=False)


def install_simhand(device_id):
    logger.info('SIMHAND INSTALL', ver=SIMHAND_VER, id=device_id)
    toolkit = PYAToolkit(device_id)
    toolkit.install_from(r'https://github.com/williamfzc/simhand2/releases/download/{}/app-debug-androidTest.apk'.format(SIMHAND_VER))
    toolkit.install_from(r'https://github.com/williamfzc/simhand2/releases/download/{}/app-debug.apk'.format(SIMHAND_VER))
    logger.info('SIMHAND INSTALLED', ver=SIMHAND_VER, id=device_id)
