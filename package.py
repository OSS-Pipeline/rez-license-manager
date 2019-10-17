name = "license_manager"

version = "0.0.1"

authors = [
    "Joshua Senouf"
]

description = \
    """
    Simple Rez project, mostly meant to setup the necessary license information for other Rez packages to pick up.
    """

requires = [
    "cmake-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "license_manager-{version}".format(version=str(version))

def commands():
    # We setup the license related environment variables.
    env.AUTODESK_LICENSE_SERVER.set("")
    env.MAYA_SERIAL_NUMBER.set("")
    env.FOUNDRY_LICENSE_SERVER.set("")
    env.HOUDINI_LICENSE_SERVER.set("")
    env.SUBSTANCE_LICENSE_SERVER.set("")
    env.EQUALIZER_LICENSE_SERVER.set("")
    env.RENDERMAN_LICENSE_SERVER.set("")
    env.DELIGHT_LICENSE_SERVER.set("")
