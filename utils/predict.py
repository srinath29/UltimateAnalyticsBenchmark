from statsmodels.api import OLS, WLS, GLSAR, RLM
from utils.helper import timeRepeater

import pandas as pd
import numpy as np
import statsmodels.api as sm
import datetime
import os

@timeRepeater
def modelTraining():
    dictSkuModels = {}
    dataFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Data", "data.xlsx")
    df = pd.read_excel(dataFile,sheetname=1)
    lisSku = list(np.unique(df["sku"]))
    df["PerChangeWrtMkt"] = (df.mkt_pr-df.sale_price)/df.mkt_pr
    df["Dom"] = df["date"].apply(lambda x: x.day)
    df["DowFlagNum"] = df["DowFlag"].apply(lambda x: 1 if x=="E" else 0)
    ndf = df[["sku","sales","sale_price","PerChangeWrtMkt","Dom","DowFlagNum"]]
    modelsList = ["LR: GLSAR","LR: OLS", "LR:WLS","RLR:HuberT"]
    for sku in lisSku:
        li = []
        requireDf = ndf[ndf["sku"]==sku].reset_index()
        requireDf = requireDf[["sales","sale_price","PerChangeWrtMkt","Dom","DowFlagNum"]]
        li.append(GLSAR(requireDf["sales"].astype(float),requireDf.ix[:,1:].astype(float)).fit())
        li.append(OLS(requireDf["sales"].astype(float),requireDf.ix[:,1:].astype(float)).fit())
        li.append( WLS(requireDf["sales"].astype(float),requireDf.ix[:,1:].astype(float)).fit())
        li.append(RLM(requireDf["sales"].astype(float), requireDf.ix[:, 1:].astype(float),M=sm.robust.norms.HuberT()).fit())
        dictSkuModels[sku] = li

