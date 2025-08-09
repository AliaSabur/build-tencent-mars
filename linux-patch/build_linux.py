#!/usr/bin/env python3
import os
import sys
import glob

from mars_utils import *


SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]

BUILD_OUT_PATH = 'cmake_build/Linux'
INSTALL_PATH = BUILD_OUT_PATH + '/Linux.out'

LINUX_BUILD_OS_CMD = 'cmake ../.. -DCMAKE_BUILD_TYPE=Release && make -j8 && make install'


def build_linux(tag=''):
    # gen_mars_revision_file('comm', tag)

    clean(BUILD_OUT_PATH)
    os.chdir(BUILD_OUT_PATH)
    
    ret = os.system(LINUX_BUILD_OS_CMD)
    os.chdir(SCRIPT_PATH)
    if ret != 0:
        print('!!!!!!!!!!!build fail!!!!!!!!!!!!!!!')
        return False

    ssl_lib = 'openssl/openssl_lib_linux_x64/libssl.a'
    crypto_lib = 'openssl/openssl_lib_linux_x64/libcrypto.a'
    
    libtool_os_dst_lib = INSTALL_PATH + '/libmars.a'
    
    libtool_src_libs = glob.glob(INSTALL_PATH + '/*.a')
    libtool_src_libs.append(ssl_lib)
    libtool_src_libs.append(crypto_lib)
    libtool_src_libs.append(BUILD_OUT_PATH + '/zstd/libzstd.a')
    
    if not libtool_libs_linux(libtool_src_libs, libtool_os_dst_lib):
        return False

    dst_release_path = INSTALL_PATH + '/mars-release'
    make_static_linux(libtool_os_dst_lib, dst_release_path, COMM_COPY_HEADER_FILES, '../')

    print('================== Output ========================')
    print(dst_release_path)
    return True


if __name__ == '__main__':
    build_linux()
    
