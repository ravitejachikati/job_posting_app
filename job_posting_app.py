import streamlit as st


if 'page' not in st.session_state:
    st.session_state.page = "Post"

if 'jobs' not in st.session_state:
    st.session_state.jobs = []

st.set_page_config(page_title="Job Posting App", layout="wide")


def switch_page(page_name):
    st.session_state.page = page_name


col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Post a Job"):
        switch_page("Post")
with col2:
    if st.button("View Jobs"):
        switch_page("View")

st.title("Job Posting Webpage")


if st.session_state.page == "Post":
    st.header("Post a New Job")
    with st.form("job_form"):
        title = st.text_input("**Job Title**")
        company = st.text_input("**Company Name**")
        location = st.text_input("**Location**")
        salary = st.text_input("**Salary**")
        description = st.text_area("**Job Description**")
        submit = st.form_submit_button("Post Job")
    
    if submit and title and company:
        st.session_state.jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Salary": salary,
            "Description": description
        })
        st.success("Job posted successfully!")


elif st.session_state.page == "View":
    st.header("Job Listings")

    if st.session_state.jobs:
        for idx, job in enumerate(st.session_state.jobs):
            with st.container():
                st.markdown(
                    f'''
                    <div style="border-radius: 10px; background-color: #2b2b2b; padding: 15px; margin-bottom: 15px;
                                box-shadow: 2px 2px 10px rgba(255,255,255,0.1); color: white;">
                        <h3 style="color:#FFA500;">{job["Title"]}</h3>
                        <p><strong>Organization {job["Company"]}</strong> -  {job["Location"]}</p>
                        <p><strong> Salary:</strong> ${job["Salary"]}</p>
                        <p>{job["Description"]}</p>
                    </div>
                    ''', unsafe_allow_html=True
                )
                
                

    else:
        st.info("No jobs posted yet.")
