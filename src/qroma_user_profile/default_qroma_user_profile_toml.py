DEFAULT_QROMA_USER_PROFILE_TOML = """
[qroma.user.profile.defaults]
new_project_firmware_platform = "platformio"


[qroma.user.profile.defaults.tools]
editor_command = "code"
docker_command = "docker"
firmware_platforms = [
    "user_managed",
    "platformio",
]


[qroma.user.profile.dirs]
# platform_io_packages_root = "C:/Users/ajb/.platformio/packages"
# platform_io_packages_root = "/Users/ajb/.platformio/packages"

[qroma.user.profile.tools.firmware_platforms.user_managed]
build_prompt = "Build firmware. Hit enter when done. >>> "
upload_prompt = "Upload firmware onto device. Hit enter when done/ >>> "


[qroma.user.profile.tools.firmware_platforms.platformio]
build_command = "pio run"
upload_command = "pio run --target upload --environment esp32dev"


[qroma.user.profile.tools.firmware_platforms.arduino]
build_prompt = "Open Arduino IDE. Build firmware. Hit enter when done. >>> "
upload_prompt = "Open Arduino IDE. Upload firmware onto device. Hit enter when done/ >>> "


# [qroma.user.profile.commands.firmware.platformio]
# platformio_exe = "pio"
# build_command = "run"
# upload_command = "run --target upload --environment esp32dev"

"""
