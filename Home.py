import streamlit as st
from datetime import datetime

# 设置页面配置
st.set_page_config(
    page_title="易见 | 一键数据洞察",
    page_icon="🔍",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .logo-title {
        font-size: 72px;
        font-weight: bold;
        background: linear-gradient(45deg, #1e3d59, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 40px;
        font-family: 'Arial Black', sans-serif;
    }
    .subtitle {
        font-size: 24px;
        color: #1e3d59;
        text-align: center;
        margin-top: -30px;
        font-weight: 500;
    }
    .nav-bar {
        background-color: #1e3d59;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        position: sticky;
        top: 0;
        z-index: 999;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .nav-bar a {
        color: white;
        margin: 0 25px;
        text-decoration: none;
        font-size: 18px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .nav-bar a:hover {
        color: #ff6b6b;
    }
    .card {
        padding: 30px;
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.9);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px;
        text-align: center;
        transition: transform 0.3s ease;
        backdrop-filter: blur(5px);
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .news-ticker {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        overflow: hidden;
        white-space: nowrap;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .news-ticker span {
        display: inline-block;
        padding-right: 50px;
        animation: ticker 30s linear infinite;
    }
    .news-ticker a {
        color: #1e3d59;
        text-decoration: none;
        margin-right: 50px;
        transition: color 0.3s ease;
    }
    .news-ticker a:hover {
        color: #ff6b6b;
    }
    @keyframes ticker {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    .feature-section {
        padding: 40px 20px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        margin: 30px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        backdrop-filter: blur(5px);
    }
    .feature-title {
        font-size: 32px;
        color: #1e3d59;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 顶部导航栏
st.markdown("""
    <div class="nav-bar">
        <a href="#home">🏠 主页</a>
        <a href="#data-analysis">📊 数据分析</a>
        <a href="#trend-insights">🌏 趋势洞察</a>
    </div>
    """, unsafe_allow_html=True)

# 主页面内容
st.markdown('<p class="logo-title">易见</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">一键洞察数据 · 智启商业未来</p>', unsafe_allow_html=True)

# 创建两列布局展示主要功能
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card">
        <h2>📊 数据分析</h2>
        <p>深入分析商品销售数据，了解销售趋势、用户行为和商品表现。提供多维数据可视化，助力精准决策。</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="card">
        <h2>🌏 趋势洞察</h2>
        <p>实时跟踪全球电商平台搜索趋势，掌握市场动向。智能预测市场走向，把握商机。</p>
        </div>
        """, unsafe_allow_html=True)

# 特色功能展示
st.markdown("""
    <div class="feature-section">
        <h2 class="feature-title">为什么选择易见</h2>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px; margin: 15px; text-align: center;">
                <h3>🚀 快速部署</h3>
                <p>简单易用的界面设计，快速上手，即刻开始数据分析之旅</p>
            </div>
            <div style="flex: 1; min-width: 250px; margin: 15px; text-align: center;">
                <h3>📈 实时更新</h3>
                <p>数据实时同步，市场趋势实时掌握，不错过任何机会</p>
            </div>
            <div style="flex: 1; min-width: 250px; margin: 15px; text-align: center;">
                <h3>🎯 精准分析</h3>
                <p>多维度数据分析，深度洞察市场，助力精准决策</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 底部新闻滚动
st.markdown("""
    <div class="news-ticker">
        <span>
            <a href="https://news.example.com/1" target="_blank">🚀 亚马逊推出新跨境物流服务</a>
            <a href="https://news.example.com/2" target="_blank">📈 2024全球电商市场增长预测发布</a>
            <a href="https://news.example.com/3" target="_blank">🌐 最新跨境电商政策解读</a>
            <a href="https://news.example.com/4" target="_blank">🛒 全球消费者行为分析报告</a>
            <a href="https://news.example.com/5" target="_blank">💡 跨境电商新机遇分析</a>
        </span>
    </div>
    """, unsafe_allow_html=True)

# 添加页脚
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("© 2024 易见 | 一键数据洞察")
with col2:
    st.markdown("联系我们：contact@yijian.com")
with col3:
    st.markdown(f"最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")