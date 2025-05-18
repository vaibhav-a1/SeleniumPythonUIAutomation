*** Settings ***
Library         SeleniumLibrary
Library         OperatingSystem
Library         ../userdefinedlib/userlib.py
Resource        ./env_config.robot
Resource        ../resources/common/common_keywords.robot
Resource        ../resources/pageobjects/01_Actions_PO.robot
Resource        ../resources/pages/01_Actions_Page.robot
Resource        ../resources/pages/09_Execution_Calender_Page.robot
Resource        ../resources/pageobjects/09_Execution_Calender_PO.robot

Variables       ../TestData/data.py