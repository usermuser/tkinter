from time import sleep
from snap7 import client as s7


def plc_connect(ip, rack, slot, stop_tries, freq):
    plc = s7.Client()
    tries = 1
    while tries < stop_tries and not plc.get_connected():
        try:
            print('trying for connecting to PLC ...')
            sleep(freq)
            plc.connect(ip, rack, slot)
            return True

        except Exception as e:
            logger.error("warning in PLC connection >>{}".format(e))
            sleep(freq)

            if tries == (stop_tries - 1):
                print('error in plc connection')
                return False

        tries += 1
    return False


def data_reader():
    plc = s7.Client()
    try:
        result, data_items = plc.read_multi_vars(data_items)
        return result, data_items
    except Exception as e:
        print('warning:>>{}'.format(e))
