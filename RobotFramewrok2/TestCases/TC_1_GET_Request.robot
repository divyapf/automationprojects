*** Settings ***
Library    RequestsLibrary


*** Variables ***
${base_url}  http://192.168.36.107:18081/api/dolphicam/hello
${command}  hello

*** Test Cases ***
#name of testcase
Get_dolphicam
	Create Session    mysession  ${base_url}
	${reposnse}=  GET On Session   mysession  ${command}
    Log To Console    ${reposnse.status_code}
    Log To Console    ${reposnse.content}
    Log To Console    ${reposnse.headers}

    #validating that the above from the respnse

    ${status_code}=  Convert To String    ${reposnse.status_code}
    Should Be Equal     ${status_code}  200

    #verify the content in the response

    ${body}=  Convert To String    ${reposnse.content}
    Should Contain  ${body}     Dolphicam

    #below example of a failed testcase
    #${body}=  Convert To String    ${reposnse.content}
    #Should Contain  ${body}     Dolphicam says hi

    