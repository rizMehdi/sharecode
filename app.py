import streamlit as st
from streamlit_custom_notification_box import custom_notification_box

def main():
    # Create a container to manage visibility of content
    content_container = st.container()
    
    with content_container:
        st.title("IRESHA Sharecode")
        st.header("Immigration/Residence Status Eligibility for Social Housing Assistance - Sharecode")

        st.write("This webapp can be used to generate a sharecode indicating that you fulfil the minimum immigration/residence status eligibility requirements for social-housing assistance.")
        
        st.subheader("For applicants")
        st.write("To create a sharecode, you will be asked a series of questions to check if you have the minimum eligibility for social-housing assistance.")
        st.write("There might be additional requirements based on where you live or where you want to apply for social housing.")
        
        if st.markdown("[?](#)"):
            styles = {'material-icons':{'color': 'black'},
                      'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'},
                      'notification-text': {'':''},
                      'close-button':{'':''},
                      'link':{'':''}}
            
            custom_notification_box(icon='info', textDisplay='We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
    
    if st.button("Check eligibility and create sharecode"):
        # Clear the previous content
        content_container.empty()
        
        # Add the eligibility check content
        option = st.radio("Are you any of the following?", [
            "British Citizen",
            "Irish Citizen",
            "Commonwealth Citizen",
            "Diplomat or their family member based in the UK",
            "None of the above"
        ])
        
        st.write(f"You selected: {option}")
        
if __name__ == "__main__":
    main()

