name = "osl"

version = "1.14.7.0.hh.1.0.1"

authors = [
    "AcademySoftwareFoundation",
]

description = """Programmable shading language"""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "pugixml-1.14",
    "boost-1.82",
    "openexr-3.1",
    "oiio-2.5.16",
]

private_build_requires = [
    "visual_studio",
]

variants = [
    ["python-3.9", "ocio-2.1"],
    ["python-3.9", "ocio-2.2"],
    ["python-3.10", "ocio-2.1"],
    ["python-3.10", "ocio-2.2"],
    ["python-3.11", "ocio-2.1"],
    ["python-3.11", "ocio-2.2"],
]


def commands():
    env.REZ_OSL_ROOT = "{root}"
    env.OSL_ROOT = "{root}"
    env.OSL_LOCATION = "{root}"
    env.OSL_INCLUDE_DIR = "{root}/include"
    env.OSL_LIBRARY_DIR = "{root}/lib"

    env.PATH.append("{root}/bin")
    env.PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/cmake/OSL")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib/python3.9/site-packages")
            elif python_ver.minor == 10:
                env.PYTHONPATH.append("{root}/lib/python3.10/site-packages")
            elif python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib/python3.11/site-packages")


build_system = "cmake"
uuid = "repository.OpenShadingLanguage"
