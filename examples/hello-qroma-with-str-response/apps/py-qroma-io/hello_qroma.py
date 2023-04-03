import sys
import asyncio
from py_qroma.qroma_comm.qcio_serial_b64 import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import hello_qroma_with_str_response_pb2


def create_hello_qroma_message(name):
    hello_qroma_message = hello_qroma_with_str_response_pb2.HelloQroma()
    hello_qroma_message.name = name
    msg_bytes = hello_qroma_message.SerializeToString()
    return msg_bytes


async def monitor(com_port: str, message: str):
    print("STARTING QROMA MONITOR")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("MONITOR READY")
    i = 0
    while i < 10:
        if i % 2 == 0:
            msg_bytes = create_hello_qroma_message(f"{message} ({i})")
            await qcio.send_bytes_base64_with_newline(msg_bytes)

        data = await qcio.read_bytes_until_timeout(1.0)
        print(f"LINE RECEIVED: {data}")
        i = i + 1

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    message = "Qroma!"
    if len(sys.argv) > 1:
        message = sys.argv[1]
    asyncio.run(monitor(QROMA_ACTIVE_COM_PORT, message))