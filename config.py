import os
from dotenv import load_dotenv

class Config:
    @staticmethod
    def check_and_create_env():
        if not os.path.exists('.env'):
            with open('.env', 'w') as f:
                f.write('DEEPSEEK_API_KEY=\n')  # 创建空的API密钥

    @staticmethod
    def get_api_key():
        load_dotenv()
        return os.getenv("DEEPSEEK_API_KEY")
