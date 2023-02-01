#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# # pandas 데이터 파악과 조작

# **분석할 데이터를 수집(확보)하면 데이터의 특징을 파악하고 다루기 쉽게 변형하는 작업을 수행해야 한다**

# # #2. 데이터 조작

# - 데이터 개수 세기 : count(), value_counts()
# - 데이터 정렬 : sort_index(), sort_values(by=, )
# - 데이터 집계 : 합계(sum()), 평균(mean()), 최대(max()), 최소(min())
# - 데이터 삭제
# - 결측치 처리
# - 데이터 변경 : 자료형 변경 / 수치형 데이터를 범주형 데이터로 변경

# ## 1. 데이터 개수 세기(count)

# : **데이터 빈도(frequency) 계산**
# 
# - **count() 함수** 
#     - 시리즈의 경우 빈도 계산
#     - 데이터프레임의 경우 각 컬럼 또는 행의 데이터 빈도 계산
#     - NaN값은 세지 않음
#     
# 
# - **value_counts() 함수**
#     - 이산형, 범주형 데이터의 범주별 빈도 계산

# ### 1) count() 적용하여 개수 세기
# 
# - 형식 : **Series.count(level=None)**
# 
# 
# - 형식 : **DataFrame.count(axis=0, level=None, numeric_only=False)**
# 
#     - axis : 0 or 'index', 1 or 'columns' , default 0
#     - level : int or str, optinal (multiIndex의 경우)
#     - numerical_only : float, int, boolean data만 포함

# #### ① Series 데이터에 count() 함수 적용

# In[4]:


titanic = pd.read_csv('data/titanic.csv')
titanic.head(3)


# In[5]:


titanic.info()


# In[10]:


type(titanic['Survived'])


# In[12]:


titanic.Survived.count()


# In[13]:


titanic.Pclass.count()


# In[15]:


titanic.Age.count()


# In[16]:


for col in titanic.columns:
    print(f'{col} : {titanic[col].count()}')


# #### ② 데이터 프레임에 count()함수 적용
# - 각 열마다 데이터 개수를 세기 때문에 누락된 부분을 찾을 때 유용

# In[17]:


titanic.count()


# ### 2) value_counts()로 범주별 빈도 계산 
# 
# - 문자열 값을 갖는 데이터의 경우 **범주별 빈도(비율) 계산**
#     - ex. 성별(남,여), 선호도(종다, 보통, 싫다), 혈액형(A,B,O,AB) 등
#     
# - 수치형 데이터의 값별 빈도 계산
# 
# 
# - 형식 : **Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)**
#     - normalize : True인 경우 상대빈도 계산
#     - sort : 빈도 크기별로 정렬
#     - ascending : 오름차순으로 정렬
#     - bins : 범주 구간 수 지정
#     - dropna : False로 지정되면 NaN를 포함하여 빈도 계산
# 
# 
# - 형식 : **DataFrame.value_counts(subset=None, normalize=False, sort=True, ascending=False, dropna=True)**
# 

# #### ① 시리즈 데이터에  value_counts() 적용
# - 시리즈의 값이 정수, 문자열인 경우 각각의 값이 나온 횟수를 셀 수 있음
# - 파라미터 normalize=True 를 사용하면 각 값 및 범주형 데이터의 비율(상대빈도)을 계산
#     - 시리즈.value_counts(normalize=True)

# In[18]:


titanic.info()


# - 정수형 값을 갖는 시리즈 데이터에 value_counts() 적용

# In[19]:


titanic['Pclass'].value_counts()


# In[20]:


titanic.Survived.value_counts()


# In[21]:


titanic.SibSp.value_counts()


# - 실수형 값을 갖는 시리즈 데이터에 value_counts() 적용

# In[22]:


titanic.Age.value_counts()


# In[25]:


titanic.Age.value_counts(bins=10, sort=False)


# - 문자열 값을 갖는 시리즈 데이터에 value_counts() 적용

# In[26]:


titanic.Sex.value_counts()


# In[28]:


titanic.Sex.value_counts(normalize=True)*100


# #### ② 데이터프레임에  value_counts()  함수 사용
# 
# - 행(row)을 하나의 value로 설정하고 동일한 행이 몇 번 나타났는지의 빈도를 Series로 반환

# In[30]:


df = pd.DataFrame({'num_legs':[2,4,4,6],
                   'num_wings':[2,0,0,0]},
                index=['falcon','dog','cat','ant'])                  
df


# In[31]:


df.info()


# In[32]:


df['num_legs'].value_counts()


# In[33]:


df.value_counts()


# In[39]:


df2 = titanic[['Survived','Sex']]
df2.head()
df2.value_counts()


# In[40]:


df2.count()


# #### 문제. 타이타닉 데이터에서 Pclass에 따른 생존/사망 빈도 계산

# In[44]:


titanic[['Pclass', 'Survived']].value_counts(sort=False, normalize=True)*100


# In[45]:


titanic[['Pclass', 'Survived']].value_counts(ascending=True)


# In[47]:


df.loc['cat','num_wings']=np.nan
df


# In[49]:


# 결측치 제외
df.value_counts()


# In[50]:


df.value_counts(dropna=False)


# ----------------------------------

# ## 2. 데이터 정렬 
# 
# - 데이터 정렬을 위한 정렬 함수 사용
# - **sort_index()** : 인덱스를 기준으로 정렬
# - **sort_value()** : 데이터 값을 기준으로 정렬

# ### 1) 시리즈 정렬

# In[51]:


titanic.head(3)


# In[52]:


titanic.Pclass.value_counts()


# In[53]:


titanic.Pclass.sort_index()


# In[63]:


titanic.Pclass.value_counts(ascending=True).index


# In[64]:


titanic.Pclass.value_counts().sort_index()


# In[65]:


titanic.Pclass.value_counts().sort_index(ascending=False)


# In[66]:


titanic.Pclass.value_counts().sort_values()


# ### 2) 데이터 프레임 정렬
# 
# - **DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)**
#     - 특정열 값 기준 정렬
#     - 정렬시 기준열을 주어야 함. by 인수 사용(생략 불가)
#         - by = 기준열, by=[기준열1,기준열2]
#     - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)
#     
#     
# - **DataFrame.sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, ignore_index=False, key=None)**
#     - DataFrame의 INDEX 기준 정렬
#     - 오름차순/내림차순 : ascending = True/False (생략하면 오름차순)

# In[67]:


df


# - 데이터프레임의 값을 기준으로 정렬

# In[68]:


df.sort_values(by='num_wings')


# In[69]:


df.sort_values(by='num_legs')


# In[70]:


# 값의 내림차순으로 정렬
df.sort_values(by='num_wings', ascending=False)


# In[71]:


# 정렬기준이 여러개인 경우 : 리스트내에 정렬기준에 따른 컬럼명을 제시
# 첫번째 컬럼이 첫번째 정렬 기준이 됨
df.sort_values(by=['num_wings', 'num_legs'])


# In[72]:


df.sort_values(by=['num_legs', 'num_wings'])


# - 데이터프레임의 index를 기준으로 정렬

# In[74]:


df
df.sort_index()


# ---------------------------------------------------

# ### 연습문제
# 
# 1. 타이타닉 데이터에서 승객의 성별(Sex) 인원수, 나이별(Age) 인원수, 선실별(Pclass) 인원수, 사망/생존(Survived)인원수를 구하시오.

# In[ ]:


titanic = pd.read_csv('data/titanic.csv')
titanic.info()


# In[77]:


titanic.head(2)


# In[78]:


# 1-1. 타이타닉 승객에 대하여 성별 인원수 구하기
titanic['Sex'].value_counts()


# In[81]:


# 1-2. 타이타닉 승객에 대하여 나이별 인원수 구하기
titanic.Age.value_counts(bins=10, sort=False)
# titanic.Age.value_counts()


# In[82]:


# 1-3. 타이타닉 승객에 대하여 선실별 인원수 구하기
titanic.Pclass.value_counts()


# In[83]:


# 1-4. 타이타닉 승객에 대하여 사망/생존 인원수 구하기
titanic.Survived.value_counts()


# 2. 성별 인원수는 인덱스 기준으로 정렬하고, 나이별 인원수는 값 기준으로 정렬하시오.

# In[84]:


# 2-1. 타이타닉 승객에 대하여 성별 인원수를 인덱스 기준으로 정렬하기
titanic.Sex.value_counts().sort_index()


# In[85]:


# 2-2. 타이타닉 승객에 대하여 나이별 인원수를 값 기준으로 정렬하기
titanic.Age.value_counts().sort_values()


# ------------------------------------------------------

# ## 3. 데이터의 행/열의 합계, 평균, 최대값, 최소값

# : 데이터프레임에 적용되는 집계 관련 함수
# 
# - 합계 : **sum**(axis=0 또는 1)
#     - 각 열의 합계 계산 : axis=0(index) => 기본값
#     - 각 행의 합계 계산 : axis=1(column)
#     
#     
# - 평균 : **mean**(axis=0 또는 1)
# - 최소값 : **min**(axis=0 또는 1)
# - 최대값 : **max**(axis=0 또는 1)   

# **예제 데이터 프레임 생성**
# 예제 DF 생성
# 4행 8열의 데이터프레임 작성, 난수를 발생시키고
# 0-9범위에서 매번 같은 난수 발생되어 반환되도록 설정
# In[90]:


np.random.seed(1)
df2 = pd.DataFrame(np.random.randint(10, size=(4,8)))
df2


# ### 행/열의 합계(sum)

# #### 각 행의 합계 계산

# In[92]:


# axis=1 => 시리즈로 반환
df2.sum(axis=1)


# **각 열의 합계 계산**

# In[93]:


df2.sum()


# In[94]:


df2.sum(axis=0)


# ### 평균, 최소값, 최대값

# In[95]:


# 컬럼별 평균, 최소값, 최대값: axis=0
df2.mean()
df2.min()
df2.max()


# In[96]:


# 각 행의 평균, 최소값, 최대값
df2.mean(axis=1)
df2.min(axis=1)
df2.max(axis=1)


# #### 각 행의 합계를 새로운 열로 추가

# In[97]:


df2['합계'] = df2.sum(axis=1)
df2


# #### 각 열의 합계를 새로운 행으로 추가
# 
# : loc 인덱서를 사용하여 새로운 행 추가

# In[99]:


df2.loc['col_sum']=df2.sum()
df2


# -------------------------------------
