#! /usr/bin/env python3

# Create By GF 2023-07-09 18:47

# Python3_Project_Pandas-VLookup.py

# Library : Pandas 1.4.1
# Library : openpyxl 3.0.9

# ----------------------------------------------------------------------------------------------------

import pandas as pd

# ----------------------------------------------------------------------------------------------------

def FuncPandasOpenExcel(VarExcelPath:str, VarHeaderRowNum:int):

    # 嵌套 open 打开方式需要配合 openpyxl 库。
    pf = pd.read_excel(open(VarExcelPath, 'rb'), sheet_name='Sheet1', header=VarHeaderRowNum)
    # --------------------------------------------------
    return pf

def FuncExcelToPandasDataFrame(VarExcelPath:str, VarHeaderRowNum:int):

    # 嵌套 open 打开方式需要配合 openpyxl 库。
    pf = pf = pd.read_excel(open(VarExcelPath, 'rb'), sheet_name='Sheet1', header=VarHeaderRowNum)
    # --------------------------------------------------
    df = pd.DataFrame(pf)
    # --------------------------------------------------
    return df

def FuncPandasDataFrameToExcel(DF, VarExportPath:str):

    # index=False 代表不会导出 index，就是最左侧的那一列。
    # header=None 代表不会导出第一行，也就是列头。
    # sheet_name="sheetname" 设置 Excel 文件脚注。
    DF.to_excel(VarExportPath, index=False)
    # --------------------------------------------------
    print("Export Excel : %s" % VarExportPath)

def Running():

    #pf = pd.read_excel(open("D:\\通力电器有限公司2006年上半年销售业绩统计表.xlsx", 'rb'), sheet_name='Sheet1', header=1)

    VarExcelPath = r"D:\\通力电器有限公司2006年上半年销售业绩统计表.xlsx"
    
    df = FuncExcelToPandasDataFrame(VarExcelPath, 1)
    
    df_groupby = df.groupby("部门").sum()
    
    print("销售（1）部 总销售额 : %d" % df_groupby.iloc[0, 0:].sum())
    print("销售（2）部 总销售额 : %d" % df_groupby.iloc[1, 0:].sum())
    print("销售（3）部 总销售额 : %d" % df_groupby.iloc[2, 0:].sum())
    
    # --------------------------------------------------
           
    Res = pd.DataFrame({"部门": ["销售（1）部", "销售（1）部", "销售（1）部"],
                        "总销售额": [df_groupby.iloc[0, 0:].sum(), df_groupby.iloc[1, 0:].sum(), df_groupby.iloc[2, 0:].sum()]}
                       )
           
    Res.to_excel("D:\\Result.xlsx", index=False)

if __name__ == '__main__':

    Running()

# ----------------------------------------------------------------------------------------------------
# EOF
