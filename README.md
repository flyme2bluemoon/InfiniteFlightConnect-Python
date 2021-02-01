# Infinite Flight Connect API

Using python to connect to the Infinite Flight Connect API v1.

## Usage

Before getting started, make sure to enable the Infinite Flight command server in the app `Settings > General > Enable Infinite Flight Connect`

First, import the module in Python.
```py
import InfiniteFlightConnectOld
```

Then, to send a command, use the `send_command` function. The first parameter is the command, the second parameter are the parameters passed to Infinite Flight while the third parameter determines whether to wait for a response or not. Await response is false by default although it must be enabled when expecting a response.
```py
send_command("Commands.{CommandName}", [Parameters], await_response=True)
send_command("Commands.{CommandName}", [Parameters]) # await_response is False by default
```

## Future updates

- [ ] Update to support Connect API v2