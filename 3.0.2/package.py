name = "openexr"

version = "3.0.2"

build_requires = [
    "cmake",
    #"gcctoolset-9",
]

requires = [
   "imath-3",
   "png",
   "zlib"
]

variants = [['platform-linux', 'arch-x86_64']]

build_command = "make -f {root}/Makefile {install}"

tools = [
    "IexTest",
    "OpenEXRExamples",
    "OpenEXRTest",
    "OpenEXRUtilTest",
    "exr2aces",
    "exrcheck",
    "exrenvmap",
    "exrheader",
    "exrmakepreview",
    "exrmaketiled",
    "exrmultipart",
    "exrmultiview",
    "exrstdattr"
]

def commands():
    env.REZ_BUILD_PROJECT_VERSION=version
    env.REZ_BUILD_INSTALL_PATH="/homw/minwoo/packages/openexr"

    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    if building:
        env.OpenEXR_ROOT="{root}" # CMake Hint
