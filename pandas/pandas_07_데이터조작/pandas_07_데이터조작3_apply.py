#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# # 행/열에 동일한 연산 적용 apply()

# #### apply() 함수
# - DataFrame의 행이나 열에 복잡한 연산을 vectorizing 할 수 있게 해주는 함수
# - 매우 많이 활용되는 함수
# 
# 
# **형식 : apply(반복적용할 함수, axis=0/1)**
# - 0 : 열마다 반복
# - 1 : 행마다 반복 
# - 생략시 기본값 : 0

# ### 예제

# In[4]:


# 예제 df 생성
df = pd.DataFrame({'a':[1,3,4,3,4],
                   'b':[2,3,1,4,5],
                   'c':[1,5,2,4,4]
})
df


# ### 데이터프레임의 각 열에 sum() 함수 적용

# apply(함수, axis=0)

# In[6]:


df.sum(axis=1)


# In[9]:


data = np.random.randint(10, size=(10,))
data
np.sum(data)


# In[10]:


df
df.apply(np.sum)


# In[11]:


df.apply(np.sum, axis=0)


# In[12]:


df.sum()


# sum함수는 열 또는 행단위로 적용되는 함수여서 각 열별로 적용 됨

# ### 데이터프레임의 각 행에 sum() 함수 적용

# In[13]:


df.apply(np.sum, axis=1)


# In[14]:


df.sum(axis=1)


# ### 데이터프레임의 각 원소의 제곱값을 계산

# - 컬럼별 모든 원소에 대하여 np.square 함수 적용

# In[16]:


data
np.square(data)


# In[18]:


df
df.apply(np.square)


# - 행별 모든 원소에 대하여 np.square 함수 적용

# In[19]:


df.apply(np.square, axis=1)


# ## 사용자가 정의한 연산을 행/열단위 적용
# 
# ### lambda() & apply()
# 
# - 데이터프레임의 기본 집계함수(sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
#     - apply() 함수를 사용할 필요가 없음
# 
# 
# - apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용
#     - lambda 함수로 필요한 연산 기능을 구현하고, apply()를 통해 열/행 단위로 적용

# ### 1회성 함수 lambda 함수를  apply()에 사용하는 예제

# #### 예1. 집합데이터의 최대값과 최소값의 차이를 구하는 lambda 함수 정의

# In[21]:


diff = lambda x : x.max() - x.min()


# - 정의한 lambda함수 diif() 적용

# In[22]:


s = pd.Series([3, 10, -10, 15, 9])
diff(s)


# In[23]:


df


# In[24]:


df.apply(diff)


# In[25]:


df.apply(diff, axis=1)


# In[26]:


df.apply(lambda x:x.max()-x.min())


# - 직접 연산을 통해 각 행의 최대값과 최소값 차이 계산

# In[29]:


df.max() - df.min()


# In[30]:


df.max(axis=1) - df.min(axis=1)


# #### 예2. 데이터프레임 각 열의 데이터에 대한 범주별 빈도 계산

# In[31]:


df


# In[33]:


df.a.value_counts()
df.b.value_counts()
df.c.value_counts()


# In[40]:


for col in df.columns:
    print(f'{col}: Freq.')
    df[col].value_counts().sort_index()


# In[38]:


df.apply(pd.value_counts)


# #### 예3. 각 열의 데이터에 대한 범주별 빈도 계산 후, NaN값은 0으로 변환하고 전체 데이터 타입을 정수로 변환

# In[42]:


df.apply(pd.value_counts).fillna(0).astype(int)


# -----------------------------------------
