import sys

CaseInfo = {
    1:'10天内强势，今天1分钟信号线已变红，注意看1分钟走势图中信号线是否在一买位置附近刚变红',
    2:'近一个月中强势，今天1分钟信号线已变红，注意看1分钟走势图中信号线是否在一买位置附近刚变红'
}

ImageInfo = {
    1:"C:\\code\\pic\\10.jpg",
    2:"C:\\code\\pic\\30.jpg"
}


def GetCaseName(index):
    return CaseInfo[index]

def GetCaseResultImagePath(index):
    return ImageInfo[index]
