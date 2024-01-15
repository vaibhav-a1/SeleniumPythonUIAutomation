This is selenium based Python automation code divided into several modules.
Each module can be run sepataely using pytest.

Command to run
pytest module_name.py

Command to generate allure reports
pytest --alluredir=./allure-results module_name.py

Command to view reports in allure
allure serve ./allure-results  
