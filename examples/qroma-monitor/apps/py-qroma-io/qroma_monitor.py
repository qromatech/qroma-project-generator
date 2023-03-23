import asyncio
import time

from py_qroma.qroma_comm.qcio_serial import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import qroma_monitor_pb2


async def monitor_for_message(qcio: QcioSerial, give_up_time: float) -> qroma_monitor_pb2.QromaHeartbeat:
    response_bytes = b''
    while time.time() < give_up_time:
        b = await qcio.read_next_byte(0.1)
        if b is not None:
            response_bytes += b

        qhb = qroma_monitor_pb2.QromaHeartbeat()
        try:
            qhb.ParseFromString(response_bytes)
            return qhb
        except:
            pass

    return None
    

async def monitor(com_port: str):
    print("STARTING QROMA MONITOR")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("MONITOR READY")
    i = 0
    while i < 15:
        give_up_time = time.time() + 0.5
        message = await monitor_for_message(qcio=qcio, give_up_time=give_up_time)
        
        if message:
            print(message)
        else:
            print("TIMED OUT")

        i += 1

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(monitor(QROMA_ACTIVE_COM_PORT))