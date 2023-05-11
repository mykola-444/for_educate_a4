*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${Browser}  Chrome
${URL}  https://www.thetestingworld.com/index.php?option=com_users&view=registration&Itemid=588

*** Test Cases ***
Robot First Test Case
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Enter Username Password Email  Testing  gfh@gd.com  1234
    Enter Username Password Email1

*** Keywords ***
Enter Username Password Email1
    Input text  name:jform[username]  hello
    Input text  name:jform[password1]  123456
    Input text  jform[email1]  Asdc@uyddbgst.com

Enter Username Password Email
    [Arguments]  ${username}  ${email}  ${password}
    Input text  name:jform[username]  ${username}
    Input text  name:jform[password1]  ${password}
    Input text  jform[email1]  ${email}
