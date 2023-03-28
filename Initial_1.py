import pytest
import os

#生成test report
if __name__ == "__main__":
    # result_dir = "../report/Json"
    # pytest.main(['-v', '-s', 'scripts/smart_connect_1.py', '--alluredir=./report/Json', '--clean-alluredir'])

    pytest.main(['-v', '-s', 'scripts/login_logout.py', '--alluredir=./report/Json', '--clean-alluredir'])
    # pytest.main(['-x', 'scripts/login_logout.py', '--alluredir=./report/Json', '--clean-alluredir'])
    # pytest.main(['-s', 'scripts/login_logout.py', '--alluredir=./report/Json', '--clean-alluredir'])
os.system('allure generate ./report/Json -o ./report/html --clean')