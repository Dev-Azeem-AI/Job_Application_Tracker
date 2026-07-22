import requests
from api import API_URL

# =====================================================
# AUTH
# =====================================================

def signup(username, email, password):
    data = {
        "username": username,
        "email": email,
        "password": password
    }

    return requests.post(
        f"{API_URL}/auth/signup",
        json=data
    )


def login(email, password):
    return requests.post(
        f"{API_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )


# =====================================================
# JOBS
# =====================================================

def get_jobs(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/jobs",
        headers=headers
    )


def add_job(token, company, position, status):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "company": company,
        "position": position,
        "status": status
    }

    return requests.post(
        f"{API_URL}/jobs",
        headers=headers,
        json=data
    )


def update_job(token, job_id, company, position, status):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "company": company,
        "position": position,
        "status": status
    }

    return requests.put(
        f"{API_URL}/jobs/{job_id}",
        headers=headers,
        json=data
    )


def delete_job(token, job_id):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/jobs/{job_id}",
        headers=headers
    )


# =====================================================
# COMPANIES
# =====================================================

def get_companies(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/companies",
        headers=headers
    )


def add_company(
    token,
    name,
    location,
    website,
    hr_name,
    hr_email,
    phone,
    priority,
    notes
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "name": name,
        "location": location,
        "website": website,
        "hr_name": hr_name,
        "hr_email": hr_email,
        "phone": phone,
        "priority": priority,
        "notes": notes
    }

    return requests.post(
        f"{API_URL}/companies",
        headers=headers,
        json=data
    )


def update_company(
    token,
    company_id,
    name,
    location,
    website,
    hr_name,
    hr_email,
    phone,
    priority,
    notes
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "name": name,
        "location": location,
        "website": website,
        "hr_name": hr_name,
        "hr_email": hr_email,
        "phone": phone,
        "priority": priority,
        "notes": notes
    }

    return requests.put(
        f"{API_URL}/companies/{company_id}",
        headers=headers,
        json=data
    )


def delete_company(token, company_id):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/companies/{company_id}",
        headers=headers
    )
    
# =====================================================
# RESUMES
# =====================================================

def get_resumes(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/resumes",
        headers=headers
    )


def add_resume(token, title, file_path, description):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "title": title,
        "file_path": file_path,
        "description": description
    }

    return requests.post(
        f"{API_URL}/resumes",
        headers=headers,
        json=data
    )


def update_resume(token, resume_id, title, file_path, description):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "title": title,
        "file_path": file_path,
        "description": description
    }

    return requests.put(
        f"{API_URL}/resumes/{resume_id}",
        headers=headers,
        json=data
    )


def delete_resume(token, resume_id):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/resumes/{resume_id}",
        headers=headers
    )
    
# =====================================================
# COVER LETTERS
# =====================================================

def get_cover_letters(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/cover-letters",
        headers=headers
    )


def add_cover_letter(token, title, content, company):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "title": title,
        "content": content,
        "company": company
    }

    return requests.post(
        f"{API_URL}/cover-letters",
        headers=headers,
        json=data
    )


def update_cover_letter(token, cover_letter_id, title, content, company):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "title": title,
        "content": content,
        "company": company
    }

    return requests.put(
        f"{API_URL}/cover-letters/{cover_letter_id}",
        headers=headers,
        json=data
    )


def delete_cover_letter(token, cover_letter_id):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/cover-letters/{cover_letter_id}",
        headers=headers
    )
    
# =====================================================
# INTERVIEWS
# =====================================================

def get_interviews(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/interviews",
        headers=headers
    )


def add_interview(
    token,
    company,
    position,
    interview_date,
    interview_time,
    round_name,
    status,
    notes
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "company": company,
        "position": position,
        "interview_date": str(interview_date),
        "interview_time": str(interview_time),
        "round": round_name,
        "status": status,
        "notes": notes
    }

    return requests.post(
        f"{API_URL}/interviews",
        headers=headers,
        json=data
    )


def update_interview(
    token,
    interview_id,
    company,
    position,
    interview_date,
    interview_time,
    round_name,
    status,
    notes
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "company": company,
        "position": position,
        "interview_date": str(interview_date),
        "interview_time": str(interview_time),
        "round": round_name,
        "status": status,
        "notes": notes
    }

    return requests.put(
        f"{API_URL}/interviews/{interview_id}",
        headers=headers,
        json=data
    )


def delete_interview(token, interview_id):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/interviews/{interview_id}",
        headers=headers
    )
def delete_interview(token, interview_id):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/interviews/{interview_id}",
        headers=headers
    )
# =====================================================
# NOTIFICATIONS
# =====================================================

def get_notifications(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.get(
        f"{API_URL}/notifications",
        headers=headers
    )


def add_notification(
    token,
    title,
    message
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "title": title,
        "message": message
    }

    return requests.post(
        f"{API_URL}/notifications",
        headers=headers,
        json=data
    )


def update_notification(
    token,
    notification_id
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.put(
        f"{API_URL}/notifications/{notification_id}",
        headers=headers
    )


def delete_notification(
    token,
    notification_id
):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    return requests.delete(
        f"{API_URL}/notifications/{notification_id}",
        headers=headers
    )