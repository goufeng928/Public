#! /usr/bin/env python3

import os
import re

Dict_Ends = {}

Dict_Ends_Explain = {".3":"IBM Embedded ViaVoice Voice Type Languages Scripts Data",
                     ".3t":"Advent 3B2 Text File, For Advanced Print Publisher",
                     ".ac":"GNU/Linux Autoconf Script, Requires GNU M4)",
                     ".asm":"用于在C++源码中内嵌汇编语言",
                     ".cc":"CC文件是Linux/Unix下为C++源文件的默认扩展名",
                     ".hpp":"hpp,其实质就是将.cpp的实现代码混入.h头文件当中，定义与实现都包含在同一文件",
                     ".cmake":"Cmake并不直接建构出最终的软件，而是产生标准的建构档",
                     ".m4":"Unix Macro Processor Functions Library",
                     ".man":"用于由UNIX系统编程实现的UNIX手册",
                     ".s":"汇编语言源程序，操作:汇编",
                     ".S":"汇编语言源程序，操作:预处理+汇编",
                     ".sh":"Bash (一种Unix Shell) 编程的脚本",
                     ".tcl":"TCL(Tool Command Language)是一种功能强大的脚本语言",
                     ".vcxproj":"VCXPROJ文件是由Visual C++创建的软件开发项目文件, 其中包括源代码文件和应用程序资源的引用",
                     ".x":"是微软为DX开发提供的一种3D文件"}

def WalkDirectoriesFile(Path: str):

    List_File = []

    # for循环中的Root获取当前根目录。
    # for循环中的FolderList获取Root下的所有文件夹并返回为列表。
    # for循环中的FileList获取Root下的所有文件并返回为列表。
    for Root, FolderList, FileList in os.walk(Path):
        
        for File in FileList:
            
            List_File.append(File)

    return List_File

def WalkDirectoriesRootFile(Path: str):

    List_Root_File = []

    # for循环中的Root获取当前根目录。
    # for循环中的FolderList获取Root下的所有文件夹并返回为列表。
    # for循环中的FileList获取Root下的所有文件并返回为列表。
    for Root, FolderList, FileList in os.walk(Path):
        
        for File in FileList:
            
            Root_File = os.path.join(Root, File)
            
            List_Root_File.append(Root_File)

    return List_Root_File

def StrHaveBatchCharVerify(String: str, BatchChar: list) -> list:

    Res = []

    for i in String:

        for j in BatchChar:

            if i == j:

                Res.append(i);

    return Res

def DirectoriesPathVerify(Path: str) -> int:

    illegal = [ '\\', '/', ':', '*', '?', '\"', '<', '>', '|'] # Windows下的文件夹非法名称。

    if '\\' not in Path and len(StrHaveBatchCharVerify(Path, illegal)) > int(0):

        return int(0)

    elif '\\' not in Path and len(StrHaveBatchCharVerify(Path, illegal)) == int(0):

        return int(1)

    elif '\\' in Path and len(StrHaveBatchCharVerify(Path, illegal)) > int(0):
        
        return int(0)

    elif '\\' in Path and len(StrHaveBatchCharVerify(Path, illegal)) == int(0):

        return int(1)

def RegexMatchEnds(Text: str):

    Pattern = re.compile(r"\.[a-zA-Z0-9]{1,}$")

    Object = Pattern.search(Text)

    if Object != None:

        return Object.group()

    else:

        return None

# 计数没有“.”的情况，计算完后删除这个列表元素。
def CountDotNonExistent(List_File: list):

    i = 0

    while i < len(List_File):

        if '.' not in List_File[i]:

            if "Dot-Non-Existent" not in Dict_Ends:

                Dict_Ends["Dot-Non-Existent"] = int(1)

            else:

                Dict_Ends["Dot-Non-Existent"] += int(1)

            del List_File[i]

        else:

            i += 1
            
# 计数“.”在前面的情况，计算完后删除这个列表元素。
def CountDotInHead(List_File: list):

    i = 0

    while i < len(List_File):

        if List_File[i][0] == '.':

            if "Dot-In-Head" not in Dict_Ends:

                Dict_Ends["Dot-In-Head"] = int(1)

            else:

                Dict_Ends["Dot-In-Head"] += int(1)

            del List_File[i]

        else:

            i += 1

            
# 计数“.”在后面的情况，计算完后删除这个列表元素。
def CountDotInTail(List_File: list):

    i = 0

    while i < len(List_File):

        if List_File[i][len(List_File[i]) - 1] == '.':

            if "Dot-In-Tial" not in Dict_Ends:

                Dict_Ends["Dot-In-Tail"] = int(1)

            else:

                Dict_Ends["Dot-In-Tail"] += int(1)

            del List_File[i]

        else:

            i += 1

def FetchFileEnds(List_File: list):

    List_Ends = []

    for File in List_File:

        Ends = RegexMatchEnds(File)

        if Ends == None:

            print("[ Notice ] 函数“RegexMatchEnds”未识别的文件：%s" %File)

        else:

            List_Ends.append(Ends)

    return List_Ends
		
def StatisticsFileEnds(Path: str):

    List_File = []

    List_File = WalkDirectoriesFile(Path)

    #################### Separate ####################

    CountDotNonExistent(List_File)

    CountDotInHead(List_File)

    CountDotInTail(List_File)

    #################### Separate ####################

    List_Ends = []

    List_Ends = FetchFileEnds(List_File)

    #################### Separate ####################

    for Ends in List_Ends:

        if Ends not in Dict_Ends:

            Dict_Ends[Ends] = int(1)

        else:

            Dict_Ends[Ends] += int(1)

    #################### Separate ####################

    print("[ Exe OK ] 函数“StatisticsFileEnds”执行结果如下：")

    for Key in Dict_Ends:

        print("%0-16s: %d" %(Key, Dict_Ends[Key]))

    #################### Separate ####################

    Dict_Ends.clear()

def main():

    while True:

        print("[ StEnds ] 请输入文件目录名称：")

        Path = input()

        if Path == "q":

            break

        elif Path == "" or Path == " ":

            continue

        else:
            
            StatisticsFileEnds(Path)
            

# 文件作为脚本直接执行,才执行以下条件.
# import到其他的Python脚本中被调用(模块重用)则不执行以下条件.
if __name__ == '__main__':

    #DirectoriesPathVerify("askfhkla klahsflka")

    main()
