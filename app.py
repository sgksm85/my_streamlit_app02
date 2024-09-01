import streamlit as st
import os

# CSSの追加
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #ffcc00;
    }
    h1 {
        color: #52f6ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Markdownの表示
st.markdown("# LINE事例集")
st.write("これはあたしが集めた事例集です。")

# Markdownファイルの相対パスを指定
markdown_file_path = os.path.join(os.path.dirname(__file__), '../__LINE_Marketing_Research/Statistics/LINEの企業活用事例.md')

# Markdownファイルの読み込み
with open(markdown_file_path, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# セクションごとに分割する
sections = markdown_content.split('## ')
sections = ['## ' + section for section in sections if section.strip() != '']

# 検索バーの設置
search_query = st.text_input("検索キーワードを入力してください")

# 検索結果の表示
if search_query:
    search_results = []
    for section in sections:
        if search_query.lower() in section.lower():
            search_results.append(section)
    
    if search_results:
        st.write(f"検索結果 ({len(search_results)}件):")
        for result in search_results:
            st.markdown(result)
            st.markdown("---")
    else:
        st.write("該当する結果が見つかりませんでした。")
