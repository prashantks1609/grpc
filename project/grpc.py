from project.generated import echo_pb2_grpc as echo_pb2_grpc
from project.generated import echo_pb2 as echo_pb2


class Echoer(echo_pb2_grpc.EchoServicer):

    def Reply(self, request, context):
        return echo_pb2.EchoReply(message=f'You said: {request.message}')