import streamlit as st
import time

st.title('Streamlit超入門')
st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"イテレーション{i+1}")
  bar.progress(i+1)
  time.sleep(0.1)

'DONE!'


# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#   right_column.write('ここは右カラムです')

# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ内容を書く')

# option = st.selectbox(
#   '好きな数字は？',
#   list(range(1,11))
# )

# '好きな数字は',option,'です'

# hobby = st.text_input('趣味は？')
# condition = st.slider('今の調子は？',0,100,50)

# '私の趣味は',hobby,'です'
# '今の調子は',condition,'です'

# if st.checkbox('Show Image'):
#   img = Image.open('flower.jpg')
#   st.image(img,caption='花',use_column_width=True)

# df = pd.DataFrame(
#   np.random.rand(100,2)/[50,50]+[35.69,139.70],
#   columns=['lat','lon']
# )

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

#st.write(df) #ソートできる
# st.dataframe(df.style.highlight_max(axis=0),width=100,height=100) #ソートできる
# st.table(df.style.highlight_max(axis=0)) #ソートできない



"""
# 章
## 節
```Python
import streamlit as st
import numpy as np
import pandas as pd
```

"""