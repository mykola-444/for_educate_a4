*** Settings ***
Library  SeleniumLibrary
Library  ../ExternalKeywords/UserKeywords.py

*** Variables ***


*** Keywords ***
Start Browser and Maximize
    Open Browser  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588  Chrome
    Maximize Browser Window

Close Browser Window
    ${Title}=  Get Title
    Log  ${Title}
    Close Browser

#Create Folder at Runtime
#    create_folder
#    create_sub_folder
#    Log  Tack complite sussec

Create Folder at Runtime
    [Arguments]  ${foldername}  ${subfoldername}
    create_folder  ${foldername}
    create_sub_folder  ${subfoldername}
    Log  Tack complite sussec

Concatenate Username and Password
    [Arguments]  ${Username}  ${Password}
    ${resultval}=  concatenate_two_values  ${Username}  ${Password}
    Log  ${resultval}