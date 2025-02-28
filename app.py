import streamlit as st
import streamlit.components.v1 as components

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

def main():
    # Create a container to manage visibility of content
    content_container = st.container()
    
    # Set text size
    text_size = "16px"
    
    if st.session_state.get('button_clicked', False):
        # Clear the previous content
        content_container.empty()
        
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
            q1 = st.radio(
                "used_st_before",
                options=[
                    "British Citizen",
                    "Irish Citizen",
                    "Commonwealth Citizen (?)",
                    "Diplomat or their family member based in the UK",
                    "None of the above"
                ],
                index=0,
                # label_visibility="collapsed",
                horizontal=False,
            )
            if st.button("Next", key="next_0"):
                st.session_state['current_page'] = 1
                st.rerun()
        
        elif st.session_state.get('current_page', 0) == 1:
            q2 = st.radio(
                "current_location",
                options=[
                    "UK",
                    "Republic of Ireland",
                    "Isle of Man",
                    "Channel Islands",
                    "None of the Above"
                ],
                index=0,
                # label_visibility="collapsed",
                horizontal=False,
            )
            col1, col2 = st.columns([1, 2])
            with col1:
                if st.button("Back", key="back_1"):
                    st.session_state['current_page'] = 0
                    st.rerun()
                ChangeButtonColour('st-key-back_1', 'white', 'blue')
            with col2:
                if st.button("Next", key="next_1"):
                    st.session_state['current_page'] = 2
                    st.rerun()
        
        elif st.session_state.get('current_page', 0) == 2:
            q3 = st.radio(
                "residence_duration",
                options=[
                    "Less than 2 years",
                    "2 years or more"
                ],
                index=0,
                # label_visibility="collapsed",
                horizontal=False,
            )
            col1, col2, pad = st.columns([1, 1, 2])
            with col1:
                if st.button("Back", key="back_2"):
                    st.session_state['current_page'] = 1
                    st.rerun()
                ChangeButtonColour('st-key-back_2', 'white', 'blue')
            with col2:
                if st.button("Generate Sharecode", key="submit"):
                    st.json({
                        "used_st_before": q1,
                        "current_location": q2,
                        "residence_duration": q3
                    })
        
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

