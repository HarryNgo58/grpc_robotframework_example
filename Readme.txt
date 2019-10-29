HOW TO USE
1. Clone the server source code and start the sever
    https://github.com/DongND/grpc-restful-code-base
2. Install the required package in requirement.txt
    pip3 install -r requirement.txt
3. Run the test case in robot_test folder same as normal


HOW TO MAKE IT?
1. Get the proto file. Ex:customer.proto
2. Generating the Stubs using the following command
    python3 -m grpc_tools.protoc --proto_path=. ./your_proto_file.proto --python_out=. --grpc_python_out=.
3. Write your client code. See the example in pythonlibs/customer_client.py
4. Write the robot test using the function written in step 3



