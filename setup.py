from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("pysbp",
                          ["python/pysbp.cpp",
                           "python/utils.cpp",
                           "src/SBPNetwork.cpp",
                           "src/SBPLayer.cpp",
                           "src/SBPNeuron.cpp"],
                          include_dirs=["include"])

setup(name="pysbp", version='0.0.1', ext_modules=[extension_mod])
