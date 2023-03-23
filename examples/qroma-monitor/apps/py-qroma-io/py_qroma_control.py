import asyncio
from py_qroma.qroma_comm.qcio_serial import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT


async def control(com_port: str):
    print("STARTING QROMA CONTROL")

    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("MONITOR READY")
    i = 0
    while i < 5:
        if i % 2 == 0:
            qcio.send_bytes()
        data = await qcio.read_bytes_until_timeout(1.0)
        print(f"LINE RECEIVED: {data}")
        i = i + 1

    print("STOPPING MONITOR")
    qcio.stop()

    print("DONE")


if __name__ == "__main__":
    asyncio.run(control(QROMA_ACTIVE_COM_PORT))