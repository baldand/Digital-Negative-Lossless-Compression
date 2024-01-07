from distutils.core import setup, Extension

module1 = Extension(
    'lj92', 
    sources = ["lj92.c","Digital-Negative-Lossless-Compression.c"],  
    xtra_compile_args=['-msse2','-std=gnu99'], 
    extra_link_args=[])

setup ( name = "lj92", version = "1.0", description = "Lossless JPEG 92 (de)compression", ext_modules = [module1])

