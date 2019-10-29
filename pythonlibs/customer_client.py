import grpc
import customer_pb2
import customer_pb2_grpc

class CustomerClient(object):
    """
    Client for accessing the gRPC functionality
    """

    def __init__(self):
        # configure the host and theCustomer
        # the port to which the client should connect
        # to.
        self.host = 'localhost'
        self.server_port = 9000

        # instantiate a communication channel
        self.channel = grpc.insecure_channel(
                        '{}:{}'.format(self.host, self.server_port))

        # bind the client to the server channel
        self.stub = customer_pb2_grpc.CustomerServiceStub(self.channel)

    def create_customer(self, customer_id, customer_name):
        """
        Client function to call the rpc for creating customer
        """
        customer_info = customer_pb2.Customer()
        customer_info.id = customer_id
        customer_info.name = customer_name
        client_request =customer_pb2.CreateCustomerRequest(request=customer_info)
        return self.stub.CreateCustomer(client_request)


def client_create_customer(customer_id, customer_name):
    curr_client = CustomerClient()
    a = curr_client.create_customer(customer_id, customer_name)
    out = {}
    out["id"] = a.response.id
    out["name"] = a.response.name
    return out

