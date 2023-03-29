DEFAULT_QROMA_USER_PROFILE_TOML = """
[qroma.user.profile.defaults.tools]
editor_command = "code"
docker_command = "docker"
firmware_platform = "platformio"


[qroma.user.profile.defaults.preferences]
firmware_platforms = [
    "arduino",
    "platformio",
]


[qroma.user.profile.commands.firmware.platformio]
platformio_exe = "pio"
build_command = "run"
upload_command = "run --target upload --environment esp32dev"
monitor_command = "TBD"


[qroma.user.profile.commands.firmware.arduino]
arduino_exe = "TBD"
build_command = "TBD"
upload_command = "TBD"
monitor_command = "TBD"

"""
