import time

import streamlit as st

from resources import data_ncert_8_englishc1, data_ncert_8_mathc1, data_ncert_8_mathc2, data_ncert_mathc3

st.title("FiguraSolve")
st.markdown("The Perfect Place For Your Learning,Creativity and Thinking")
st.divider()
a = st.selectbox(
    "Please Select a Board of Education",
    [
        "Default(Toggle)",
        "AI-ResourceBuilder(RB)[Upcoming]",
        "CBSE",
        "STATE EDUCATION[Upcoming]",
    ],
)
if a == "CBSE":
    classn = st.selectbox(
        "Please select your Class", ["Default(Toggle)", "Class 8th", "Class 9th"]
    )
    st.divider()
    if classn == "Class 8th":
        with st.spinner("Loading Class 8th NCERT Resources", show_time=True):
            time.sleep(5)
            st.subheader(f"Resources for Class 8th,({a})")
            st.markdown(
                "Curated and Perfected Resources for Class 8th Ncert.Check all The Free Resources"
            )
            st.divider()
            subjectsn = st.selectbox(
                "Please Select a Subject(NCERT)",
                [
                    "Default(Toggle)",
                    "Maths(Part 1)",
                    "Science",
                    "English",
                    "Maths(Part 2)",
                ],
            )
            st.divider()
            chaptersn = st.selectbox(
                "Please Select a Chapter",
                ["Default(Toggle)", "Chapter 1", "Chapter 2", "Chapter 3"],
            )
            if subjectsn == "Maths(Part 1)" and chaptersn == "Chapter 1":
                st.header("Ganita Prakash(Part 1) Chapter 1: A Square and A Cube")
                st.divider()
                linktextbook1 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                    "Maths Textbook1"
                ]
                st.subheader("Math Textbooks Part 1 and 2")
                st.divider()
                st.markdown(f"1. [Math Textbook[Part 1]]({linktextbook1})")
                linktextbook2 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                    "Maths Textbook2"
                ]
                st.divider()
                st.markdown(f"2. [Math Textbook[Part 2]]({linktextbook2})")
                st.divider()
                st.markdown("A Square and A Cube(Contents)")
                with st.expander("1. Link Resources"):
                    linkti = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["l1"]
                    st.markdown(f"[Tiwari Academy]({linkti})")
                    linkti1 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["l2"]
                    st.markdown(f"[Ncert.Pdf]({linkti1})")
                    linkti2 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["l3"]
                    st.markdown(f"[Cbse.Academic]({linkti2})")
                    linkti3 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["l4"]
                    st.markdown(f"[MathisFun]({linkti3})")
                    st.divider()
                with st.expander("2. Video Resources"):
                    st.divider()
                    vidti1 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["Video Resources"]["vid1"]
                    st.markdown(f"[Youtube Video(1)]({vidti1})")
                    vidti2 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["Video Resources"]["vid2"]
                    st.markdown(f"[Youtube Video(2)]({vidti2})")
                    vidti3 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["Video Resources"]["vid3"]
                    st.markdown(f"[Youtube Video(3)]({vidti3})")
                    vidti4 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["Video Resources"]["vid4"]
                    st.markdown(f"[Youtube Video(4)]({vidti4})")
                with st.expander("3.Phet and Interaction Resources"):
                    ph1 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["Phet Simulation"]["phet_simulation_1"]
                    st.markdown(f"[Algebra Model by Phet Simulations]({ph1})")
                    inter1 = data_ncert_8_mathc1["Chapter 1"]["Resources"][
                        "Link Resources"
                    ]["Phet Simulation"]["Interaction"]["I1"]
                    st.markdown(f"[TCSION Interaction]({inter1})")
            if subjectsn == "Maths(Part 1)" and chaptersn == "Chapter 2":
                st.title("Ganita Prakash|Chapter-2:Power Play")
                st.subheader("Resources for Ganita Prakash: Power Play")
                st.divider()
                with st.expander("1. Link Resources"):
                    lin1 = data_ncert_8_mathc2["Resources(Link)"]["l1"]
                    st.markdown(f"1. [NCERT PDF]({lin1})")
                    lin2 = data_ncert_8_mathc2["Resources(Link)"]["l2"]
                    st.markdown(f"2. [LearnCbse]({lin2})")
                    lin3 = data_ncert_8_mathc2["Resources(Link)"]["l3"]
                    st.markdown(f"3. [The Study Path]({lin3})")
                    lin4 = data_ncert_8_mathc2["Resources(Link)"]["l4"]
                    st.markdown(f"4. [Tiwari Academy]({lin4})")
                with st.expander("2. Video Resources"):
                    vidi1 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "vid1"
                    ]
                    st.markdown(f"1. [Youtube Video: PowerPlay(1)]({vidi1})")
                    vidi2 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "vid2"
                    ]
                    st.markdown(f"2. [Youtube Video: Power Play(2)]({vidi2})")
                    vidi3 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "vid3"
                    ]
                    st.markdown(f"3. [Youtube Video: Power Play(3)]({vidi3})")
                    vidi4 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "vid4"
                    ]
                    vidi5 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "vid5"
                    ]
                    st.markdown(f"4. [Youtube Video: Power Play(4)]({vidi4})")
                    st.markdown(f"5. [Youtube Video: Power Play(5)]({vidi5})")
                    in1 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "Resources(I)"
                    ]["i1"]
                    in2 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "Resources(I)"
                    ]["i2"]
                    in3 = data_ncert_8_mathc2["Resources(Link)"]["Resources(Vid)"][
                        "Resources(I)"
                    ]["i3"]
                with st.expander("3. Interaction and Phet Resources"):
                    st.markdown(f"1. [TCSION INTERACTION]({in1})")
                    st.markdown(f"2. [Super Tutor]({in2})")
                    st.markdown(f"3. [Teachoo]({in3})")
            if chaptersn == "Chapter 3" and subjectsn == "Maths(Part 1)":
                st.title("Ganita Prakash: A Story of Numbers")
                st.divider()
                with st.expander("1. Link Resources"):
                    lin1 = data_ncert_mathc3["Resources"]["l1"]
                    st.markdown(f"1. [SchoolCareers360]({lin1})")
                    lin2 = data_ncert_mathc3["Resources"]["l2"]
                    st.markdown(f"2. [LearnCbse]({lin2})")
                    lin3 = data_ncert_mathc3["Resources"]["l3"]
                    lin4 = data_ncert_mathc3["Resources"]["l4"]
                    lin5 = data_ncert_mathc3["Resources"]["l5"]
                    lin6 = data_ncert_mathc3["Resources"]["l6"]
                    lin7 = data_ncert_mathc3["Resources"]["l7"]
                    st.markdown(f"3. [NCERT PDF]({lin3})")
                    st.markdown(f"4. [Sarthaks]({lin4})")
                    st.markdown(f"5. [Tiwari Academy]({lin5})")
                    st.markdown(f"6. [Mathify]({lin6})")
                    st.markdown(f"7. [Teachoo]({lin7})")
                with st.expander("2. Video Resources"):
                    vidn1 = data_ncert_mathc3["Resources"]["vid1"]
                    st.markdown(f"1. [Youtube Video: A Story of Numbers(1)]({vidn1})")
                    vidn2 = data_ncert_mathc3["Resources"]["vid2"]
                    vidn3 = data_ncert_mathc3["Resources"]["vid3"]
                    vidn4 = data_ncert_mathc3["Resources"]["vid4"]
                    st.markdown(f"2. [Youtube Video: A Story of Numbers(2)]({vidn2})")
                    st.markdown(f"3. [Youtube Video: A Story of Numbers(3)]({vidn3})")
                    st.markdown(f"4. [Youtube Video: A Story of Numbers(4)]({vidn4})")
                with st.expander("3. Interactive and Phet Resources"):
                    it1 = data_ncert_mathc3["Resources"]["i1"]
                    it2 = data_ncert_mathc3["Resources"]["i2"]
                    it3 = data_ncert_mathc3["Resources"]["i3"]
                    it4 = data_ncert_mathc3["Resources"]["i4"]
                    it5 = data_ncert_mathc3["Resources"]["i5"]
                    it6 = data_ncert_mathc3["Resources"]["i6"]
                    st.markdown(f"1. [TCSION]({it1})")
                    st.markdown(f"2. [SpinTheCrocodile]({it2})")
                    st.markdown(f"3. [SuperTutor Interactive]({it3})")
                    st.markdown(f"4. [Phet Colorado(1)]({it4})")
                    st.markdown(f"5. [Phet Colorado(2)]({it5}) ")
                    st.markdown(f"6. [People.UCSC: Ancient Calculator]({it6})")
            if chaptersn == "Chapter 1" and subjectsn == "English":
                st.title("English Poorvi: The Wit That Won Hearts")
                st.divider() 
                lik1 = data_ncert_8_englishc1["Resources"]["l1"]
                lik2 = data_ncert_8_englishc1["Resources"]["l2"]
                lik3 = data_ncert_8_englishc1["Resources"]["l3"]
                lik4 = data_ncert_8_englishc1["Resources"]["l4"] 
                lik5 = data_ncert_8_englishc1["Resources"]["l5"]
                with st.expander("1. Link Resources"):
                    st.markdown(f"1. [LearnCbse]({lik1})")
                    st.markdown(f"2. [Tiwari Academy]({lik2})")
                    st.markdown(f"3. [EnglishwithMrk]({lik3})") 
                    st.markdown(f"4. [SchoolCareers360]({lik4})")
                    st.markdown(f"5. [LearnInsta]({lik5})")
