# ZontAPI Python Library

The ZontAPI Python library provides a convenient way to interact with the Zont Online API. It allows you to retrieve device information, get thermometer data, and update device settings.

## Installation

You can install the ZontAPI library using `pip`:

```bash
pip install zont-api
```

## Usage

Here's a basic example of how to use the ZontAPI library:

```python
from zont_api import ZontAPI

# Create an instance of the ZontAPI class
api = ZontAPI(zont_username='your_zont_username', zont_password='your_zont_password', dev_id=12345)

# Retrieve device information
device_info = api.get_device()
print(device_info)

# Get thermometer data
thermometers = api.get_thermometers()
print(thermometers)

# Update device settings
api.update_device({"ot_config": ["ch", "dhw"]})
```

Replace 'your_zont_username' and 'your_zont_password' with your actual Zont Online credentials. Also, provide the device ID (dev_id) for the specific device you want to interact with.

## Logging Requests and Responses

By default, the library does not log the requests and responses. However, you can enable logging for debugging purposes by passing log_requests=True when creating an instance of the ZontAPI class:

```python
api = ZontAPI(zont_username='your_zont_username', zont_password='your_zont_password', dev_id=12345, log_requests=True)
```

This will enable logging of the HTTP requests and responses to the console.

## Error Handling

The ZontAPI library raises two custom exceptions: DeviceNotFoundError and ResponseError.

DeviceNotFoundError is raised when a device with the specified ID is not found.
ResponseError is raised when the API response does not contain the expected keys or values.
Make sure to handle these exceptions appropriately in your code.

## License

This library is licensed under the MIT License. See the LICENSE file for more information.