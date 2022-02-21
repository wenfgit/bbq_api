import os
import pytest


pytest.main(['-s', r"--alluredir=report/data", "--clean-alluredir"])
os.system('allure generate ./report/data -o ./report/html -c')
