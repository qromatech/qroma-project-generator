import asyncio
import time

from py_qroma.qroma_comm.qcio_serial_b64 import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from qroma_proto import qroma_monitor_pb2



def on_message_callback(message):
    now = time.time()
    print(f"{now}: {message}")
    

async def monitor(com_port: str):
    print("STARTING QROMA MONITOR")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("MONITOR READY")

    await qcio.monitor_for_pb_message(qroma_monitor_pb2.QromaHeartbeat(), on_message_callback, 3.0)

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(monitor(QROMA_ACTIVE_COM_PORT))
    