import asyncio
import time

from py_qroma.qroma_comm.qcio_serial import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import hello_qroma_with_pb_response_pb2


def create_hello_qroma_message(name):
    hello_qroma_message = hello_qroma_with_pb_response_pb2.HelloQroma()
    hello_qroma_message.name = name
    msg_bytes = hello_qroma_message.SerializeToString()
    print("CREATED")
    print(hello_qroma_message)
    print(msg_bytes)
    return msg_bytes


def test_parse(msg_bytes):
    hello_qroma_message = hello_qroma_with_pb_response_pb2.HelloQroma()
    hello_qroma_message.ParseFromString(msg_bytes)
    print("TEST PARSE")
    print(hello_qroma_message)


async def monitor_for_message(qcio: QcioSerial, give_up_time: float) -> hello_qroma_with_pb_response_pb2.HelloQromaResponse:
    response_bytes = b''
    while time.time() < give_up_time:
        # b = await qcio.read_next_byte(0.1)
        b = await qcio.read_n_bytes(100, 0.3)
        if b is not None:
            response_bytes += b

        qhb = hello_qroma_with_pb_response_pb2.HelloQromaResponse()
        try:
            qhb.ParseFromString(response_bytes)
            return qhb
        except:
            print(f"PARSE FAILURE: {response_bytes}")
            pass

    return None


async def monitor(com_port: str):
    print("STARTING QROMA MONITOR")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("MONITOR READY")
    i = 0
    while i < 10:
        if i % 2 == 0:
            # msg_bytes = create_hello_qroma_message(f"Dev World: {i}\x00")
            msg_bytes = create_hello_qroma_message(f"Dev World: {i}")
            test_parse(msg_bytes)
            print(f"SENDING {msg_bytes} [{len(msg_bytes)}]")
            await qcio.send_bytes(msg_bytes)

        # data = await qcio.read_bytes_until_timeout(1.0)
        # print(f"LINE RECEIVED: {data}")
        # i = i + 1

        give_up_time = time.time() + 0.5
        message = await monitor_for_message(qcio=qcio, give_up_time=give_up_time)
        
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