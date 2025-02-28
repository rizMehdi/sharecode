import streamlit as st
import streamlit_survey as ss

def main():
    # Initialize the survey
    survey = ss.StreamlitSurvey("Survey Example 2 - Advanced Usage")
    pages = survey.pages(2, on_submit=lambda: st.json(survey.to_json()))

    # Button customization
    pages.prev_button = pages.default_btn_previous("Back")
    pages.next_button = pages.default_btn_next("Next")

    with pages:
        if pages.current == 0:
            st.title("IRESHA Sharecode")
            st.header("Immigration/Residence Status Eligibility for Social Housing Assistance - Sharecode")

            st.write("This webapp can be used to generate a sharecode indicating that you fulfil the minimum immigration/residence status eligibility requirements for social-housing assistance.")
            
            st.subheader("For applicants")
            st.write("To create a sharecode, you will be asked a series of questions to check if you have the minimum eligibility for social-housing assistance.")
            st.write("There might be additional requirements based on where you live or where you want to apply for social housing.")
            
            if st.button("Check eligibility and create sharecode"):
                st.session_state['button_clicked'] = True
                st.rerun()
        if pages.current == 1:
            st.write("Are you any of the following?")
            selected_page0 = survey.radio(
                "used_st_before",
                options=[
                    "British Citizen",
                    "Irish Citizen",
                    "Commonwealth Citizen",
                    "Diplomat or their family member based in the UK",
                    "None of the above"
                ],
                index=0,
                label_visibility="collapsed",
                horizontal=False,
            )

            if selected_page0 == "British Citizen":
                location = survey.radio(
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
                st.write(f"You selected: {location}")

            st.write("This is the last question.")
            acknowledge = survey.checkbox("Acknowledge")
        
if __name__ == "__main__":
    main()

