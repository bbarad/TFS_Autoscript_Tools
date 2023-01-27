from autoscript_sdb_microscope_client import SdbMicroscopeClient
import time
ip_address = '192.168.0.1' # depends on system setup
open_time = 1.5 # seconds
microscope = SdbMicroscopeClient()
microscope.connect(ip_address)
gis_port = microscope.gas.get_gis_port("Pt dep")
print(gis_port.get_temperature())
gis_port.open()
time.sleep(open_time)
gis_port.close()
