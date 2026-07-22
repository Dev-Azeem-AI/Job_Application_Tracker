import streamlit as st

from auth import (
    signup,
    login,
    get_jobs,
    add_job,
    update_job,
    delete_job,
    get_companies,
    add_company,
    update_company,
    delete_company,
    get_resumes,
    add_resume,
    update_resume,
    delete_resume,
    get_cover_letters,
    add_cover_letter,
    update_cover_letter,
    delete_cover_letter,
    get_interviews,
    add_interview,
    update_interview,
    delete_interview,
     get_notifications,
    add_notification,
    update_notification,
    delete_notification
)

st.set_page_config(
    page_title="Job Application Tracker",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Job Application Tracker")

# ---------------- LOGIN / SIGNUP ----------------

if "token" not in st.session_state:

    option = st.radio(
        "Choose Option",
        ["Login", "Signup"],
        horizontal=True
    )

    # ---------- LOGIN ----------

    if option == "Login":

        st.subheader("Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            response = login(email, password)

            if response.status_code == 200:

                st.session_state["token"] = response.json()["access_token"]

                st.success("Login Successful ✅")

                st.rerun()

            else:

                st.error(response.json()["detail"])

    # ---------- SIGNUP ----------

    else:

        st.subheader("Create Account")

        username = st.text_input("Username")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Signup"):

            response = signup(
                username,
                email,
                password
            )

            if response.status_code == 200:

                st.success("✅ Account Created Successfully")

                st.info("Now select Login and sign in.")

            else:

                try:
                    st.error(response.json()["detail"])
                except:
                    st.error("Signup Failed")
                    
# ---------------- DASHBOARD ----------------

else:

    st.success("Login Successful ✅")

    st.header("Dashboard")

    if st.button("🚪 Logout"):
        del st.session_state["token"]
        st.rerun()

    st.divider()

    # ---------------- JOB LIST ----------------

    st.subheader("My Jobs")

    response = get_jobs(st.session_state["token"])

    if response.status_code == 200:

        jobs = response.json()

        if len(jobs) == 0:
            st.info("No Jobs Found")
        else:
            st.dataframe(jobs, use_container_width=True)

    else:
        st.error("Unable to Fetch Jobs")

    st.divider()

    # ---------------- ADD JOB ----------------

    st.subheader("Add New Job")

    company = st.text_input("Company")

    position = st.text_input("Position")

    status = st.selectbox(
        "Status",
        ["Applied", "Interview", "Rejected", "Accepted"]
    )

    if st.button("Add Job"):

        response = add_job(
            st.session_state["token"],
            company,
            position,
            status
        )

        if response.status_code == 200:
            st.success("Job Added Successfully ✅")
            st.rerun()

        else:
            st.error("Unable to Add Job")

    st.divider()

    # ---------------- UPDATE JOB ----------------

    st.subheader("Update Job")

    update_id = st.number_input(
        "Job ID to Update",
        min_value=1,
        step=1,
        key="update_id"
    )

    new_company = st.text_input(
        "New Company",
        key="new_company"
    )

    new_position = st.text_input(
        "New Position",
        key="new_position"
    )

    new_status = st.selectbox(
        "New Status",
        ["Applied", "Interview", "Rejected", "Accepted"],
        key="new_status"
    )

    if st.button("Update Job"):

        response = update_job(
            st.session_state["token"],
            int(update_id),
            new_company,
            new_position,
            new_status
        )

        if response.status_code == 200:

            st.success("Job Updated Successfully ✅")
            st.rerun()

        else:

            st.error("Unable to Update Job")

    st.divider()

    # ---------------- DELETE JOB ----------------

    st.subheader("Delete Job")

    delete_id = st.number_input(
        "Job ID to Delete",
        min_value=1,
        step=1,
        key="delete_id"
    )

    if st.button("Delete Job"):

        response = delete_job(
            st.session_state["token"],
            int(delete_id)
        )

        if response.status_code == 200:

            st.success("Job Deleted Successfully ✅")
            st.rerun()

        else:

            st.error("Unable to Delete Job")
        
            st.divider()

    st.header("🏢 Companies")

    response = get_companies(
        st.session_state["token"]
    )

    if response.status_code == 200:

        companies = response.json()

        if len(companies) == 0:

            st.info("No Companies Found")

        else:

            st.dataframe(
                companies,
                use_container_width=True
            )

    else:

        st.error("Unable to Fetch Companies")
        
        st.divider()

    st.subheader("Add Company")

    company_name = st.text_input(
        "Company Name"
    )

    location = st.text_input(
        "Location"
    )

    website = st.text_input(
        "Website"
    )

    hr_name = st.text_input(
        "HR Name"
    )

    hr_email = st.text_input(
        "HR Email"
    )

    phone = st.text_input(
        "Phone"
    )

    priority = st.selectbox(
        "Priority",
        [
            "High",
            "Medium",
            "Low"
        ]
    )

    notes = st.text_area(
        "Notes"
    )

    if st.button("Add Company"):

        response = add_company(
            st.session_state["token"],
            company_name,
            location,
            website,
            hr_name,
            hr_email,
            phone,
            priority,
            notes
        )

        if response.status_code == 200:

            st.success(
                "Company Added Successfully ✅"
            )

            st.rerun()

        else:

            try:
                st.error(
                    response.json()["detail"]
                )
            except:
                st.error(response.text)
                
            st.divider()

    st.subheader("Update Company")

    company_id = st.number_input(
        "Company ID",
        min_value=1,
        step=1,
        key="company_update"
    )

    update_name = st.text_input(
        "Company Name",
        key="update_name"
    )

    update_location = st.text_input(
        "Location",
        key="update_location"
    )

    update_website = st.text_input(
        "Website",
        key="update_website"
    )

    update_hr_name = st.text_input(
        "HR Name",
        key="update_hr_name"
    )

    update_hr_email = st.text_input(
        "HR Email",
        key="update_hr_email"
    )

    update_phone = st.text_input(
        "Phone",
        key="update_phone"
    )

    update_priority = st.selectbox(
        "Priority",
        ["High", "Medium", "Low"],
        key="update_priority"
    )

    update_notes = st.text_area(
        "Notes",
        key="update_notes"
    )

    if st.button("Update Company"):

        response = update_company(
            st.session_state["token"],
            int(company_id),
            update_name,
            update_location,
            update_website,
            update_hr_name,
            update_hr_email,
            update_phone,
            update_priority,
            update_notes
        )

        if response.status_code == 200:

            st.success("Company Updated Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)
            st.divider()

    st.subheader("Delete Company")

    delete_company_id = st.number_input(
        "Company ID to Delete",
        min_value=1,
        step=1,
        key="delete_company_id"
    )

    if st.button("Delete Company"):

        response = delete_company(
            st.session_state["token"],
            int(delete_company_id)
        )

        if response.status_code == 200:

            st.success("Company Deleted Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)
                
                
            st.divider()

    # ===========================
    # RESUMES
    # ===========================

    st.header("📄 Resumes")

    response = get_resumes(
        st.session_state["token"]
    )

    if response.status_code == 200:

        resumes = response.json()

        if len(resumes) == 0:

            st.info("No Resume Found")

        else:

            st.dataframe(
                resumes,
                use_container_width=True
            )

    else:

        try:
            st.error(response.json()["detail"])
        except:
            st.error("Unable to Fetch Resumes")
            
        st.divider()

    # ===========================
    # ADD RESUME
    # ===========================

    st.subheader("Add Resume")

    resume_title = st.text_input(
        "Resume Title"
    )

    resume_file = st.text_input(
        "File Path"
    )

    resume_description = st.text_area(
        "Description"
    )

    if st.button("Add Resume"):

        response = add_resume(
            st.session_state["token"],
            resume_title,
            resume_file,
            resume_description
        )

        if response.status_code == 200:

            st.success(
                "Resume Added Successfully ✅"
            )

            st.rerun()

        else:

            try:
                st.error(
                    response.json()["detail"]
                )
            except:
                st.error(response.text)
                
            st.divider()

    # ===========================
    # UPDATE RESUME
    # ===========================

    st.subheader("Update Resume")

    resume_id = st.number_input(
        "Resume ID",
        min_value=1,
        step=1,
        key="resume_update_id"
    )

    update_title = st.text_input(
        "New Resume Title",
        key="resume_title_update"
    )

    update_file_path = st.text_input(
        "New File Path",
        key="resume_file_update"
    )

    update_description = st.text_area(
        "New Description",
        key="resume_description_update"
    )

    if st.button("Update Resume"):

        response = update_resume(
            st.session_state["token"],
            int(resume_id),
            update_title,
            update_file_path,
            update_description
        )

        if response.status_code == 200:

            st.success("Resume Updated Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)
            
            st.divider()

    # ===========================
    # DELETE RESUME
    # ===========================

    st.subheader("Delete Resume")

    delete_resume_id = st.number_input(
        "Resume ID to Delete",
        min_value=1,
        step=1,
        key="delete_resume_id"
    )

    if st.button("Delete Resume"):

        response = delete_resume(
            st.session_state["token"],
            int(delete_resume_id)
        )

        if response.status_code == 200:

            st.success("Resume Deleted Successfully ✅")

            st.rerun()
            
            

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)
            
                st.divider()

    # ===========================
    # COVER LETTERS
    # ===========================

    st.header("📝 Cover Letters")

    response = get_cover_letters(
        st.session_state["token"]
    )

    if response.status_code == 200:

        cover_letters = response.json()

        if len(cover_letters) == 0:

            st.info("No Cover Letters Found")

        else:

            st.dataframe(
                cover_letters,
                use_container_width=True
            )

    else:

        try:
            st.error(response.json()["detail"])
        except:
            st.error("Unable to Fetch Cover Letters")

    st.divider()

    # ===========================
    # ADD COVER LETTER
    # ===========================

    st.subheader("Add Cover Letter")

    cover_title = st.text_input(
        "Title",
        key="cover_title"
    )

    cover_company = st.text_input(
        "Company",
        key="cover_company"
    )

    cover_content = st.text_area(
        "Content",
        key="cover_content"
    )

    if st.button(
        "Add Cover Letter",
        key="add_cover_btn"
    ):

        response = add_cover_letter(
            st.session_state["token"],
            cover_title,
            cover_content,
            cover_company
        )

        if response.status_code == 200:

            st.success("Cover Letter Added Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)

    st.divider()

    # ===========================
    # UPDATE COVER LETTER
    # ===========================

    st.subheader("Update Cover Letter")

    update_cover_id = st.number_input(
        "Cover Letter ID",
        min_value=1,
        step=1,
        key="update_cover_id"
    )

    update_cover_title = st.text_input(
        "New Title",
        key="update_cover_title"
    )

    update_cover_company = st.text_input(
        "New Company",
        key="update_cover_company"
    )

    update_cover_content = st.text_area(
        "New Content",
        key="update_cover_content"
    )

    if st.button(
        "Update Cover Letter",
        key="update_cover_btn"
    ):

        response = update_cover_letter(
            st.session_state["token"],
            int(update_cover_id),
            update_cover_title,
            update_cover_content,
            update_cover_company
        )

        if response.status_code == 200:

            st.success("Cover Letter Updated Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)

        st.divider()

    # ===========================
    # DELETE COVER LETTER
    # ===========================

    st.subheader("Delete Cover Letter")

    delete_cover_id = st.number_input(
        "Cover Letter ID",
        min_value=1,
        step=1,
        key="delete_cover_id"
    )

    if st.button(
        "Delete Cover Letter",
        key="delete_cover_btn"
    ):

        response = delete_cover_letter(
            st.session_state["token"],
            int(delete_cover_id)
        )

        if response.status_code == 200:

            st.success("Cover Letter Deleted Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)            
                
        st.divider()

    # ===========================
    # INTERVIEWS
    # ===========================

    st.header("📅 Interviews")

    response = get_interviews(
        st.session_state["token"]
    )

    if response.status_code == 200:

        interviews = response.json()

        if len(interviews) == 0:

            st.info("No Interviews Found")

        else:

            st.dataframe(
                interviews,
                use_container_width=True
            )

    else:

        try:
            st.error(response.json()["detail"])
        except:
            st.error("Unable to Fetch Interviews")

    st.divider()

    # ===========================
    # ADD INTERVIEW
    # ===========================

    st.subheader("Add Interview")

    interview_company = st.text_input(
        "Company",
        key="interview_company"
    )

    interview_position = st.text_input(
        "Position",
        key="interview_position"
    )

    interview_date = st.date_input(
        "Interview Date",
        key="interview_date"
    )

    interview_time = st.time_input(
        "Interview Time",
        key="interview_time"
    )

    interview_round = st.text_input(
        "Round",
        key="interview_round"
    )

    interview_status = st.selectbox(
        "Status",
        [
            "Scheduled",
            "Completed",
            "Cancelled"
        ],
        key="interview_status"
    )

    interview_notes = st.text_area(
        "Notes",
        key="interview_notes"
    )

    if st.button(
        "Add Interview",
        key="add_interview_btn"
    ):

        response = add_interview(
            st.session_state["token"],
            interview_company,
            interview_position,
            interview_date,
            interview_time,
            interview_round,
            interview_status,
            interview_notes
        )

        if response.status_code == 200:

            st.success("Interview Added Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)

    st.divider()

    # ===========================
    # UPDATE INTERVIEW
    # ===========================

    st.subheader("Update Interview")

    update_interview_id = st.number_input(
        "Interview ID",
        min_value=1,
        step=1,
        key="update_interview_id"
    )

    update_company = st.text_input(
        "New Company",
        key="update_interview_company"
    )

    update_position = st.text_input(
        "New Position",
        key="update_interview_position"
    )

    update_date = st.date_input(
        "New Interview Date",
        key="update_interview_date"
    )

    update_time = st.time_input(
        "New Interview Time",
        key="update_interview_time"
    )

    update_round = st.text_input(
        "New Round",
        key="update_interview_round"
    )

    update_status = st.selectbox(
        "New Status",
        [
            "Scheduled",
            "Completed",
            "Cancelled"
        ],
        key="update_interview_status"
    )

    update_notes = st.text_area(
        "New Notes",
        key="update_interview_notes"
    )

    if st.button(
        "Update Interview",
        key="update_interview_btn"
    ):

        response = update_interview(
            st.session_state["token"],
            int(update_interview_id),
            update_company,
            update_position,
            update_date,
            update_time,
            update_round,
            update_status,
            update_notes
        )

        if response.status_code == 200:

            st.success("Interview Updated Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)

    st.divider()

    # ===========================
    # DELETE INTERVIEW
    # ===========================

    st.subheader("Delete Interview")

    delete_interview_id = st.number_input(
        "Interview ID to Delete",
        min_value=1,
        step=1,
        key="delete_interview_id"
    )

    if st.button(
        "Delete Interview",
        key="delete_interview_btn"
    ):

        response = delete_interview(
            st.session_state["token"],
            int(delete_interview_id)
        )

        if response.status_code == 200:

            st.success("Interview Deleted Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)
                
            st.divider()

    # ===========================
    # NOTIFICATIONS
    # ===========================

    st.header("🔔 Notifications")

    response = get_notifications(
        st.session_state["token"]
    )

    if response.status_code == 200:

        notifications = response.json()

        if len(notifications) == 0:

            st.info("No Notifications Found")

        else:

            st.dataframe(
                notifications,
                use_container_width=True
            )

    else:

        try:
            st.error(response.json()["detail"])
        except:
            st.error("Unable to Fetch Notifications")

    st.divider()

    # ===========================
    # ADD NOTIFICATION
    # ===========================

    st.subheader("Add Notification")

    notification_title = st.text_input(
        "Title",
        key="notification_title"
    )

    notification_message = st.text_area(
        "Message",
        key="notification_message"
    )

    if st.button(
        "Add Notification",
        key="add_notification_btn"
    ):

        response = add_notification(
            st.session_state["token"],
            notification_title,
            notification_message
        )

        if response.status_code == 200:

            st.success("Notification Added Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)

    st.divider()

    # ===========================
    # MARK NOTIFICATION AS READ
    # ===========================

    st.subheader("Mark Notification as Read")

    notification_read_id = st.number_input(
        "Notification ID",
        min_value=1,
        step=1,
        key="notification_read_id"
    )

    if st.button(
        "Mark as Read",
        key="mark_notification_btn"
    ):

        response = update_notification(
            st.session_state["token"],
            int(notification_read_id)
        )

        if response.status_code == 200:

            st.success("Notification Marked as Read ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)

    st.divider()

    # ===========================
    # DELETE NOTIFICATION
    # ===========================

    st.subheader("Delete Notification")

    delete_notification_id = st.number_input(
        "Notification ID",
        min_value=1,
        step=1,
        key="delete_notification_id"
    )

    if st.button(
        "Delete Notification",
        key="delete_notification_btn"
    ):

        response = delete_notification(
            st.session_state["token"],
            int(delete_notification_id)
        )

        if response.status_code == 200:

            st.success("Notification Deleted Successfully ✅")

            st.rerun()

        else:

            try:
                st.error(response.json()["detail"])
            except:
                st.error(response.text)