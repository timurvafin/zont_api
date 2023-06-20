import requests
import time
import logging

class DeviceNotFoundError(Exception):
    pass

class ResponseError(Exception):
    pass

class ZontAPI:
    BASE_URL = 'https://lk.zont-online.ru/api'


    def __init__(self, zont_username: str, zont_password: str, dev_id: int, log_requests: bool = False):
        self.zont_username = zont_username
        self.zont_password = zont_password
        self.dev_id = dev_id
        self._device_cache = None
        self.session = requests.Session()

        self._setup_logger(log_requests)


    def _setup_logger(self, log_requests):
        self.logger = logging.getLogger("ZontAPI")

        if log_requests:
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(logging.StreamHandler())


    def _make_request(self, method, endpoint, request=None):
        url = f"{self.BASE_URL}/{endpoint}"

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-ZONT-Client': self.zont_username,            
        }

        auth = (self.zont_username, self.zont_password)

        response = self.session.request(method, url, json=request, headers=headers, auth=auth)
        response_json = response.json()

        self._log_request(method, url, headers, request, response, response_json)

        return response_json


    def _log_request(self, method, url, request_headers, request_body, response, response_json):
        self.logger.debug(f"{method} {url}")
        self.logger.debug(f"Request headers: {request_headers}")
        self.logger.debug(f"Request body: {request_body}")
        self.logger.debug(f"Response status code: {response.status_code}")
        self.logger.debug(f"Response body: {response_json}")


    def __get_device_data(self):
        if self._device_cache is not None and (time.time() - self._device_cache.get('timestamp', 0)) < 60:
            return self._device_cache['data']

        request = {"load_io": True}
        response = self._make_request('POST', 'devices', request)

        if 'ok' not in response or not response['ok']:
            raise ResponseError('Response does not contain the "ok" key')

        if 'devices' not in response:
            raise ResponseError('Response does not contain the "devices" key')

        device_list = response.get('devices', [])

        for device in device_list:
            if device['id'] == self.dev_id:
                self._device_cache = {'timestamp': time.time(), 'data': device}
                return self._device_cache['data']

        raise DeviceNotFoundError(f'Device with ID {self.dev_id} not found')

    def get_device(self):
        device_data = self.__get_device_data()
        
        return {
            "id": device_data.get("id"),
            "ip": device_data.get("ip"),
            "is_active": device_data.get("is_active"),
            "name": device_data.get("name"),
            "ot_config": device_data.get("ot_config")
        }

    def get_thermometers(self):
        device_data = self.__get_device_data()
        
        thermometers = device_data.get('thermometers', [])
        thermometer_data = {}

        for thermometer in thermometers:
            if thermometer.get('last_state') == 'ok':
                name = thermometer.get('name')
                last_value = thermometer.get('last_value')
                thermometer_data[name] = last_value

        return thermometer_data
    
    def update_device(self, data):
        request = {'device_id': self.dev_id, **data}
        response = self._make_request('POST', 'update_device', request)

        if 'ok' in response and response['ok']:
            return response
        else:
            return False    
        

    def enable_dhw(self):
        return self.update_device({"ot_config": ["ch", "dhw"]})

    def disable_dhw(self):
        return self.update_device({"ot_config": ["ch"]})
    