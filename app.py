import streamlit as st

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
        color: #ff6600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Markdownの表示
st.markdown("# カスタマイズされたタイトル")
st.write("これはカスタマイズされたStreamlitアプリケーションです。")

# Markdownファイルの読み込み
with open('/Users/shigikasumi/Dropbox/Projects/Projects/01_REXLI/__LINE_Marketing_Research/Statistics/LINEの企業活用事例.md', 'r', encoding='utf-8') as file:
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
