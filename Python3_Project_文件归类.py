# Python3_Project_文件归类.py

# Python 3.8.0

# Create By GF 2023-07-23 13:47

# --------------------------------------------------

import os
import re

# --------------------------------------------------

ListFilePath = list()

ListWhlPath = list()

ListTarGz = list()

# --------------------------------------------------

# 获取指定目录下的所有文件路径。
def FuncMyOsWalk(VarInPath:str):

    for Root, Folders, Files in os.walk(VarInPath):

        for File in Files:
        
            FilePath = os.path.join(Root, File)

            ListFilePath.append(FilePath)

    # ----------------------------------------------
    # End

# 对文件按后缀名进行分类。
def FuncClassifyFiles(ListFilePath:list):

    for File in ListFilePath:

        if File[-4:] == ".whl":

            ListWhlPath.append(File)

        elif File[-7:] == ".tar.gz":

            ListTarGz.append(File)

    # ----------------------------------------------
    # End

def FuncMatchWhlInfo(VarInWhlPath:str):

    WhlInfo = list()

    # 去除文件路径中的 Root 及 Folder 只保留文件名。
    FileName = re.sub(r"[a-zA-Z]\:.*\\", str(), VarInWhlPath)

    # WhlInfo[0] 代表 Wheel 包的名字。
    WhlInfo.append(re.search("[0-9a-zA-Z]*[\_0-9a-zA-Z]*", FileName).group())

    # WhlInfo[1] 代表 Wheel 包的版本。匹配模式：数字开头 + 数字或者 "." 号任意多个 + 数字结尾。
    WhlInfo.append(re.search("[0-9][\.0-9]*[0-9]", FileName).group())

    # WhlInfo[2] 代表 Wheel 包的适用平台。
    WhlInfo.append(re.findall("py[0-9]*|cp[0-9]*|pp[0-9]*", FileName))

    return WhlInfo

# 提取 Wheel 包的适用平台范围。
def FuncFetchWhlPlatformRange(ListWhlInfo:list):

    WhlPlatformRange = str()

    SetWhlPlatformRange = set()

    SetWhlPlatformAlpha = set()

    # ----------------------------------------------

    for WhlInfo in ListWhlInfo:

        for Platform in WhlInfo[2]:

            Alpha = re.search("[a-z]+", Platform).group()

            Num = re.search("[0-9]+", Platform).group()

            SetWhlPlatformAlpha.add(Alpha)

            SetWhlPlatformRange.add(int(Num))
    
    # ----------------------------------------------

    WhlPlatformAlpha = SetWhlPlatformAlpha.pop()

    WhlPlatformRange = WhlPlatformAlpha + str(min(SetWhlPlatformRange)) + str('-') + WhlPlatformAlpha + str(max(SetWhlPlatformRange))

    return WhlPlatformRange

def FuncSearchTarGzInfo(VarInFileName:str):
 
    VarInFileName = re.sub(r"[a-zA-Z]\:.*\\", str(), VarInFileName)

    TarGzName = re.search("[0-9a-zA-Z]*[\_0-9a-zA-Z]*", VarInFileName).group()

    return TarGzName

def FuncCreateNewFolder():

    NoRepeatFileName = set()

    for File in ListWhlPath:

        WhlInfo = FuncMatchWhlInfo(File)

        # WhlInfo[0] 代表 Wheel 包的名字。
        NoRepeatFileName.add(WhlInfo[0])

    # ----------------------------------------------

    for File in ListTarGz:

        print(FuncSearchTarGzInfo(File))

    # ----------------------------------------------

    for WhlName in NoRepeatFileName:

        ListWhlInfo = list()

        for Whl in ListWhlPath:

            if WhlName in Whl:

                WhlInfo = FuncMatchWhlInfo(Whl)

                ListWhlInfo.append(WhlInfo)

        # ------------------------------------------

        WhlPlatformRange = FuncFetchWhlPlatformRange(ListWhlInfo)

        print(WhlPlatformRange)

def Running():

    VarInPath = "D:\\Temp-Work"

    FuncMyOsWalk(VarInPath)

    FuncClassifyFiles(ListFilePath)

    FuncCreateNewFolder()

if __name__ == "__main__":

    Running()
