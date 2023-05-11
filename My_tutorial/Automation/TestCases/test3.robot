*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${Browser}  Chrome
${URL}  http://www.facebook.com
#${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=login&Itemid=587

*** Test Cases ***
Robot First Test Case
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Select Radio Button  sex  -1
    Input text  id:email  hello
    Input text  id:pass  Asdc
    Click Button  xpath://input[@type='submit']
    #Select Checkbox  remember
    #Click Link  xpath://a[text()='Забыли аккаунт?']
    #Click Link  xpath://a[text()='Quick Demo']
    #Close Browser
