*** Settings ***
Library    RequestsLibrary


*** Variables ***
${base_url}  http://192.168.36.107:18081/api/dolphicam/
${command}  hello
${command_TrmStatus}    Trmstatus
${command_startscan}    startscan
${command_stopscan}    stopscan
${command_loadfile}    loadPuT Request | Rest API Testing using Robot Frameworkfile/C:/Users/Public/Documents/DolphiCam2/Profiles/FMCManual_FIR_1.0.DolphiCam
${command_setTrmMode}   setTrmMOde/2
*** Test Cases ***
#name of testcase
Get_Trmstatus
	Create Session    mysession  ${base_url}
	${reposnse}=  GET On Session   mysession  ${command_TrmStatus}
    #outputs contents to terminal
    Log To Console    ${reposnse.content}

    #validation of content
    ${body}=  Convert To String    ${reposnse.content}
    Should Contain  ${body}     BB190123



Get_dolphicam
    ${reposnse1}=  GET On Session   mysession  ${command}
    #outputs contents to terminal
    Log To Console    ${reposnse1.content}

    #validation of content
    ${body}=  Convert To String    ${reposnse1.content}
    Should Contain  ${body}     Dolphicam

#Put_loadfile
 #  ${reponse2}=    PUT On Session  mysession    ${command_loadfile}


Put_startscan
   ${reponse2}=    PUT On Session  mysession    ${command_startscan}


Put_stopscan
   ${reponse2}=    PUT On Session  mysession    ${command_stopscan}


#Put_SetTrmMode
   #${reponse2}=    PUT On Session  mysession    ${command_stopscan}