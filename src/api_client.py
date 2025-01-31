import requests

class APIClient:
    def __init__(self, base_url, auth_token=None):
        self.base_url = base_url
        self.auth_token = auth_token

    def _get_headers(self, headers):
        """Merge custom headers with authentication headers"""
        default_headers = {"Content-Type": "application/json"}
        if self.auth_token:
            default_headers["Authorization"] = f"Bearer {self.auth_token}"
        if headers:
            default_headers.update(headers)
        return default_headers

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params, headers=self._get_headers(headers))
            return response
        except requests.RequestException as e:
            return {"error": str(e)}

    def post(self, endpoint, data, headers=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=data, headers=self._get_headers(headers))
            return response
        except requests.RequestException as e:
            return {"error": str(e)}

    def put(self, endpoint, data, headers=None):
        """Send a PUT request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.put(url, json=data, headers=self._get_headers(headers))
            return response
        except requests.RequestException as e:
            return {"error": str(e)}

    def patch(self, endpoint, data, headers=None):
        """Send a PATCH request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.patch(url, json=data, headers=self._get_headers(headers))
            return response
        except requests.RequestException as e:
            return {"error": str(e)}

    def delete(self, endpoint, headers=None):
        """Send a DELETE request"""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.delete(url, headers=self._get_headers(headers))
            return response
        except requests.RequestException as e:
            return {"error": str(e)}