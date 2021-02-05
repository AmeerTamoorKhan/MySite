import streamlit as st


def cv_func():
    header = st.beta_container()
    with header:
        cols = st.beta_columns((1, 0.6, 2, 1))
        cols[1].image('media/profile.png', width=150)
        cols[2].markdown('''
        <style>
            .header{
                line-height:1pt;
            }
        </style>
        <div class='header'>
        <h2 class="header">Ameer Tamoor Khan</h2>
        <h4 class="header">Ph.D. Student</h4>
        <h4 class="header"><strong>Email: </strong><a href="mailto:drop-in@atkhan.info">drop-in@atkhan.info</a></h4>
        <h4 class="header"><strong>Linkedin:</strong> <a href="https://www.linkedin.com/in/ameer-tamoor-khan-39571076/" target ="_blank">ameer-tamoor-khan</a></h4>
        <h4 class="header"><strong>Contact:</strong> +852-91397094</h3>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('''<hr>''', unsafe_allow_html=True)
    portions = st.beta_columns((1.5, 2.1, 1.5, 1))
    with portions[0]:
        st.markdown('''
            <style>
                .education{
                    line-height:1px;
                    font-weight:normal;
                }
            </style>
            <h3 class="education"><b>Education</b></h3>
            <h4 class="education"><b>Ph.D. In Computing</b></h4>
            <h4 class="education">The Hong Kong Polytechnic University</h4>
            <h4 class="education"><b>Status:</b> 2018-Present-2022</h4>
            <!-- <h4 class="education"><b>Expected:</b> June </h4> -->
            <!--<h4 class="education"><b>CGPA:</b> 3.57/4</h4> -->
            <h4 class="education"><b>Research:</b> Optimization, Robotics</h4>
            <h4 class="education">Machine Learning, Data Science.</h4>
            <h4 class="education"><b>Publications:</b> 9</h4>
            <h4 class="education"><b>First Author:</b> 8</h4>
            <h4 class="education"><b> <b> Co-Author:</b> 1</h4>
            <h4 class="education"><b>Submitted (Additional):</b> 6</h4>
            <br>
            <h4 class="education"><b>BS-Electrical (Electronics)</b></h4>
            <h4 class="education">PIEAS, Pakistan.</h4>
            <h4 class="education"><b>Status:</b> 2013-2017</h4>
            <h4 class="education"><b>CGPA:</b> 3.85/4</h4>
            <h4 class="education"><b>Thesis:</b> Tremor Sensing and Minimi-</h4>
            <h4 class="education">zation using Non-invasive Technique</h4>
            <h4 class="education"></h4>
        ''', unsafe_allow_html=True)
    with portions[1]:
        st.markdown('''
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <style>
                .experience{
                    line-height:1px;
                    font-weight:normal;
                }
                .checked {
                    color: orange;
                }
            </style>
            <h3 class="experience"><b>Experience</b></h3>
            <h4 class="experience"><b>Research Assistant (2017-2018)</b></h4>
            <h4 class="experience">The Hong Kong Polytechnic University</h4>
            <h4 class="experience"><b>Research:</b> Soft-robotics Control And Path-Planing.</h4>
            <br style="line-height:1px">
            <h4 class="experience"><b>PTCL (Intern: 2016)</b></h4>
            <h4 class="experience"><b>Department:</b> IP Network Services</h4>
            <h4 class="experience"><b>Job:</b> Improve network operations, enhance network</h4>
            <h4 class="experience"> resilience, bandwidth capacity, latency & packet loss.</h4>
            <br>
            <h4 class="experience"><b>PTCL (Intern: 2016)</b></h4>
            <h4 class="experience"><b>Department:</b> Customer Services</h4>
            <h4 class="experience"><b>Job:</b> Improve customer’s network experience</h4>
            <br>
            <h4 class="experience"><b>Writing Creek (Freelancer: 2017-2018)</b></h4>
            <h4 class="experience"><b>Rank:</b> Intermediate Writer</h4>
            <h4 class="experience"><b>Success rate:</b> 96% &nbsp;&nbsp; &nbsp;&nbsp; <b>Rating:</b> 4.75
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star checked"></span>
            <span class="fa fa-star-half-o checked"></span></h4>
        ''', unsafe_allow_html=True)
    with portions[2]:
        st.markdown('''
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <style>
                .publications{
                    line-height:1px;
                    font-weight:normal;
                }
                .checked {
                    color: orange;
                }
                .note{
                    font-weight:normal;
                    border-radius: 10px;
                    border: 2px solid rgba(75, 181, 67, 0.75);
                    text-align: center;
                    background: rgba(75, 181, 67, 0.75);
                    opacity: 0.75;
                }
            </style>
            <h3 class="publications"><b>Publications</b></h3>
            <h5 class="publications"><b>2021:</b></h5>
            <ol>
            <li><a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/adc2.63" target="_blank" style="font-size:12px">Obstacle Avoidance and Model‐free Tracking Control for Home Automation Using Bio‐inspired Approach</a></li>
            <li><a href="https://www.sciencedirect.com/science/article/pii/S0263224120307922" target="_blank" style="font-size:12px">Control framework for cooperative robots in smart home using bio-inspired neural network</a></li>
            </ol>
            <h5 class="publications"><b>2020:</b></h5>
            <ol>
            <li><a href="https://engine.scichina.com/publisher/scp/journal/SCIS/doi/10.1007/s11432-020-3073-5?slug=fulltext" target="_blank" style="font-size:12px">Human Guided Cooperative Robotic Agents in Smart Home Using Beetle Antennae Search</a></li>
            <li><a href="https://ieeexplore.ieee.org/abstract/document/9199815" target="_blank" style="font-size:12px">Control Framework for Trajectory Planning of Soft Manipulator Using Optimized RRT Algorithm</a></li>
            <li><a href="https://engine.scichina.com/publisher/scp/journal/SCIS/doi/10.1007/s11432-020-2894-9" target="_blank" style="font-size:12px">Quantum Beetle Antennae Search: A Novel Technique for The Constrained Portfolio Optimization Problem</a></li>
            </ol>
            <h4 class="note">Check <b>'Publication Section'</b> For More Publications</h4>
        ''', unsafe_allow_html=True)
    with portions[3]:
        st.markdown('''
            
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            
            <style>
                .skills{
                    line-height:1px;
                    font-weight:normal;
                }
                .checked {
                    color: orange;
                }
            </style>
            <h3 class="skills"><b>Software Skills</b></h3>
            <h4 class="skills"><b>Professional:</b></h4>
            <h4 class="skills">Python, Numpy, Pandas</h4>
            <h4 class="skills">Keras, Tensorflow.</h4>
            <h4 class="skills"><b>Intermediate:</b></h4>
            <h4 class="skills">Pytorch, Matlab, C, C++</h4>
            <h4 class="skills"><b>Familiar:</b></h4>
            <h4 class="skills">HTML, CSS, Javascript</h4>
            <hr>
                        
            <h3 class="skills"><b>Email</b></h3>
            <h4 class="skills"> &nbsp;
                   <a href="mailto:ameertamkhan1992@gmail.com"><i class="fas fa-envelope fa-2x" style="color:#FF5733"></i></a> &nbsp;
                   <a href="mailto:drop-in@atkhan.info"><i class="fas fa-envelope fa-2x" style="color:#FF5733"></i></a> &nbsp;
                   <a href="mailto:ameer.khan@connect.polyu.hk"><i class="fas fa-envelope-open-text fa-2x" style="color:#2d6eb9"></i></a> &nbsp;
            </h4>                                  
            <h3 class="skills"><b>Links</b></h3>
            <h4 class="skills"><a href="https://www.facebook.com/Tam947" target="_blank"><i class="fa fa-facebook-square fa-2x" style="color:#3b5998"></i></a> &nbsp;
                               <a href="https://github.com/AmeerTamoorKhan" target="_blank"><i class="fa fa-github-square fa-2x" style="color:#000000"></i></a> &nbsp;
                               <a href="https://www.researchgate.net/profile/Ameer_Tamoor_Khan" target="_blank"><i class="fab fa-researchgate fa-2x" style="color:#5cc9bb" target="_blank"></i></a> &nbsp;
                               <a href="https://www.linkedin.com/in/ameer-tamoor-khan-39571076/" target="_blank"><i class="fa fa-linkedin-square fa-2x" style="color:#2c66bc" target="_blank"></i></a> &nbsp;
            </h4>
            <script src="https://code.iconify.design/1/1.0.7/iconify.min.js"></script>
        ''', unsafe_allow_html=True)
    st.markdown('''<hr>''', unsafe_allow_html=True)
