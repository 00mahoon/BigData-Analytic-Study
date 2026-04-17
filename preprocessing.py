import pandas as pd
import numpy as np

# 1. 데이터 생성
data = {
    'id': range(1, 11),
    'age': [25, 30, np.nan, 45, 22, 50, 35, np.nan, 40, 28],
    'income': [5000, 6000, 5500, 15000, 4500, 7000, np.nan, 5200, 6500, 4800]
}
df = pd.DataFrame(data)

def main():
    print("--- 원본 데이터 ---")
    print(df, "\n")

    # 2. 결측치 처리
    # age는 평균으로 채우고, income에 결측치가 있으면 그 행은 지웁니다.
    df['age'] = df['age'].fillna(df['age'].mean())
    df_cleaned = df.dropna(subset=['income']).copy()

    # 3. 이상치 처리
    # 소득(income)이 10,000을 넘는 데이터는 이상치로 보고 제거합니다.
    df_final = df_cleaned[df_cleaned['income'] <= 10000]

    # 4. 결과 도출
    # 최종 데이터의 나이(age) 평균을 구하고 반올림하여 정수로 출력합니다.
    result = int(round(df_final['age'].mean(), 0))
    
    print("--- 전처리 완료 후 결과 ---")
    print(f"최종 age 평균값: {result}")

if __name__ == "__main__":
    main()
