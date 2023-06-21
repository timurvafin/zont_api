import sys
from zont_api import ZontAPI

if len(sys.argv) < 4:
    print("Usage: python script.py <username> <password> <dev_id>")
    sys.exit(1)

zont_username = sys.argv[1]
zont_password = sys.argv[2]
dev_id = int(sys.argv[3])

api = ZontAPI(zont_username, zont_password, dev_id, log_requests=True)

print("\n\nGET THERMOMETERS")
thermometer_data = api.get_thermometers()
print(f"Thermometer data: {thermometer_data}")

print("\n\nENABLE DHW")
response = api.enable_dhw()
if response:
    print("Enabled DHW successfully")
else:
    print("Failt to enable DHW")

print("\n\nDISABLE DHW")
response = api.disable_dhw()
if response:
    print("Disabled DHW successfully")
else:
    print("Failt to disable DHW")
