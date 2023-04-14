import asyncio
import time

from py_qroma.qroma_comm.qcio_serial_b64 import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import hello_qroma_with_pb_response_pb2


def create_hello_qroma_message(name):
    hello_qroma_message = hello_qroma_with_pb_response_pb2.HelloQromaRequest()
    hello_qroma_message.name = name
    msg_bytes = hello_qroma_message.SerializeToString()
    return msg_bytes


async def monitor(com_port: str):
    print("STARTING QROMA MONITOR")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("MONITOR READY")
    i = 0
    while i < 10:
        if i % 2 == 0:
            msg_bytes = create_hello_qroma_message(f"Dev World: {i}")
            await qcio.send_bytes_base64_with_newline(msg_bytes)

        qhr = hello_qroma_with_pb_response_pb2.HelloQromaResponse()
        message = await qcio.read_until_base64_newline_pb_parsed(qhr, 1.5)
        
        if message:
            print("MESSAGE RECEIVED")
            print(message)
        else:
            print("TIMED OUT")

        i += 1

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(monitor(QROMA_ACTIVE_COM_PORT))