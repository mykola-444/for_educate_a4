*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***
Start Browser and Maximize
    Open Browser  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588  Chrome
    Maximize Browser Window

Close Browser Window
    ${Title}=  Get Title
    Log  ${Title}
    Close Browser