DEFAULT_QROMA_USER_PROFILE_TOML = """
[qroma.user.profile.defaults.tools]
editor_command = "code"
docker_command = "docker"
firmware_platform = "user_managed"


[qroma.user.profile.defaults.preferences]
firmware_platforms = [
    "user_managed",
]


[qroma.user.profile.dirs]
# platform_io_package_root = "C:/Users/ajb/.platformio/packages"


[qroma.user.profile.commands.firmware.user_managed]
build_command = "pio run"
upload_command = "pio run --target upload --environment esp32dev"


# [qroma.user.profile.commands.firmware.platformio]
# platformio_exe = "pio"
# build_command = "run"
# upload_command = "run --target upload --environment esp32dev"

"""
