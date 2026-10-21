from pycomm3 import LogixDriver

with LogixDriver('154.57.164.83:32630', init_tags=False, init_info=False) as plc:
    print(plc.info)