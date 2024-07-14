from setuptools import setup, find_packages

setup(
    name='mawaqit_api',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/Ahmad-Said/mawaqit-api',
    install_requires=[
        'uvicorn==0.19.0',
        'requests==2.28.1',
        'fastapi==0.85.1',
        'httpx==0.23.0',
        'pytest==7.2.0',
        'bs4==0.0.1',
        'redis==5.0.1',
        'python-dotenv==1.0.1',
    ],
)
