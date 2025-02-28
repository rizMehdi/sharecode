import streamlit as st
import streamlit_survey as ss

def main():
    # Create a container to manage visibility of content
    content_container = st.container()
    
    if st.session_state.get('button_clicked', False):
        # Clear the previous content
        content_container.empty()
        
        # Initialize the survey
        survey = ss.StreamlitSurvey("IRESHA Sharecode")
        pages = survey.pages(9, on_submit=lambda: st.json(survey.to_json()))

        # Button customization
        pages.submit_button = pages.default_btn_submit("Generate Sharecode")
        pages.prev_button = pages.default_btn_previous("Back")
        pages.next_button = pages.default_btn_next("Next")

        with pages:
            if pages.current == 0:
                st.write("Are you any of the following?")
                selected_page0 = survey.radio(
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
                    

            if pages.current == 1:
                # selected_page0 == "British Citizen":
                location = survey.radio(
                    "Where do you currently live?",
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

            if pages.current == 2:
                # selected_page0 == "British Citizen":
                loc_duration = survey.radio(
                    "Since how long have you been residing in your current place of residence?",
                    options=[
                        "Less than 2 years",
                        "2 years or more"
                    ],
                    index=0,
                    label_visibility="collapsed",
                    horizontal=False,
                )
        
        # if st.button("Back"):
        #     st.session_state['button_clicked'] = False
        #     st.rerun()
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

