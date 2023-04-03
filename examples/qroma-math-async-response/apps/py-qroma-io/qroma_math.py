import asyncio
from py_qroma.qroma_comm.qcio_serial import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import qroma_math_async_response_pb2


def create_add_problem_message(a: int, b: int):
    problem = qroma_math_async_response_pb2.MathProblem()
    problem.op = qroma_math_async_response_pb2.MathOp_Add
    problem.a = a
    problem.b = b
    msg_bytes = problem.SerializeToString()
    return msg_bytes


def create_subtract_problem_message(a: int, b: int):
    problem = qroma_math_async_response_pb2.MathProblem()
    problem.op = qroma_math_async_response_pb2.MathOp_Subtract
    problem.a = a
    problem.b = b
    msg_bytes = problem.SerializeToString()
    return msg_bytes


def create_add_and_subtract_problem_message(a: int, b: int):
    problem = qroma_math_async_response_pb2.MathProblem()
    problem.op = qroma_math_async_response_pb2.MathOp_Add_And_Subtract
    problem.a = a
    problem.b = b
    msg_bytes = problem.SerializeToString()
    return msg_bytes
    

async def do_math_queries(com_port: str):
    print("STARTING QROMA MATH")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    add_message_bytes = create_add_problem_message(3, 5)
    subtract_message_bytes = create_subtract_problem_message(11, 7)
    add_and_subtract_message_bytes = create_add_and_subtract_problem_message(9, 8)

    await qcio.read_n_bytes(2000, 5.0)

    for message_bytes in [add_message_bytes, subtract_message_bytes, add_and_subtract_message_bytes]:
        # await asyncio.sleep(3.5)

        request = qroma_math_async_response_pb2.MathProblem()
        request.ParseFromString(message_bytes)
        print(message_bytes)
        print(f">> {request}")
        # print(request_obj.a)

        response_message = qroma_math_async_response_pb2.MathProblemResponse()

        await qcio.send_bytes_base64_with_newline(message_bytes)
        response = await qcio.read_until_base64_newline_pb_parsed(response_message, 5.0)
        if response is None:
            print("RESPONSE TIMED OUT")
        else:
            print(response)

        # await asyncio.sleep(2.0)

    await qcio.read_n_bytes(200, 5.0)

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(do_math_queries(QROMA_ACTIVE_COM_PORT))


    # b = b'\x08\x03\x10\x05\x18\x01'
    # b = b[0:2]
    # print(f"B {b}")
    # request = qroma_math_async_response_pb2.MathProblem()
    # request.ParseFromString(b)
    # print(request)
