from InfiniteFlightConnectOld import *

for i in range(500):
    print(send_command("Airplane.GetState", [], await_response=True))