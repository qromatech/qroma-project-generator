# import tomllib
# import tomli_w
#
# from qp_config import QromaProjectConfig
# from qroma_enums import DeviceBoardPlatform
#
#
# with open('../qroma-project-template/qroma-test.toml', 'rb') as f:
#     config = tomllib.load(f)
#     print(config)
#
# qpc = QromaProjectConfig(dev_board_platforms=[DeviceBoardPlatform.arduino, DeviceBoardPlatform.platformio])
#
# print(tomli_w.dumps(qpc))
