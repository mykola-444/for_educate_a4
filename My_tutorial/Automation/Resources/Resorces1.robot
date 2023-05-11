*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***
Start Browser and Maximize
    [Arguments]  ${UserURL}  ${InpurBrowser}
    Open Browser  ${UserURL}  ${InpurBrowser}
    Maximize Browser Window
    ${Title}=  Get Title
    [Return]  ${Title}

