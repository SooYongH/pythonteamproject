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

# - 데이터 개수 세기
# - 데이터 정렬
# - 데이터 집계 : 합계, 평균, 최대, 최소
# - 데이터 삭제
# - 결측치 처리
# - 데이터 변경 : 자료형 변경 / 수치형 데이터를 범주형 데이터로 변경

# ## 4. 데이터 삭제

# - **Series.drop**(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
# 
# - **DataFrame.drop**(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')

# ### 1) 데이터프레임의 행 삭제

# - df.drop(labels='행이름', axis=0) : 행삭제 
# 
# 
# - 행삭제 후 데이터프레임으로 결과 반환
#      
#      
# - 원본에 반영되지 않으므로 원본수정하려면 저장해야 함
#     - 객체변수로 저장하거나, 매개변수 inplace를 True로 지정

# In[11]:


np.random.seed(1)
df2 = pd.DataFrame(np.random.randint(10, size=(4,8)))
df2
df2['합계'] = df2.sum(axis=1)
df2.loc['col_sum'] = df2.sum()
df2


# - df2의 col_sum 행 삭제

# In[12]:


# df2.drop(labels='col_sum', axis=0, inplace=True)
df2 = df2.drop(labels='col_sum', axis=0)
df2


# In[9]:


# del df2['합계']


# In[10]:


# df2


# ### 2) 데이터프레임의 열 삭제
# - df.drop(labels='행이름', axis=1) : 열 삭제
# - 행삭제 후 데이터프레임으로 결과 반환

# In[14]:


df2 = df2.drop(labels='합계', axis=1)
df2


# -----------------------------------

# ## 5. 결측치 처리
# 
# : **NaN 값 처리** 함수
# 
# - **df.dropna(axis=0 또는 1, inplace=False)**
#     - NaN값이 있는 열 또는 행을 삭제
#     - 원본 반영되지 않음
#     - inplace=True :원본 데이터프레임 변경
# 
# 
# - **df.fillna(0, inplace=False)**
#     - NaN값을 정해진 숫자로 채움
#     - 원본 반영 되지 않음

# #### 결측치 적용

# In[19]:


np.random.seed(10)
df3 = pd.DataFrame(np.random.randint(10, size=(4,8)))
df3


# In[20]:


df3.iloc[0,0]=np.nan
df3.iloc[2,3]=np.nan
df3.iloc[1,2]=np.nan
df3


# ### 1) 결측치 포함 행 삭제 : dropna()

# In[21]:


df3.dropna()
df3


# ### 2) 결측치 포함 열 삭제 : dropna(axis=1)

# In[22]:


df3.dropna(axis=1)
df3


# ### 3) 결측치를 다른 값으로 대체 : fillna() 함수

# **결측치를 0으로 변경**

# In[24]:


df3.fillna(0)
df3


# In[25]:


df3[0].fillna(0)
df3


# **결측치를 1로 변경**

# In[26]:


df3.fillna(1)


# In[27]:


df3[2].fillna(1)


# #### 결측치를 평균값으로 대체

# In[29]:


df3
df3[3].fillna(df3[3].mean(), inplace=True)
df3


# #### 결측치 확인

# In[33]:


df3.isna().sum()


# In[34]:


titanic = pd.read_csv('data/titanic.csv')
titanic.info()


# In[37]:


# 데이터프레임의 컬럼별 결측치 개수 확인
titanic.isna().sum()


# -------------------------------

# ## 6. 데이터의 변경

# ### 1) 데이터 자료형(dtype) 변경
# 
# 
# **astype(데이터형)**

# In[38]:


df3


# In[45]:


df3.iloc[3,3]=6.5
df3


# #### 데이터를 정수형으로 변경 : astype(int)

# In[46]:


df3.fillna(0).astype(int)


# In[47]:


# 지정된 컬럼의 데이터형식을 변경 {컬럼명:데이터유형, 컬럼명:데이터유형}
df3.astype({3:'int64'})


# #### 데이터를 실수형으로 변경 : astype(float)

# In[41]:


df3.astype(float)


# ### 2) 수치형 데이터를 범주형 데이터로 변환
# 
# - 범주형 데이터 **Categorical 클래스** 객체로 변환
# 
# 
# - **cut(data, bins, labels)** : 구간 경계선을 선정하여 범주형 데이터로 변환
#     - data : 구간 나눌 실제 값
#     - bins : 구간 경계값
#     - label: 카테고리 값
#         
#         
# - **qcut(data, bins, labels)** : 구간 경계선을 선정하지 않고 데이터 개수가 같도록 구간을 분할하여 범주형 데이터로 변환

# ### ① 구간 경계선을 선정하여 범주형 데이터로 변환 : cut()

# #### 리스트 데이터를 범주형 데이터로 변환

# - 예제 데이터

# In[56]:


ages = [0.1,0.5,5,4,6,3,10,31,15,33,37,17,25,36,70,61,20,40,31,100]
len(ages)


# - 구간 경계값, 범주 라벨 설정

# In[57]:


# 0 < 영유아 <= 5 
# 5 < 미성년자 <= 15
# 15 < 청소년  <= 20
# 20 < 청년   <= 40 
# 40 < 장년   <= 64
# 65 < 노년   <= 100

# 구간경계값
bins = [0, 5, 15, 20, 40, 64, 100]

# 구간별(범주) 라벨
labels = ['영유아', '미성년자', '청소년', '청년', '장년', '노년']


# - cut()로 범주형 데이터로 변경

# In[58]:


cut_ages= pd.cut(ages, bins=bins, labels=labels)
cut_ages


# In[60]:


type(cut_ages)


# In[59]:


list(cut_ages)


# In[63]:


df_age['나이대'].value_counts()


# In[65]:


df_age.나이.min()
df_age.나이.max()
df_age.나이.mean()


# In[66]:


df_age.describe()


# In[67]:


df_age.describe(include='all')


# **참고: Categorical 클래스 객체**
# 
# - 카테고리명 속성 : Categorical.categories
# 
# 
# - 코드 속성 : Categorical.codes 
#     - 인코딩한 카테고리 값을 정수로 갖음

# In[70]:


cut_ages.categories


# In[72]:


ages
cut_ages.codes


# #### 데이터프레임 데이터를 범주형으로 변환

# - ages 리스트를 데이터프레임으로 변경

# In[61]:


df_age = pd.DataFrame(ages, columns=['나이'])
df_age


# - 데이터프레임에 범주형 데이터 추가

# In[73]:


df_age['나이대'] = cut_ages
df_age.head()


# ### ② 데이터 개수가 같도록 데이터 분할 :  qcut()
# 
# **: 구간 경계선을 지정하지 않고 데이터의 사분위수(quantile) 기준으로 분할**
# 
# - 형식 : **pd.qcut(data,구간수,labels=[d1,d2....])**
# 
# 
# - 예. 1000개의 데이터를 4구간으로 나누려고 한다면
#      - qcut 명령어를 사용 한 구간마다 250개씩 나누게 된다.
#      - 예외) 같은 숫자인 경우에는 같은 구간으로 처리한다.

# - 예제 데이터

# In[74]:


# 정수난수 20개
np.random.seed(2)
data = np.random.randint(20, size=20)
data


# - 20개의 데이터를 동일한 개수를 갖는 4개 구간으로 나누어 범주형 데이터로 생성하고, 각 구간의 label은 Q1,Q2,Q3,Q4 로 설정

# In[75]:


qcut_data = pd.qcut(data, 4, labels=['q1','q2','q3','q4'] )
qcut_data


# In[76]:


list(qcut_data)


# In[78]:


data
np.sort(data)


# In[79]:


df_data = pd.DataFrame(data, columns=['data'])
df_data


# In[80]:


df_data['qcut'] = qcut_data
df_data


# In[81]:


qcut_data.categories


# In[83]:


data
qcut_data.codes


# -----
