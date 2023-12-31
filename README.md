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

# Get heating modes
heating_modes = api.get_heating_modes()
print(heating_modes)

# Update device settings
api.update_device({"ot_config": ["ch", "dhw"]})

# Enable or disable DHW
api.enable_dhw()
api.disable_dhw()
```

Replace 'your_zont_username' and 'your_zont_password' with your actual Zont Online credentials. Also, provide the device ID (dev_id) for the specific device you want to interact with.

## Logging Requests and Responses

By default, the library does not log the requests and responses. However, you can enable logging for debugging purposes by passing log_requests=True when creating an instance of the ZontAPI class:

```python
api = ZontAPI(zont_username='your_zont_username', zont_password='your_zont_password', dev_id=12345, log_requests=True)
```

This will enable logging of the HTTP requests and responses to the console.

## Error Handling

The ZontAPI library raises two custom exceptions: `DeviceNotFoundError` and `ResponseError`.

DeviceNotFoundError is raised when a device with the specified ID is not found.
ResponseError is raised when the API response does not contain the expected keys or values.
Make sure to handle these exceptions appropriately in your code.

## Development

### console.py

`console.py` is a Python script for interacting with the ZontAPI. It requires three command-line arguments: ZontAPI username, password, and device ID.


```
python console.py <username> <password> <dev_id>
```

The script performs the following operations:
1. Fetches and displays thermometer data.
2. Enables and disables Domestic Hot Water (DHW), providing success or failure feedback.

## Running Tests

Upgrade pip and install packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run tests in the `tests/` directory:

```bash
python -m pytest tests/
```

Ensure you're in the correct directory when running these commands.

## License

This library is licensed under the MIT License. See the LICENSE file for more information.
