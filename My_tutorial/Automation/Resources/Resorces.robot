*** Settings ***
Documentation    Suite description
Library  SeleniumLibrary


*** Variables ***
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588
${Browser}  Chrome


*** Keywords ***
Start Browser
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window