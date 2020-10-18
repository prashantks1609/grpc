# test_grpc.py

import project

def test_reply(grpc_stub):
    value = 'test-data'
    request = project.echo_pb2.EchoRequest(message=value)
    response = grpc_stub.Reply(request)

    assert response.message == f'You said: {value}'