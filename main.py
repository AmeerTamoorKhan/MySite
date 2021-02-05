import streamlit as st
from CV import cv_func
import time
import webbrowser as wb
from bokeh.models.widgets import Div

st.set_page_config('Ameer Tamoor Khan', layout='wide')
first_author_publications = [
    '<a href="https://arxiv.org/abs/1807.02754" target="_blank">Khan, A. T., Senior, S. L., Stanimirovic, P. S., & Zhang, Y. (2018). Model-free optimization using eagle perching optimizer. arXiv preprint arXiv:1807.02754.</a>',
    '<a href="https://arxiv.org/pdf/1812.05452.pdf" target="_blank">Khan, A. T., Cao, X., & Li, S. (2018). A survey on blockchain technology and its potential applications in distributed control and cooperative robots. arXiv preprint arXiv:1812.05452.</a>',
    '<a href="https://www.researchgate.net/profile/Ameer_Tamoor_Khan2/publication/330715055_Blockchain_Technology_with_Applications_to_Distributed_Control_and_Cooperative_Robotics_A_Survey/links/5c51757492851c22a39a7b0a/Blockchain-Technology-with-Applications-to-Distributed-Control-and-Cooperative-Robotics-A-Survey.pdf" target="_blank">Khan, A. T., Cao, X., Li, S., & Milosevic, Z. (2019). Blockchain Technology with Applications to Distributed Control and Cooperative Robotics: A Survey. International Journal of Robotics and Control, 2(1), 36-48.</a>',
    '<a href="https://engine.scichina.com/publisher/scp/journal/SCIS/doi/10.1007/s11432-020-2894-9" target="_blank">Khan, A. T., Cao, X., Li, S., Hu, B., & Katsikis, V. N. (2020). Quantum beetle antennae search: a novel technique for the constrained portfolio optimization problem. SCIENCE CHINA Information Sciences.</a>',
    '<a href="https://ieeexplore.ieee.org/abstract/document/9199815" target="_blank">Khan, A. T., Li, S., Kadry, S., & Nam, Y. (2020). Control framework for trajectory planning of soft manipulator using optimized RRT algorithm. IEEE Access, 8, 171730-171743.</a>',
    '<a href="https://engine.scichina.com/publisher/scp/journal/SCIS/doi/10.1007/s11432-020-3073-5?slug=fulltext" target="_blank">Khan, A. T., & Li, S. Human Guided Cooperative Robotic Agents in Smart Home Using Beetle Antennae Search. SCIENCE CHINA Information Sciences.</a>',
    '<a href="https://www.sciencedirect.com/science/article/pii/S0263224120307922" target="_blank">Khan, A. T., Li, S., & Cao, X. (2021). Control framework for cooperative robots in smart home using bio-inspired neural network. Measurement, 167, 108253.</a>',
    '<a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/adc2.63" target="_blank">Khan, A. T., Li, S., & Li, Z. Obstacle Avoidance and Model‐free Tracking Control for Home Automation Using Bio‐inspired Approach. Advanced Control for Applications: Engineering and Industrial Systems, e63.</a>',

]

co_author_publications = [
    '<a href="https://eric.ed.gov/?id=EJ1236921" target="_blank">Rafique, M. U., Mohammed, A. M., Li, S., Khan, A. T., & Kadry, S. (2019). Integrating Open-Source Tools for Embedded Software Teaching: A Case Study. Advances in Engineering Education.</a>',
]

submitted_publications = {
    'Paper1': ['Name: Enhanced Beetle Antennae Search with Zeroing Neural Network For Online Solution of Constrained '
               'Optimization.', 'Author: First Author', 'Status: Major Revision']
}


def publications():
    row1 = st.beta_container()
    row2 = st.beta_container()
    cols = st.beta_columns(3)
    with row1:
        cols_row1 = st.beta_columns(3)
        cols_row1[1].title('Publications')
    with row2:
        # First author Publications
        st.subheader('First Author Publications')
        st.markdown('''<strong>2021:</strong>''', unsafe_allow_html=True)
        st.markdown(f'''
        <ol>
            <li>{first_author_publications[-1]}</li>
            <li>{first_author_publications[-2]}</li>
        </ol>
        ''', unsafe_allow_html=True)
        st.markdown('''<strong>2020:</strong>''', unsafe_allow_html=True)
        st.markdown(f'''
        <ol>
            <li>{first_author_publications[-3]}</li>
            <li>{first_author_publications[-4]}</li>
            <li>{first_author_publications[-5]}</li>
        </ol>
        ''', unsafe_allow_html=True)

        st.markdown('''<strong>2019:</strong>''', unsafe_allow_html=True)
        st.markdown(f'''
        <ol>
            <li>{first_author_publications[-6]}</li>
        </ol>
        ''', unsafe_allow_html=True)

        st.markdown('''<strong>2018:</strong>''', unsafe_allow_html=True)
        st.markdown(f'''
        <ol>
            <li>{first_author_publications[-7]}</li>
            <li>{first_author_publications[-8]}</li>
        </ol>
        <hr>
        ''', unsafe_allow_html=True)
        # Co author Publications
        st.subheader('Co Author Publications')
        st.markdown('''<strong>2019:</strong>''', unsafe_allow_html=True)
        st.markdown(f'''
        <ol>
            <li>{co_author_publications[-1]}</li>
        </ol>
        <hr>
        ''', unsafe_allow_html=True)

        # Submitted Publications
        st.subheader('Submitted Publications')
        st.markdown('''<strong>2021:</strong>''', unsafe_allow_html=True)
        st.markdown('''
        <p><strong>1) Name:</strong> Enhanced Beetle Antennae Search with Zeroing Neural Network For Online Solution of Constrained 
        Optimization</p>
        <p><strong>Journal:</strong> Neurocomputing<p>
        <p><strong>Author:</strong> First Author<p>
        <p><strong>Status:</strong> Major Revision<p>
        <br>
        ''', unsafe_allow_html=True)
        st.markdown('''
        <p><strong>2) Name:</strong> Zeroing Neural Network with Beetle Antennae
        Search: A Novel Tracking Controller For Surgical
        Manipulator Under RCM Constraint</p>
        <p><strong>Journal:</strong> IEEE RA-L<p>
        <p><strong>Author:</strong> First Author<p>
        <p><strong>Status:</strong> Under Review<p>
        <br>
        ''', unsafe_allow_html=True)
        st.markdown('''
        <p><strong>3) Name:</strong> Optimally Configured GRU-RNN Using Hyperband
        For The Long-Term Forecasting Of Solar PV Plant</p>
        <p><strong>Journal:</strong> IEEE TRANSACTIONS ON SUSTAINABLE ENERGY<p>
        <p><strong>Author:</strong> First Author<p>
        <p><strong>Status:</strong> Under Review<p>
        <br>
        ''', unsafe_allow_html=True)
        st.markdown('''
        <p><strong>4) Name:</strong> Trajectory Optimization of 5-link Biped Robot
        Using Beetle Antennae Search</p>
        <p><strong>Journal:</strong> IEEE TRANSACTIONS ON CIRCUITS AND SYSTEMS II: EXPRESS BRIEFS<p>
        <p><strong>Author:</strong> First Author<p>
        <p><strong>Status:</strong> Under Review<p>
        <br>
        ''', unsafe_allow_html=True)
        st.markdown('''
        <p><strong>5) Name:</strong> Using Quadratic Interpolated Beetle Antennae Search For Higher Dimensional Portfolio
        Selection Under Cardinality Constraints</p>
        <p><strong>Journal:</strong> Applied Mathematics and Computation<p>
        <p><strong>Author:</strong> First Author<p>
        <p><strong>Status:</strong> Under Review<p>
        <br>
        ''', unsafe_allow_html=True)
        st.markdown('''
        <p><strong>6) Name:</strong> Non-linear Activated Beetle Antennae Search: A Novel
        Technique for Non-Convex Tax-Aware</p>
        <p><strong>Journal:</strong> Expert Systems With Applications<p>
        <p><strong>Author:</strong> First Author<p>
        <p><strong>Status:</strong> Under Review<p>
        <br>
        ''', unsafe_allow_html=True)
# *****************************************************************************
# ************************* General Layout of Sidebar *************************
# *****************************************************************************
st.sidebar.subheader("Profile")
cv = st.sidebar.button("Curriculum Vitae")

st.sidebar.subheader("Data Science Projects")
twitter_bot = st.sidebar.button("Twitter Bot")
pinterest_bot = st.sidebar.button("Pinterest Bot")
quora_bot = st.sidebar.button("Quora Bot (Soon)")

st.sidebar.subheader("Machine Learning (ML) Section")
st.sidebar.markdown("<h4><strong>ML Projects\n</strong></h4>", unsafe_allow_html=True)
projects_ml = ['Diagnoser', 'Sentimeter', 'Trump-o-meter']
diagnoser = st.sidebar.button('Diagnoser')
senti_meter = st.sidebar.button('Sentimeter')
trump_meter = st.sidebar.button('Trump-o-meter')


st.sidebar.markdown("<h4><strong>ML Games</strong></h4>", unsafe_allow_html=True)
dino = st.sidebar.button("Dino (Soon)")
ai_pong = st.sidebar.button("AI Pong (Soon)")
autonomous_car = st.sidebar.button("Autonomous Car (Soon)")
avoid_obstacles = st.sidebar.button("Avoid Obstacles (Soon)")
build_bridge = st.sidebar.button("Building Bridges (Soon)")

st.sidebar.subheader("Publication Section")
publication = st.sidebar.button("Publications")

last = st.empty()
# *****************************************************************************
# ********************** End General Layout of Sidebar ************************
# *****************************************************************************

# *****************************************************************************
# ********************** Different Sidebar Sections ***************************
# *****************************************************************************

if cv:
    st.empty()
    cv_func()
elif twitter_bot:
    cv_func()
    js = "window.open('https://twitterbot.atkhan.info/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
elif pinterest_bot:
    cv_func()
    js = "window.open('https://pinterestbot.atkhan.info/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
elif diagnoser:
    cv_func()
    js = "window.open('https://diagnoser.atkhan.info/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
elif senti_meter:
    cv_func()
    js = "window.open('https://sentimeter.atkhan.info/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
elif trump_meter:
    cv_func()
    js = "window.open('https://trump-o-meter.atkhan.info/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
elif publication:
    publications()
else:
    cv_func()



