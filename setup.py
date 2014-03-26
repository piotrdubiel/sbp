from distutils.core import setup, Extension

# the c++ extension module
extension_mod = Extension("sbp",
                          ["bindings/sbp.cpp",
                           "bindings/utils.cpp",
                           "src/SBPNetwork.cpp",
                           "src/SBPLayer.cpp",
                           "src/SBPNeuron.cpp"],
                          include_dirs=["include"])

setup(name="pysbp",
      version='0.0.2',
      ext_modules=[extension_mod],
      packages=['pysbp'],
      install_requires=["PyYAML >= 3.10"])
