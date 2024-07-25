name = "osl"

version = "1.13.7.0.hh.1.0.0"

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
    "ocio-2.1",  # being explicit here in case we have oiio 2.5.9 against ocio-2.3.2
    "oiio-2.5.9",
]

private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
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
            if python_ver.minor == 7:
                env.PYTHONPATH.append("{root}/lib64/python3.7/site-packages")
            elif python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib64/python3.9/site-packages")
            elif python_ver.minor == 10:
                env.PYTHONPATH.append("{root}/lib64/python3.10/site-packages")
            elif python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib64/python3.11/site-packages")
            elif python_ver.minor == 12:
                env.PYTHONPATH.append("{root}/lib64/python3.12/site-packages")


build_system = "cmake"
uuid = "repository.OpenShadingLanguage"
