import streamlit as st
import streamlit_survey as ss

def main():
    # Create a container to manage visibility of content
    content_container = st.container()
    
    # Set text size
    text_size = "16px"
    
    if st.session_state.get('button_clicked', False):
        # Clear the previous content
        content_container.empty()
        
        # Initialize the survey
        survey = ss.StreamlitSurvey("IRESHA Sharecode")
        
        # Define each question separately
        q1 = survey.radio(
            "used_st_before",
            options=[
                "British Citizen",
                "Irish Citizen",
                "Commonwealth Citizen (?)",
                "Diplomat or their family member based in the UK",
                "None of the above"
            ],
            index=0,
            label_visibility="collapsed",
            horizontal=False,
        )
        
        q2 = survey.radio(
            "current_location",
            options=[
                "UK",
                "Republic of Ireland",
                "Isle of Man",
                "Channel Islands",
                "None of the Above"
            ],
            index=0,
            label_visibility="collapsed",
            horizontal=False,
        )
        
        q3 = survey.radio(
            "residence_duration",
            options=[
                "Less than 2 years",
                "2 years or more"
            ],
            index=0,
            label_visibility="collapsed",
            horizontal=False,
        )

        # Button customization
        submit_button = survey.default_btn_submit("Generate Sharecode")
        prev_button = survey.default_btn_previous("Back")
        next_button = survey.default_btn_next("Next")

        # Apply custom styles to buttons and text
        st.markdown(f"""
            <style>
            .stButton > button {{
                background-color: green;
                color: white;
            }}
            .stButton > button:disabled {{
                background-color: white;
                color: grey;
            }}
            .stButton > div:nth-child(1) > button {{
                background-color: blue;
                color: white;
            }}
            .stButton > button:hover {{
                color: white;
            }}
            .stMarkdown {{
                font-size: {text_size};
            }}
            .button-container {{
                display: flex;
                justify-content: space-between;
            }}
            </style>
            """, unsafe_allow_html=True)

        # Display questions based on the current page
        if st.session_state.get('current_page', 0) == 0:
            st.write("Are you any of the following?")
            q1.display()
            if next_button:
                st.session_state['current_page'] = 1
                st.rerun()
        
        elif st.session_state.get('current_page', 0) == 1:
            q2.display()
            if prev_button:
                st.session_state['current_page'] = 0
                st.rerun()
            if next_button:
                st.session_state['current_page'] = 2
                st.rerun()
        
        elif st.session_state.get('current_page', 0) == 2:
            q3.display()
            if prev_button:
                st.session_state['current_page'] = 1
                st.rerun()
            if submit_button:
                st.json(survey.to_json())
        
    else:
        with content_container:
            st.title("IRESHA Sharecode")
            st.header("Immigration/Residence Status Eligibility for Social Housing Assistance - Sharecode")

            st.write("This webapp can be used to generate a sharecode indicating that you fulfil the minimum immigration/residence status eligibility requirements for social-housing assistance.")
            
            st.subheader("For applicants")
            st.write("To create a sharecode, you will be asked a series of questions to check if you have the minimum eligibility for social-housing assistance.")
            st.write("There might be additional requirements based on where you live or where you want to apply for social housing.")
            
            if st.button("Check eligibility and create sharecode"):
                st.session_state['button_clicked'] = True
                st.rerun()
        
if __name__ == "__main__":
    main()

