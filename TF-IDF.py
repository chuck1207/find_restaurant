import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 식당 메타 정보 
meta = pd.read_csv("meta.csv")
meta.head()

# 리뷰
review = pd.read_csv("review.csv")
review.head()

#특수문자 제거 
review['review'] = review['review'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]"," ")

# 식당별 리뷰 통합 
result = []
for t in review.title.unique():
    reviews = ''
    for r in review.loc[review.title == t,'review']:
        reviews += (f' {r}')
        
        # print(t,'\t',reviews)
    result.append(pd.DataFrame({"title":t,'review':reviews},index = [0]))

df = pd.concat(result).reset_index(drop = True)

# tf-idf matrix 생성 
min_df_vectorizer = TfidfVectorizer(min_df = 2) 
tfidf_matrix = min_df_vectorizer.fit_transform(df.review.tolist()).toarray()

# 코사인 유사도 계산
cosine_sim = cosine_similarity(tfidf_matrix,tfidf_matrix)

indices = pd.Series(df.index, index=df['title'])

# 유사도 기반의 상위 10개의 식당 추출 
get_recommendations(df['title'][1], cosine_sim=cosine_sim)
