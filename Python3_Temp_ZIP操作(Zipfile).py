#! /usr/bin/env python3

# Create By GF 2023-07-08 00:18

# Python3_Temp_ZIP操作(Zipfile).py

# ----------------------------------------------------------------------------------------------------

import zipfile

# ----------------------------------------------------------------------------------------------------
# 使用 zipfile.ZipFile() 时，参数为文件的路径与文件名组成的字符串。

# CompressFile = zipfile.ZipFile(r'D:\test.zip')

# ----------------------------------------------------------------------------------------------------
# 调用 .namelist 方法可以得到压缩包里面的所有文件名。

# ListCompressFile = CompressFile.namelist()

# ----------------------------------------------------------------------------------------------------
# 调用 .extract 方法并配合 for 循环解压文件到指定目录。

# for FileName in ListCompressFile:
#     CompressFile.extract(FileName, r'D:\Dist', pwd="123456".encode("utf-8"))

# ----------------------------------------------------------------------------------------------------
# 当使用 zipfile 解压非加密 ZIP 压缩包时，只需修改：
# CompressFile.extract(FileName, r"D:\Dist", pwd="123".encode("utf-8"))
# 为：
# CompressFile.extract(FileName, r"D:\Dist")

# ----------------------------------------------------------------------------------------------------
# 不再使用ZIP压缩文件时，关闭文件，释放内存（必须）。
# CompressFile.close()

# ----------------------------------------------------------------------------------------------------
# Notice

# 调用 zipfile 对传统加密的 ZIP 文件进行解压可以成功（传统加密 : CRC32 也即 ZIP 2.0）。
# 但是当 ZIP 为非传统加密方式时无法解压（非传统加密 : AES-256）。
# 这里的传统加密指的什么呢？
# 使用版本比较新的 WinRAR 进行 ZIP 加密压缩的时候，下面会有一个“ZIP传统加密”的选项。
# 自带的 zipfile 模块只支持 CRC32 加密的 ZIP 文件，pyzipper 三方库可以读写 AES 加密的 ZIP 文件。

# ----------------------------------------------------------------------------------------------------

def FuncOpenZip():

    CompressFile = zipfile.ZipFile("D:\\ExampleZip.zip", 'r')
    
    # --------------------------------------------------
    CompressFile.close()
    
    # --------------------------------------------------
    return CompressFile
    
def FuncListZipContents():

    CompressFile = zipfile.ZipFile("D:\\ExampleZip.zip", 'r')
    
    # --------------------------------------------------
    # 调用 .namelist 方法可以得到压缩包里面的所有文件名。
    ListCompressFile = CompressFile.namelist()
    
    # --------------------------------------------------
    CompressFile.close()
    
    # --------------------------------------------------
    return ListCompressFile

def FuncUnZip():

    CompressFile = CompressFile = zipfile.ZipFile("D:\\ExampleZip.zip", 'r')
    
    # --------------------------------------------------
    ListCompressFile = CompressFile.namelist()
    
    # --------------------------------------------------
    for FileName in ListCompressFile:
        CompressFile.extract(FileName, r'D:\Dist')
        
        # ----------------------------------------------
        # 或者可以指定 pwd 的值，用于解压带密码的 Zip 文件 (支持 CRC32 传统 ZIP 2.0 加密)。
        #CompressFile.extract(FileName, r'D:\Dist', pwd="1234".encode("utf-8"))
        
        # ----------------------------------------------
        print("Extract File : %s" % FileName)
    
    # --------------------------------------------------
    # 或者可以使用 .extractall(r"D:\\Dist") 提取所有文件。
    
    # --------------------------------------------------
    CompressFile.close()
 
def FuncWriteZip():

    NewZip = zipfile.ZipFile("D:\\NewZip.zip", 'w')
    
    # --------------------------------------------------
    # 可以总是将 compress_type 的值设置为 zipfile.ZIP_DEFLATED 这个值。
    # ---- 有效选项 : ZIP_STORED
    # ---- 有效选项 : zipfile.ZIP_DEFLATED (deflate 压缩算法，它对各种类型的数据都比较有效)。
    # ---- 有效选项 : ZIP_BZIP2
    # ---- 有效选项 : ZIP_LZMA
    NewZip.write('Example.txt', compress_type=zipfile.ZIP_DEFLATED)
    
    # --------------------------------------------------
    NewZip.close()
    
def Running():

    VarZipPath = r"D:\\Python-Crack-Example-ZIP-4-Digit-CRC32.zip"

    #FuncOpenZip(VarZipPath)

    #FuncListZipContents(VarZipPath)

    FuncUnZip(VarZipPath)
    
if __name__ == "__main__":

    Running()
    
# ----------------------------------------------------------------------------------------------------
# EOF
