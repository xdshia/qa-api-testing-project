class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data

    def json(self):
        return self._json


def post(endpoint, payload):
    if endpoint == "/api/login":
        # SUCCESS CASE
        if payload.get("email") and payload.get("password"):
            return MockResponse(
                200,
                {"token": "fake-jwt-token"}
            )

        # FAILURE CASE
        return MockResponse(
            400,
            {"error": "Missing password"}
        )

    return MockResponse(404, {})
