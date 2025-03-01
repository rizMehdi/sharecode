import streamlit as st
import streamlit.components.v1 as components
import streamlit_survey as ss

def ChangeButtonColour(button_key, font_color, background_color='transparent'):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('div[data-testid="stButton"] button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].parentElement.parentElement.getAttribute('class').includes('{button_key}')) {{ 
                    elements[i].style.color ='{font_color}';
                    elements[i].style.background = '{background_color}'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def info(question_number):
    # extra info:
    if question_number == "Q1":
        with st.expander("Who is a Commonwealth Citizen?"):
            st.write("A Commonwealth citizen is a citizen of a Commonwealth of Nations member state. Check here if your conuntry is a commonwealth member https://thecommonwealth.org/our-member-countries")

    # why we asking this question
    if question_number == "Q2":
        with st.expander("Why we are asking this question?"):
            st.write('''
            This is to check if you are a habitual resident.
            'Habitual residence' means your main home is in the Common Travel Area and you do not have plans to live anywhere else.
            The Common Travel Area means the UK, Republic of Ireland, Channel Islands, or Isle of Man.
            Most people have to be habitually resident to apply for council housing. This applies to British and Irish citizens as well as other passport holders.
            For more information, please check the habitual residence test here: https://www.gov.uk/guidance/homelessness-code-of-guidance-for-local-authorities/annex-1-the-habitual-residence-test
            ''')
    elif question_number == "Q1":  
        with st.expander("Why we are asking this question?"):
            st.write('''British, Irish citizens, Commonwealth citizens with right to abode, and diplomats are eligible for housing assistance if they are habitually resident in the UK.
For further information, check the Homelessness code of guidance for local authorities here: https://www.gov.uk/guidance/homelessness-code-of-guidance-for-local-authorities/chapter-7-eligibility-for-assistance''')
   
def main():
    # Create a container to manage visibility of content
    content_container = st.container()
    st.image("img/IRESHAwide.png", width=200)
    
    # Set text size
    text_size = "16px"
    
    if st.session_state.get('button_clicked', False):
        # Clear the previous content
        content_container.empty()
        
        # Initialize the survey
        survey = ss.StreamlitSurvey("IRESHA Sharecode")

        # Define questions
        Q1 = ss.Radio(survey, "Are you any of the following?", options=[
            "British Citizen",
            "Irish Citizen",
            "Commonwealth Citizen",
            "Diplomat or their family member based in the UK",
            "None of the above"
        ], horizontal=False)

        Q2 = ss.Radio(survey, "Where do you currently live?", options=[
            "UK",
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the Above"
        ], horizontal=False)

        Q3 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False)

        createPage1 = ss.Radio(survey, "Are you any of the following?", options=[
            "British Citizen",
            "Irish Citizen",
            "Commonwealth Citizen",
            "Diplomat or their family member based in the UK",
            "None of the above"
        ], horizontal=False)

        habitual9 = ss.Radio(survey, "Where do you currently live?", options=[
            "UK",
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the Above"
        ], horizontal=False)

        commonwealth = ss.Radio(survey, "Do you have any of the following?", options=[
            "I have right to abode in UK",
            "I have indefinite leave to remain (settlement)",
            "I have limited leave to remain",
            "None of the above"
        ], horizontal=False)

        habitual10 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False)

        sponsorship1 = ss.Radio(survey, "Is your settled status based on a sponsorship?", options=[
            "Yes",
            "No"
        ], horizontal=False)

        habitual1 = ss.Radio(survey, "Where do you currently live?", options=[
            "UK",
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands"
        ], horizontal=False)

        habitual2 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False)

        exemption1 = ss.Radio(survey, "Are you in the UK as a result of deportation, expulsion or other removal by compulsion of law from another country to the UK?", options=[
            "Yes",
            "No"
        ], horizontal=False)

        habitual3 = ss.Radio(survey, "Where do you currently live?", options=[
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the Above"
        ], horizontal=False)

        habitual4 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 5 years",
            "5 years or more"
        ], horizontal=False)

        createPage2 = ss.Radio(survey, "Which of the following applies to you?", options=[
            "EEA national with a presettled status in the UK",
            "EEA national or family member with settled status in the UK",
            "National of any other country with indefinite leave to remain in the UK (Settlement)",
            "None of the above applies to me"
        ], horizontal=False)

        rejection1 = ss.Radio(survey, "Does any of the following apply to you?", options=[
            "My right to reside in the UK is only due to my jobseeker status",
            "I only have an initial right to reside in the UK",
            "None of the above applies to me"
        ], horizontal=False)

        createPage4 = ss.Radio(survey, "Are you a person or family member of a person who is a frontier worker in the UK before 31 December 2020?", options=[
            "None of the above applies to me"
        ], horizontal=False)

        createPage3 = ss.Radio(survey, "Are you a person/dependant of a person who:", options=[
            "Has a refugee status abroad",
            "Former asylum seeker who has been instructed to move but failed to do so (failed asylum seeker)",
            "Is in the UK in breach of UK immigration laws",
            "Failed asylum seeker with dependant children",
            "None of the above applies to me"
        ], horizontal=False)

        createPage5 = ss.Radio(survey, "Are you a person who:", options=[
            "Has a refugee status in the UK",
            "Has humanitarian protection",
            "Limited leave to enter and remain in the UK as the family member of a ‘relevant person of Northern Ireland’",
            "Is in the UK on the basis of the Afghan Relocations and Assistance Policy",
            "Had to move to the UK from Ukraine as part of the Russian invasion of Ukraine",
            "Is a victim of human trafficking/slavery and granted permission to stay in the UK",
            "Is a victim of transnational marriage abandonment and granted permission to stay in the UK",
            "None of the above applies to me"
        ], horizontal=False)

        habitual5 = ss.Radio(survey, "Where do you currently live?", options=[
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the Above"
        ], horizontal=False)

        habitual6 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False)

        createPage6 = ss.Radio(survey, "Are you a person who:", options=[
            "Has leave to enter or remain in the UK on family and private life grounds",
            "Has a British National Overseas Visa",
            "None of the above applies to me"
        ], horizontal=False)

        publicFunds1 = ss.Radio(survey, "Do you have access to public funds?", options=[
            "Yes",
            "No"
        ], horizontal=False)

        createPage7 = ss.Radio(survey, "Are you a person who:", options=[
            "Moved to the UK in connection with the collapse of the Afghanistan government",
            "Moved to the UK from Sudan in connection with the violence",
            "Moved to the UK in connection to the Hamas Terrorist Attack",
            "None of the above applies to me"
        ], horizontal=False)

        publicFunds2 = ss.Radio(survey, "Do you have access to public funds?", options=[
            "Yes",
            "No"
        ], horizontal=False)


        # st.markdown("""
        # <style>
        #        .block-container {
        #             padding-top: 0.75rem;
        #             padding-bottom: 0rem;
        #             padding-left: 1rem;
        #             padding-right: 1rem;
        #         }
        # </style>
        # """, unsafe_allow_html=True)

        
        # st.markdown("""
        # <style>
        # #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
        # </style>
        # """, unsafe_allow_html=True)



        # Apply custom styles to buttons and text
        st.markdown(f"""
            <style>
            .stButton > button {{
                background-color: green;
                color: white;
                margin-top: 0px;
                margin-bottom: 0px;
            }}
            .stButton > button:disabled {{
                background-color: white;
                color: grey;
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
            .stRadio > label {{
                font-size: 28px;
            }}
            </style>
            """, unsafe_allow_html=True)

        # Display questions based on the current page
        if st.session_state.get('current_page', 0) == 0:
            q1_value = Q1.display()
            if st.button("Next", key="next_0"):
                st.session_state['current_page'] = 1
                st.rerun()
            info("Q1")
            
        
        elif st.session_state.get('current_page', 0) == 1:
            if st.button("Back", key="back_1"):#, use_container_width=True):
                st.session_state['current_page'] = 0
                st.rerun()
            ChangeButtonColour('st-key-back_1', 'white', 'blue')
            q2_value = Q2.display()
            if st.button("Next", key="next_1"):#, use_container_width=True):
                st.session_state['current_page'] = 2
                st.rerun()
            info("Q2")
        elif st.session_state.get('current_page', 0) == 2:
            if st.button("Back", key="back_2"):
                st.session_state['current_page'] = 1
                st.rerun()
            ChangeButtonColour('st-key-back_2', 'white', 'blue')
            q3_value = Q3.display()
            if st.button("Generate Sharecode", key="submit"):
                st.json({
                    "used_st_before": q1_value,
                    "current_location": q2_value,
                    "residence_duration": q3_value
                })

            info("Q3")
        
    else:
        with content_container:
            # st.title("IRESHA Sharecode")
            # st.image("img/IRESHAlogo.png", width=200)
            # st.header("Immigration/Residence Status Eligibility for Social Housing Assistance - Sharecode")

            st.write("This webapp can be used to generate a sharecode indicating that you fulfil the minimum immigration/residence status eligibility requirements for social-housing assistance.")
            
            st.subheader("For applicants")
            st.write("To create a sharecode, you will be asked a series of questions to check if you have the minimum eligibility for social-housing assistance.")
            st.write("There might be additional requirements based on where you live or where you want to apply for social housing.")
            
            if st.button("Check eligibility and create sharecode"):
                st.session_state['button_clicked'] = True
                st.rerun()
        
if __name__ == "__main__":
    main()

