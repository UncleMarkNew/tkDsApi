from openai import OpenAI
import os

class APIClient:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://api.deepseek.com/v1",
            api_key=api_key
        )

    def send_message(self, message):
        # 发送消息的逻辑
        pass
