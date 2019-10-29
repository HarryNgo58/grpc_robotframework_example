*** Settings ***
Library        ../pythonlibs/customer_client.py

*** Variables ***
${customer_id}            ${100}
${customer_name}          Harry

*** Test Cases ***
GRPC_Client_testing
    ${response}=    Client Create Customer      ${customer_id}                  ${customer_name}
    should be equal as integers                 ${customer_id}                  ${response}[id]
    should be equal as strings                  ${customer_name} created        ${response}[name]