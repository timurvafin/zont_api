import pytest
import requests_mock
import json
from zont_api import ZontAPI


@pytest.fixture
def api():
    return ZontAPI('test@example.com', 'my_auth_token', 62953, True)


@pytest.fixture
def devices_response_json():
    with open('tests/devices.json') as f:
        return json.load(f)
    

@pytest.fixture
def update_device_response_json():
    with open('tests/update_device.json') as f:
        return json.load(f)


def test_response_without_ok(api, requests_mock, devices_response_json):
    del devices_response_json['ok'] 
    requests_mock.post('https://lk.zont-online.ru/api/devices', json=devices_response_json)
    
    with pytest.raises(Exception) as exc_info:
        api.get_device()
    
    assert str(exc_info.value) == 'Response does not contain the "ok" key'


def test_response_without_devices(api, requests_mock, devices_response_json):
    del devices_response_json['devices'] 
    requests_mock.post('https://lk.zont-online.ru/api/devices', json=devices_response_json)
    
    with pytest.raises(Exception) as exc_info:
        api.get_device()
    
    assert str(exc_info.value) == 'Response does not contain the "devices" key'


def test_get_device_not_found(api, requests_mock, devices_response_json):
    devices_response_json['devices'][0]['id'] = 123456
    requests_mock.post('https://lk.zont-online.ru/api/devices', json=devices_response_json)
    
    with pytest.raises(Exception) as exc_info:
        api.get_device()
    
    assert str(exc_info.value) == 'Device with ID 62953 not found'


def test_get_device(api, requests_mock, devices_response_json):
    requests_mock.post('https://lk.zont-online.ru/api/devices', json=devices_response_json)

    expected_device = {
        "id": 62953,
        "ip": "192.168.1.1",
        "is_active": True,
        "name": "Орёл.Котел",
        "ot_config": [ "ch" ]
    }

    result = api.get_device()

    assert result == expected_device


def test_get_thermometers(api, requests_mock, devices_response_json):
    requests_mock.post('https://lk.zont-online.ru/api/devices', json=devices_response_json)

    expected_thermometers = {
        "Улица": 16.5,
        "Котельная": 34.0,
        "Коллектор подача": 27.7,
        "Спальня": 24.8
    }

    result = api.get_thermometers()

    assert result == expected_thermometers

def test_update_device(api, requests_mock, update_device_response_json):
    requests_mock.post('https://lk.zont-online.ru/api/update_device', json=update_device_response_json)

    result = api.update_device({
        "ot_config": [
            "ch",
            "dhw"
        ]
    })
    
    assert result == update_device_response_json


def test_enable_dhw(api, requests_mock, update_device_response_json):
    requests_mock.post('https://lk.zont-online.ru/api/update_device', json=update_device_response_json)

    result = api.enable_dhw()
    
    assert result == update_device_response_json


def test_disable_dhw(api, requests_mock, update_device_response_json):
    requests_mock.post('https://lk.zont-online.ru/api/update_device', json=update_device_response_json)

    result = api.disable_dhw()
    
    assert result == update_device_response_json