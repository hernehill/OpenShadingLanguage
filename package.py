name = "osl"

version = "1.15.7.0.hh.1.0.0"

authors = [
    "AcademySoftwareFoundation",
]

description = """Programmable shading language"""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "pugixml-1.14",
    "boost-1.88",
    "openexr-3.4",
    "ocio-2.5.2",
    "oiio-3.0.9",
]

private_build_requires = []

variants = [
    ["python-3.13"],
]


def commands():
    env.REZ_OSL_ROOT = "{root}"
    env.OSL_ROOT = "{root}"
    env.OSL_LOCATION = "{root}"
    env.OSL_INCLUDE_DIR = "{root}/include"
    env.OSL_LIBRARY_DIR = "{root}/lib64"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.PKG_CONFIG_PATH.append("{root}/lib64/cmake/OSL")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib64/python3.11/site-packages")
            elif python_ver.minor == 13:
                env.PYTHONPATH.append("{root}/lib64/python3.13/site-packages")


build_system = "cmake"
uuid = "repository.OpenShadingLanguage"
