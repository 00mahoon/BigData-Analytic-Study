{\rtf1\ansi\ansicpg949\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import numpy as np\
\
# \uc0\u44032 \u49345 \u51032  \u45936 \u51060 \u53552  \u49373 \u49457  (\u49892 \u51228  \u49884 \u54744 \u50640 \u49436 \u45716  pd.read_csv('data.csv') \u49324 \u50857 )\
data = \{\
    'id': range(1, 11),\
    'age': [25, 30, np.nan, 45, 22, 50, 35, np.nan, 40, 28],\
    'income': [5000, 6000, 5500, 15000, 4500, 7000, np.nan, 5200, 6500, 4800]\
\}\
df = pd.DataFrame(data)\
\
def main():\
    print("--- \uc0\u50896 \u48376  \u45936 \u51060 \u53552  ---")\
    print(df, "\\n")\
\
    # 1. \uc0\u44208 \u52769 \u52824  \u52376 \u47532 : 'age'\u51032  \u44208 \u52769 \u52824 \u45716  \u54217 \u44512 \u51004 \u47196  \u45824 \u52404 , 'income'\u51032  \u44208 \u52769 \u52824 \u45716  \u54665  \u49325 \u51228 \
    df['age'] = df['age'].fillna(df['age'].mean())\
    df_cleaned = df.dropna(subset=['income']).copy()\
\
    # 2. \uc0\u51060 \u49345 \u52824  \u52376 \u47532 : 'income'\u51060  10000 \u52488 \u44284 \u51064  \u45936 \u51060 \u53552 \u45716  \u51060 \u49345 \u52824 \u47196  \u44036 \u51452 \u54616 \u44256  \u51228 \u44144 \
    df_final = df_cleaned[df_cleaned['income'] <= 10000]\
\
    # 3. \uc0\u44208 \u44284  \u46020 \u52636 : \u52572 \u51333  \u45936 \u51060 \u53552 \u51032  'age' \u54217 \u44512 \u44050 \u51012  \u44396 \u54616 \u44256  \u48152 \u50732 \u47548 \u54616 \u50668  \u51221 \u49688 \u47196  \u52636 \u47141 \
    result = int(round(df_final['age'].mean(), 0))\
    \
    print("--- \uc0\u51204 \u52376 \u47532  \u50756 \u47308  \u54980  \u44208 \u44284  ---")\
    print(f"\uc0\u52572 \u51333  age \u54217 \u44512 \u44050 : \{result\}")\
\
if __name__ == "__main__":\
    main()}