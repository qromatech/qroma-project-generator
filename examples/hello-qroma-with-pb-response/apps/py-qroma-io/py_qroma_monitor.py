import asyncio
from py_qroma.qroma_comm.qcio_serial import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import hello_qroma_pb2


def create_hello_qroma_message(name):
    hello_qroma_message = hello_qroma_pb2.HelloQroma()
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
    while i < 5:
        if i % 2 == 0:
            msg_bytes = create_hello_qroma_message(f"Dev World: {i}")
            await qcio.send_bytes(msg_bytes)

        data = await qcio.read_bytes_until_timeout(1.0)
        print(f"LINE RECEIVED: {data}")
        i = i + 1

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(monitor(QROMA_ACTIVE_COM_PORT))