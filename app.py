import streamlit as st
import streamlit.components.v1 as components
import streamlit_survey as ss
from datetime import datetime


st.set_page_config(
    page_title="IRESHA Sharecode",
    page_icon="🏠"
    # page_icon="/img/favicon.png"
)


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
    # why we asking this question
    with st.expander("Why we are asking this question?"):
        if question_number == "habitual9":
            st.write('''
            This is to check if you are a habitual resident.
            'Habitual residence' means your main home is in the Common Travel Area and you do not have plans to live anywhere else.
            The Common Travel Area means the UK, Republic of Ireland, Channel Islands, or Isle of Man.
            Most people have to be habitually resident to apply for council housing. This applies to British and Irish citizens as well as other passport holders.
            For more information, please check the habitual residence test here: https://www.gov.uk/guidance/homelessness-code-of-guidance-for-local-authorities/annex-1-the-habitual-residence-test
            ''')
        elif question_number == "createPage1":  
            st.write('''British, Irish citizens, Commonwealth citizens with right to abode, and diplomats are eligible for housing assistance if they are habitually resident in the UK.
            For further information, check the Homelessness code of guidance for local authorities here: https://www.gov.uk/guidance/homelessness-code-of-guidance-for-local-authorities/chapter-7-eligibility-for-assistance''')
        else:
            st.write("")
    if question_number == "createPage1":
        with st.expander("Who is a Commonwealth Citizen?"):
            st.write("A Commonwealth citizen is a citizen of a Commonwealth of Nations member state. Check here if your conuntry is a commonwealth member https://thecommonwealth.org/our-member-countries")
    else:
        st.write("")




def show(result):
    if result == "result1" or result == "result5" or result == "result11":
        st.warning(
    """
    You have been referred to a case worker.  

    #### What this means  
    You need to have already resided in the **United Kingdom, Republic of Ireland, Isle of Man,** or **Channel Islands** for at least **two continuous years**. However, there may be exceptions, and a case worker will assess your situation further.  

    #### What to do next  
    You can still create a **sharecode**, but you may need to answer additional questions or provide further documents to help the case worker determine your eligibility for social housing. After creating the sharecode, please contact your potential housing provider directly.  

    You can also seek advice from the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**  
    """
)
    elif result == "result2" or result == "result4" or result == "result7" or result == "result10" or result == "result15":
        st.success(
    """
    You fulfil the minimum eligibility requirements for social-housing assistance  

    #### What this means?  
    Based on your answers, you fulfil the minimum eligibility requirements for seeking social-housing assistance. Please note that there might be additional requirements that you may need to fulfil, depending on where you live or where you want to apply for social housing.  

    #### What to do next?  
    You can go ahead and create a **sharecode**. This sharecode can be shared with your housing association or local authority.  
    """
)
    elif result == "result3" or result == "result12":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance.  

    #### What this means  
    You can only apply for housing assistance if you currently live in the **United Kingdom, Republic of Ireland, Isle of Man,** or **Channel Islands**.  

    #### What to do next  
    If you are facing **homelessness,** need **urgent housing support,** or further **advice,** you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**  
    """
)

    elif result == "result6":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance at the moment.  

    #### What this means?  
    You cannot apply for social housing if you are a **Commonwealth citizen** but do not have **Indefinite Leave to Remain (ILR)** or the **right to reside** in the UK. For more information, please check section 7.14 of the **Homelessness Code of Guidance for Local Authorities** here: [Homelessness Code of Guidance](https://www.gov.uk/guidance/homelessness-code-of-guidance-for-local-authorities/chapter-7-eligibility-for-assistance).  

    #### What to do next?  
    You can wait until you have **Indefinite Leave to Remain (ILR)** or settlement and apply afterward.  

    If you are facing **homelessness**, need **urgent housing support**, or need further **advice**, you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**  
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**  
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**  
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**
    """
)
    elif result == "result8":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance at the moment.  

    #### What this means?  
    As an **EEA national** with **pre-settled status** in the UK, you cannot apply for social housing if:  
    - Your right to reside in the UK is only due to your **jobseeker status**, or  
    - You only have an **initial right to reside** in the UK.  

    #### What to do next?  
    If you are facing **homelessness**, need **urgent housing support**, or need further **advice**, you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**  
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**  
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**  
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**
    """
)
    elif result == "result9":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance at the moment.  

    #### What this means?  
    You cannot apply for social housing if you are a person or dependent of a person who:  
    - Has **refugee status** abroad  
    - Is a **former asylum seeker** who has been instructed to move but failed to do so (failed asylum seeker)  
    - Is in the UK in **breach of UK immigration laws**  
    - Is a **failed asylum seeker** with dependent children  

    #### What to do next?  
    If you are facing **homelessness**, need **urgent housing support**, or need further **advice**, you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**  
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**  
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**  
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**
    """
)
    elif result == "result13":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance at the moment.  

    #### What this means?  
    You cannot apply for social housing if you do not have access to **public funds** while on a **British National Overseas (BNO) visa**. However, you may be able to apply for a **"change of conditions"** to access public funds if you meet certain criteria.  

    Please see the highlighted text on this website:  
    [Public Funds Access](https://www.gov.uk/government/publications/public-funds/public-funds-accessible#:~:text=For%20this%20reason%2C%20the%20majority,affecting%20their%20income%20or%20expenditure).  

    #### What to do next?  
    If you are facing **homelessness**, need **urgent housing support**, or need further **advice**, you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**  
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**  
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**  
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**
    """
)
    elif result == "result14":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance at the moment.  

    #### What this means?  
    You cannot apply for social housing if you do not have access to **public funds** while on a **British National Overseas (BNO) visa**. However, you may be able to apply for a **"change of conditions"** to access public funds if you meet certain criteria.  

    Please see the highlighted text on this website:  
    [Public Funds Access](https://www.gov.uk/government/publications/public-funds/public-funds-accessible#:~:text=For%20this%20reason%2C%20the%20majority,affecting%20their%20income%20or%20expenditure).  

    #### What to do next?  
    If you are facing **homelessness**, need **urgent housing support**, or need further **advice**, you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**  
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**  
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**  
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**
    """
)
    elif result == "result16":
        st.info(
    """
    You do not meet the minimum requirements to be eligible for housing assistance at the moment.  

    #### What to do next?  
    If you are facing **homelessness**, need **urgent housing support**, or need further **advice**, you can contact the following organisations:  

    - **[Shelter England](https://england.shelter.org.uk/get_help)**  
    - **[Shelter Scotland](https://scotland.shelter.org.uk/about_us/contact_us)**  
    - **[Citizen Advice (England)](https://www.citizensadvice.org.uk/about-us/information/chat-with-an-adviser-online/)**  
    - **[Citizen Advice Scotland](https://www.citizensadvice.org.uk/scotland/housing/)**
    """
)   
    else:
        st.write("Unknown state. Please resert the app")     


def main():
    st.session_state['prevAnswer']="None"
    st.logo("img/IRESHAwide.png")
    verbose=True
    # verbose=True
    # if verbose: st.write(st.session_state.get('current_page', "start"))
    # if verbose: st.write(st.session_state.get('prevAnswer', "None"))
    # Create a container to manage visibility of content
    content_container = st.container()
    
    
    # Set text size
    text_size = "16px"
    
    if st.session_state.get('button_clicked', False):
        # st.image("img/IRESHAwide.png", width=200)
        # Clear the previous content
        content_container.empty()
        
        # Initialize the survey
        survey = ss.StreamlitSurvey("IRESHA Sharecode")
        # st.session_state['current_page'] = "createPage1"
        # Define questions
        createPage1 = ss.Radio(survey, "Are you any of the following?", options=[
            "British Citizen",
            "Irish Citizen",
            "Commonwealth Citizen",
            "Diplomat or their family member based in the UK",
            "None of the above"
        ], horizontal=False, key="createPage1")

        habitual9 = ss.Radio(survey, "Where do you currently live?", options=[
            "UK",
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the above"
        ], horizontal=False, key="habitual9")

        commonwealth = ss.Radio(survey, "Do you have any of the following?", options=[
            "I have right to abode in UK",
            "I have indefinite leave to remain (settlement)",
            "I have limited leave to remain",
            "None of the above"
        ], horizontal=False, key="commonwealth")

        habitual10 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False, key="habitual10")

        sponsorship1 = ss.Radio(survey, "Is your settled status based on a sponsorship?", options=[
            "Yes",
            "No"
        ], horizontal=False, key="sponsorship1")

        habitual1 = ss.Radio(survey, "Where do you currently live?", options=[
            "UK",
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands"
        ], horizontal=False, key="habitual1")

        habitual2 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False, key="habitual2")

        exemption1 = ss.Radio(survey, "Are you in the UK as a result of deportation, expulsion or other removal by compulsion of law from another country to the UK?", options=[
            "Yes",
            "No"
        ], horizontal=False, key="exemption1")

        habitual3 = ss.Radio(survey, "Where do you currently live?", options=[
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the above"
        ], horizontal=False, key="habitual3")

        habitual4 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 5 years",
            "5 years or more"
        ], horizontal=False, key="habitual4")

        createPage2 = ss.Radio(survey, "Which of the following applies to you?", options=[
            "EEA national with a presettled status in the UK",
            "EEA national or family member with settled status in the UK",
            "National of any other country with indefinite leave to remain in the UK (Settlement)",
            "None of the above applies to me"
        ], horizontal=False, key="createPage2")

        rejection1 = ss.Radio(survey, "Does any of the following apply to you?", options=[
            "My right to reside in the UK is only due to my jobseeker status",
            "I only have an initial right to reside in the UK",
            "None of the above applies to me"
        ], horizontal=False, key="rejection1")

        createPage4 = ss.Radio(survey, "Are you a person or family member of a person who is", options=[
            "a worker in the UK",
            "self-employed in the UK?",
            "frontier worker in the UK before 31 December 2020",
            "None of the above applies to me"
        ], horizontal=False, key="createPage4")

        createPage3 = ss.Radio(survey, "Are you a person/dependant of a person who:", options=[
            "Has a refugee status abroad",
            "Former asylum seeker who has been instructed to move but failed to do so (failed asylum seeker)",
            "Is in the UK in breach of UK immigration laws",
            "Failed asylum seeker with dependant children",
            "None of the above applies to me"
        ], horizontal=False, key="createPage3")

        createPage5 = ss.Radio(survey, "Are you a person who:", options=[
            "Has a refugee status in the UK",
            "Has humanitarian protection",
            "Limited leave to enter and remain in the UK as the family member of a ‘relevant person of Northern Ireland’",
            "Is in the UK on the basis of the Afghan Relocations and Assistance Policy",
            "Had to move to the UK from Ukraine as part of the Russian invasion of Ukraine",
            "Is a victim of human trafficking/slavery and granted permission to stay in the UK",
            "Is a victim of transnational marriage abandonment and granted permission to stay in the UK",
            "None of the above applies to me"
        ], horizontal=False, key="createPage5")

        habitual5 = ss.Radio(survey, "Where do you currently live?", options=[
            "Republic of Ireland",
            "Isle of Man",
            "Channel Islands",
            "None of the above"
        ], horizontal=False, key="habitual5")

        habitual6 = ss.Radio(survey, "Since how long have you been residing in your current place of residence?", options=[
            "Less than 2 years",
            "2 years or more"
        ], horizontal=False, key="habitual6")

        createPage6 = ss.Radio(survey, "Are you a person who:", options=[
            "Has leave to enter or remain in the UK on family and private life grounds",
            "Has a British National Overseas Visa",
            "None of the above applies to me"
        ], horizontal=False, key="createPage6")

        publicFunds1 = ss.Radio(survey, "Do you have access to public funds?", options=[
            "Yes",
            "No"
        ], horizontal=False, key="publicFunds1")

        createPage7 = ss.Radio(survey, "Are you a person who:", options=[
            "Moved to the UK in connection with the collapse of the Afghanistan government",
            "Moved to the UK from Sudan in connection with the violence",
            "Moved to the UK in connection to the Hamas Terrorist Attack",
            "None of the above applies to me"
        ], horizontal=False, key="createPage7")

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
        if st.session_state.get('current_page') == "createPage0":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                st.session_state['button_clicked'] = False
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            st.markdown(
                """
                **Before you start:**  
                You will be asked a series of questions to assess your minimum eligibility for social housing assistance.  
                - Under each question, you can click to see why that question is being asked.  
                - For certain terms, additional information is available. Look under the questions for additional information.  

                **Things you will need:**  
                - An **email address** to get a one-time code.  
                - Your **e-visa** or **biometric resident permit**, or any other document related to permission to stay in the UK, if you require such permission.
                """
            )
            # if verbose: st.write("createPage1_value", createPage1_value)
            if st.button("Next", key="next_createPage1"):
                st.session_state['current_page'] = "createPage1"#2
                st.rerun()


        elif st.session_state.get('current_page') == "verifySharecode":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                st.session_state['button_clicked'] = False
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            # st.markdown(
            #     """
            #     This feature is disabled for now. Please go back to the previous page to continue."""
            # )

            # Sharecode input
            sharecode = st.text_input("Please enter the sharecode supplied by the applicant")

            # Date of birth input in dd/mm/yyyy format
            dob_str = st.text_input("Please enter the date of birth of the applicant (dd/mm/yyyy)")

            # Check if the date of birth is valid
            if dob_str:
                try:
                    # Try parsing the date input in dd/mm/yyyy format
                    dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
                    
                    # Check if the date of birth is in the future
                    if dob > datetime.today().date():
                        st.error("The date of birth cannot be in the future. Please enter a valid date.")
                    else:
                        # Calculate age
                        age = datetime.today().year - dob.year
                        if datetime.today().month < dob.month or (datetime.today().month == dob.month and datetime.today().day < dob.day):
                            age -= 1  # Adjust age if the birthday hasn't occurred yet this year

                        # Example: check if the applicant is at least 18 years old
                        if age < 18:
                            st.error("The applicant must be at least 18 years old.")
                        # else:
                        #     st.success(f"The applicant is {age} years old. Verification can proceed.")
                except ValueError:
                    # Handle invalid date format
                    st.error("Invalid date format. Please enter the date in dd/mm/yyyy format.")
            else:
                st.warning("Please enter the date of birth.")
            if st.button("Submit", key="submit_sharecode"):
                st.session_state['button_clicked'] = True
                st.session_state['current_page'] = "sharecodeResult_No"#0
                st.rerun()
            ChangeButtonColour('st-key-check_eligibility', 'white', 'green')


        elif st.session_state.get('current_page') == "sharecodeResult_Yes":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "verifySharecode"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            st.write("Sharecode verification successful !")
            st.success(
                """
                **Sharecode:** 3UB3C6CLY  
                **It is valid until:** 2025-02-13  
                **Name:** John Smith  
                **Status:** The applicant fulfils the minimum eligibility requirements for social-housing assistance.
                """
            )



        elif st.session_state.get('current_page') == "sharecodeResult_No":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "verifySharecode"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            st.error(
                """
                **Sorry, we are unable to verify the sharecode which you gave us.**
                
                Please make sure that the sharecode and the date of birth of the applicant are typed in correctly.
                """
            )

        elif st.session_state.get('current_page') == "sharecode":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                # st.session_state['button_clicked'] = False
                st.session_state['current_page'] = "habitual10"#0
                # st.session_state['current_page'] = "habitual2"#0
                # st.session_state['current_page'] = "exemption1"#0
                # st.session_state['current_page'] = "createPage4"#0
                # st.session_state['current_page'] = "habitual6"#0
                # st.session_state['current_page'] = "publicFunds2"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            # st.markdown(
            #     """
            #     This feature is disabled for now. Please go back to the previous page to continue."""
            # )
            # Title or header
            st.subheader("Enter your information")
            # First name input
            st.text_input("What is your first name? (This should be the same as on your identity document)")
            # Last name input
            st.text_input("What is your last name? (This should be the same as on your identity document)")


        # Display questions based on the current page
        elif st.session_state.get('current_page') == "createPage1":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                # st.session_state['button_clicked'] = False
                st.session_state['current_page'] = "createPage0"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage1_value = createPage1.display()
            st.session_state['prevAnswer'] = createPage1_value
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("createPage1_value", createPage1_value)
            if createPage1_value=="British Citizen" or createPage1_value=="Irish Citizen" or createPage1_value=="Diplomat or their family member based in the UK":
                if st.button("Next", key="next_habitual9"):
                    st.session_state['current_page'] = "habitual9"#1
                    st.rerun()
            elif createPage1_value=="Commonwealth Citizen":  
                if st.button("Next", key="next_commonwealth"):
                    st.session_state['current_page'] = "commonwealth"#2
                    st.rerun()
            elif createPage1_value=="None of the above": 
                if st.button("Next", key="next_createPage2"):
                    st.session_state['current_page'] = "createPage2"#3
                    st.rerun()
            info("createPage1")


        elif st.session_state.get('current_page') == "habitual9":#1:#habitual9
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage1"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual9_value = habitual9.display()
            st.session_state['prevAnswer'] = habitual9_value
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual9_value", habitual9_value)
            if habitual9_value=="None of the above": 
                if st.button("Next", key="next_result3"):
                    st.session_state['current_page'] = "result3"
                    st.rerun()
            else:
                if st.button("Next", key="next_habitual10"):
                    st.session_state['current_page'] = "habitual10"
                    st.rerun()
            info("habitual9")

        elif st.session_state.get('current_page') == "habitual10":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual9"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual10_value = habitual10.display()
            st.session_state['prevAnswer'] = habitual10_value
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual10_value", habitual10_value)
            if habitual10_value=="Less than 2 years": 
                if st.button("Next", key="next_result1"):
                    st.session_state['current_page'] = "result1"
                    st.rerun()
            elif habitual10_value=="2 years or more": 
                if st.button("Next", key="next_result2"):
                    st.session_state['current_page'] = "result2"
                    st.rerun()
            info("habitual10")

        elif st.session_state.get('current_page') == "commonwealth":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage1"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            commonwealth_value = commonwealth.display()
            st.session_state['prevAnswer'] = commonwealth_value
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if commonwealth_value=="I have right to abode in UK": 
                if st.button("Next", key="next_habitual1"):
                    st.session_state['current_page'] = "habitual1"
                    st.rerun()
            elif commonwealth_value=="I have indefinite leave to remain (settlement)": 
                if st.button("Next", key="next_sponsorship1"):
                    st.session_state['current_page'] = "sponsorship1"
                    st.rerun()
            elif commonwealth_value=="I have limited leave to remain" or commonwealth_value=="None of the above": 
                if st.button("Next", key="next_result6"):
                    st.session_state['current_page'] = "result6"
                    st.rerun()
            info("commonwealth")


        elif st.session_state.get('current_page') == "sponsorship1":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "commonwealth"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            sponsorship1 = sponsorship1.display()
            st.session_state['prevAnswer'] = sponsorship1
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if sponsorship1=="Yes": 
                if st.button("Next", key="next_habitual1"):
                    st.session_state['current_page'] = "habitual1"
                    st.rerun()
            elif sponsorship1=="No": 
                if st.button("Next", key="next_habitual3"):
                    st.session_state['current_page'] = "habitual3"
                    st.rerun()
            info("sponsorship1")

        elif st.session_state.get('current_page') == "habitual1":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "sponsorship1"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual1 = habitual1.display()
            st.session_state['prevAnswer'] = habitual1
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if habitual1=="None of the above": 
                if st.button("Next", key="next_result3"):
                    st.session_state['current_page'] = "result3"
                    st.rerun()
            else: 
                if st.button("Next", key="next_habitual2"):
                    st.session_state['current_page'] = "habitual2"
                    st.rerun()
            info("habitual1")

        elif st.session_state.get('current_page') == "habitual2":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual1"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual2 = habitual2.display()
            st.session_state['prevAnswer'] = habitual2
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual10_value", habitual10_value)
            if habitual2=="Less than 2 years": 
                if st.button("Next", key="next_exemption1"):
                    st.session_state['current_page'] = "exemption1"
                    st.rerun()
            elif habitual2=="2 years or more": 
                if st.button("Next", key="next_result4"):
                    st.session_state['current_page'] = "result4"
                    st.rerun()
            info("habitual2")        

        elif st.session_state.get('current_page') == "exemption1":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual1"#0
                # st.session_state['current_page'] = "habitual4"#0todotodotodotodotodotodo
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            exemption1 = exemption1.display()
            st.session_state['prevAnswer'] = exemption1
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual10_value", habitual10_value)
            if exemption1=="Yes": 
                if st.button("Next", key="next_result4"):
                    st.session_state['current_page'] = "result4"
                    st.rerun()
            elif exemption1=="No": 
                if st.button("Next", key="next_result5"):
                    st.session_state['current_page'] = "result5"
                    st.rerun()
            info("exemption1")  

        elif st.session_state.get('current_page') == "habitual3":#1:#habitual9
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "sponsorship1"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual3 = habitual3.display()
            st.session_state['prevAnswer'] = habitual3
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if habitual3=="None of the above": 
                if st.button("Next", key="next_result3"):
                    st.session_state['current_page'] = "result3"
                    st.rerun()
            else:
                if st.button("Next", key="next_habitual4"):
                    st.session_state['current_page'] = "habitual4"
                    st.rerun()
            info("habitual3")            


        elif st.session_state.get('current_page') == "habitual4":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual3"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual4 = habitual4.display()
            st.session_state['prevAnswer'] = habitual4
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if habitual4=="Less than 5 years": 
                if st.button("Next", key="next_exemption1"):
                    st.session_state['current_page'] = "exemption1"
                    st.rerun()
            elif habitual4=="5 years or more": 
                if st.button("Next", key="next_result4"):
                    st.session_state['current_page'] = "result4"
                    st.rerun()
            info("habitual4")    

        elif st.session_state.get('current_page') == "createPage2":#0:#createPage1
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage1"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage2 = createPage2.display()
            st.session_state['prevAnswer'] = createPage2
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if createPage2=="EEA national with a presettled status in the UK": 
                if st.button("Next", key="next_rejection1"):
                    st.session_state['current_page'] = "rejection1"#1
                    st.rerun()
            elif createPage2=="EEA national or family member with settled status in the UK":  
                if st.button("Next", key="next_sponsorship1"):
                    st.session_state['current_page'] = "sponsorship1"#2
                    st.rerun()
            elif createPage2=="National of any other country with indefinite leave to remain in the UK (Settlement)":  
                if st.button("Next", key="next_sponsorship1"):
                    st.session_state['current_page'] = "sponsorship1"#2
                    st.rerun()
            elif createPage2=="None of the above applies to me": 
                if st.button("Next", key="next_createPage3"):
                    st.session_state['current_page'] = "createPage3"#3
                    st.rerun()
            info("createPage2")


        elif st.session_state.get('current_page') == "rejection1":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage2"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            rejection1 = rejection1.display()
            st.session_state['prevAnswer'] = rejection1
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if rejection1=="My right to reside in the UK is only due to my jobseeker status" or rejection1=="I only have an initial right to reside in the UK": 
                if st.button("Next", key="next_result8"):
                    st.session_state['current_page'] = "result8"
                    st.rerun()
            else:
                if st.button("Next", key="next_createPage4"):
                    st.session_state['current_page'] = "createPage4"
                    st.rerun()
            info("rejection1")   



        elif st.session_state.get('current_page') == "createPage4":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "rejection1"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage4 = createPage4.display()
            st.session_state['prevAnswer'] = createPage4
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if createPage4=="None of the above applies to me": 
                if st.button("Next", key="next_habitual1"):
                    st.session_state['current_page'] = "habitual1"
                    st.rerun()
            else:
                if st.button("Next", key="next_result7"):
                    st.session_state['current_page'] = "result7"
                    st.rerun()
            info("createPage4")    



        elif st.session_state.get('current_page') == "createPage3":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage2"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage3 = createPage3.display()
            st.session_state['prevAnswer'] = createPage3
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if createPage3=="None of the above applies to me": 
                if st.button("Next", key="next_createPage5"):
                    st.session_state['current_page'] = "createPage5"
                    st.rerun()
            else:
                if st.button("Next", key="next_result9"):
                    st.session_state['current_page'] = "result9"
                    st.rerun()
            info("createPage3")



        elif st.session_state.get('current_page') == "createPage5":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage3"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage5 = createPage5.display()
            st.session_state['prevAnswer'] = createPage5
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if createPage5=="None of the above applies to me": 
                if st.button("Next", key="next_createPage6"):
                    st.session_state['current_page'] = "createPage6"
                    st.rerun()
            else:
                if st.button("Next", key="next_habitual5"):
                    st.session_state['current_page'] = "habitual5"
                    st.rerun()
            info("createPage5")




        elif st.session_state.get('current_page') == "habitual5":#1:#habitual9
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage5"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual5 = habitual5.display()
            st.session_state['prevAnswer'] = habitual5
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if habitual5=="None of the above": 
                if st.button("Next", key="next_result12"):
                    st.session_state['current_page'] = "result12"
                    st.rerun()
            else:
                if st.button("Next", key="next_habitual6"):
                    st.session_state['current_page'] = "habitual6"
                    st.rerun()
            info("habitual5")     


        elif st.session_state.get('current_page') == "habitual6":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual5"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            habitual6 = habitual6.display()
            st.session_state['prevAnswer'] = habitual6
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual10_value", habitual10_value)
            if habitual6=="Less than 2 years": 
                if st.button("Next", key="next_result11"):
                    st.session_state['current_page'] = "result11"
                    st.rerun()
            elif habitual6=="2 years or more": 
                if st.button("Next", key="next_result10"):
                    st.session_state['current_page'] = "result10"
                    st.rerun()
            info("habitual6")    





        elif st.session_state.get('current_page') == "createPage6":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage5"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage6 = createPage6.display()
            st.session_state['prevAnswer'] = createPage6
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if createPage6=="None of the above applies to me": 
                if st.button("Next", key="next_createPage7"):
                    st.session_state['current_page'] = "createPage7"
                    st.rerun()
            else:
                if st.button("Next", key="next_publicFunds1"):
                    st.session_state['current_page'] = "publicFunds1"
                    st.rerun()
            info("createPage6")



        elif st.session_state.get('current_page') == "createPage7":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage6"#0
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            createPage7 = createPage7.display()
            st.session_state['prevAnswer'] = createPage7
            if verbose: st.write(st.session_state.get('prevAnswer'))
            if createPage7=="None of the above applies to me": 
                if st.button("Next", key="next_result16"):
                    st.session_state['current_page'] = "result16"
                    st.rerun()
            else:
                if st.button("Next", key="next_publicFunds2"):
                    st.session_state['current_page'] = "publicFunds2"
                    st.rerun()
            info("createPage7")



        elif st.session_state.get('current_page') == "publicFunds1":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage6"#0
                # st.session_state['current_page'] = "habitual4"#0todotodotodotodotodotodo
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            publicFunds1 = publicFunds1.display()
            st.session_state['prevAnswer'] = publicFunds1
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual10_value", habitual10_value)
            if publicFunds1=="Yes": 
                if st.button("Next", key="next_habitual5"):
                    st.session_state['current_page'] = "habitual5"
                    st.rerun()
            elif publicFunds1=="No": 
                if st.button("Next", key="next_result13"):
                    st.session_state['current_page'] = "result13"
                    st.rerun()
            info("publicFunds1")  




        elif st.session_state.get('current_page') == "publicFunds2":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "createPage7"#0
                # st.session_state['current_page'] = "habitual4"#0todotodotodotodotodotodo
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            publicFunds2 = publicFunds2.display()
            st.session_state['prevAnswer'] = publicFunds2
            if verbose: st.write(st.session_state.get('prevAnswer'))
            # if verbose: st.write("habitual10_value", habitual10_value)
            if publicFunds2=="Yes": 
                if st.button("Next", key="next_result15"):
                    st.session_state['current_page'] = "result15"
                    st.rerun()
            elif publicFunds2=="No": 
                if st.button("Next", key="next_result14"):
                    st.session_state['current_page'] = "result14"
                    st.rerun()
            info("publicFunds2")  





        elif st.session_state.get('current_page') == "result1":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual10"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result1")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()

        elif st.session_state.get('current_page') == "result2":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual10"
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result2")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()
        
        elif st.session_state.get('current_page') == "result3":#1:
            show("result3")
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual9"
                # st.session_state['current_page'] = "habitual1"tododododooddood
                # st.session_state['current_page'] = "habitual3"toododoododoodod
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')

            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()
        
        elif st.session_state.get('current_page') == "result4":#1:
            if st.button("Back", key="back_Q2"):
                st.session_state['current_page'] = "habitual2"
                # st.session_state['current_page'] = "exemption1"tododododooddood
                # st.session_state['current_page'] = "habitual4"toododoododoodod
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result4")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()
        
        elif st.session_state.get('current_page') == "result5":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "exemption1" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result5")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()

                
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result4")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()
        
        elif st.session_state.get('current_page') == "result5":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "exemption1" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result5")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()

                
        elif st.session_state.get('current_page') == "result6":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "commonwealth" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result6")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()
        
        elif st.session_state.get('current_page') == "result7":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "createPage4" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result7")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()

                
        elif st.session_state.get('current_page') == "result8":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "rejection1" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result8")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()    
                        
        elif st.session_state.get('current_page') == "result9":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "createPage3" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result9")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()
        
        elif st.session_state.get('current_page') == "result10":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "habitual6" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result10")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()
        
        elif st.session_state.get('current_page') == "result11":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "habitual6" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result11")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()
                        
        elif st.session_state.get('current_page') == "result12":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "habitual5" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result12")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()
                        
        elif st.session_state.get('current_page') == "result13":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "publicFunds1" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result13")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()
                        
        elif st.session_state.get('current_page') == "result14":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "publicFunds2" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result14")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()
                        
        elif st.session_state.get('current_page') == "result15":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "publicFunds2" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result15")
            if st.button("Create Sharecode", key="next_sharecode"):
                st.session_state['current_page'] = "sharecode"
                st.rerun()
                        
        elif st.session_state.get('current_page') == "result16":#1:
            if st.button("Back", key="back_Q2"): 
                st.session_state['current_page'] = "createPage7" 
                st.rerun()
            ChangeButtonColour('st-key-back_Q2', 'white', 'blue')
            show("result16")
            # if st.button("Create Sharecode", key="next_sharecode"):
            #     st.session_state['current_page'] = "sharecode"
            #     st.rerun()

    else:
        with content_container:
            # st.title("IRESHA Sharecode")
            # st.image("img/IRESHAlogo.png", width=200)
            # st.header("Immigration/Residence Status Eligibility for Social Housing Assistance - Sharecode")

            st.write("This app can be used to generate a sharecode indicating that you fulfil the minimum immigration/residence status eligibility requirements for social-housing assistance.")
            
            # st.subheader("For applicants")
            # st.write("To create a sharecode, you will be asked a series of questions to check if you have the minimum eligibility for social-housing assistance.")
            # st.write("There might be additional requirements based on where you live or where you want to apply for social housing.")
            
            # if st.button("Check eligibility and create sharecode"):
            #     st.session_state['button_clicked'] = True
            #     st.session_state['current_page'] = "createPage1"
            #     st.rerun()

            st.write("For applicants:")
            if st.button("Check eligibility and create sharecode", key="check_eligibility"):
                st.session_state['button_clicked'] = True
                st.session_state['current_page'] = "createPage0"
                st.rerun()
            ChangeButtonColour('st-key-check_eligibility', 'white', 'green')
            
            st.write("For housing officers or caseworkers:") 
            if st.button("Verify sharecode", key="verify_sharecode"):
                st.session_state['button_clicked'] = True
                st.session_state['current_page'] = "verifySharecode"
                st.rerun()
            ChangeButtonColour('st-key-verify_sharecode', 'white', 'green')
            st.image("img/partnerLogos.png", width=300)
            st.markdown("---")
            # st.image("img/partnerLogos.png", width=300)

            

        
if __name__ == "__main__":
    main()

