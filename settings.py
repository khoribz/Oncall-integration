import os

ONCALL_BASE_URL = os.getenv('ONCALL_BASE_URL', 'http://127.0.0.1:8080/')
ONCALL_API_VERSION = 'v0'
ONCALL_USERNAME = os.getenv('ONCALL_USERNAME', 'root')
ONCALL_PASSWORD = os.getenv('ONCALL_PASSWORD', '123')