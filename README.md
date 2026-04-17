# Day 1: Data Preprocessing Basics

## 📌 프로젝트 개요
- **목표:** 빅데이터 분석기사 실기 제1유형 완벽 대비를 위한 데이터 전처리 기초 연습
- **주요 작업:** 결측치(Missing Values) 대치 및 이상치(Outliers) 제거

## 🛠 사용 기술 (Tech Stack)
- Python 3.x
- Pandas
- NumPy

## 📝 주요 학습 내용 및 회고
1. **결측치 제어:** - `fillna()`를 활용하여 연속형 변수의 결측치를 평균(mean)으로 대치하는 방법 숙지.
   - `dropna()`를 사용하여 핵심 타겟 변수에 결측치가 있는 레코드를 안전하게 삭제.
2. **이상치 필터링:** - 조건부 인덱싱(`df[df['column'] <= limit]`)을 활용하여 도메인 지식 기반의 이상치 제거 수행.
3. **결과 산출:** - 요구사항에 맞춘 집계 함수(`mean()`) 사용 및 `round()`를 통한 정수형 반올림 연산 처리.

## 🚀 실행 방법
```bash
python preprocessing.py
