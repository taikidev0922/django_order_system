import json
from django.utils.deprecation import MiddlewareMixin

class LogRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            body = request.body.decode('utf-8')
            # JSON形式のデータをPythonオブジェクトに変換
            body = json.loads(body) if body else 'No Body'
        except json.JSONDecodeError:
            body = 'Could not decode JSON'

        # リクエストの詳細をログに記録
        print(f"Request Path: {request.path}")
        print(f"Request Method: {request.method}")
        print(f"Request Body: {body}")
        print(f"Request Headers: {dict(request.headers)}")

        return None