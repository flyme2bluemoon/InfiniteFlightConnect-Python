from InfiniteFlightConnect import *

print(send_command("Airplane.GetState", [], await_response=True))
print(send_command("Commands.ShowATCWindowCommand", []))