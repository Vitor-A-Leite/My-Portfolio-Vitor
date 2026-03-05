from .models import (
    Education as EducationModel,
    Experience as ExperienceModel,
    Languages as LanguagesModel,
    Profile as ProfileModel,
    Projects as ProjectsModel,
    Skills as SkillsModel,
    SoftSkills as SoftSkillsModel,
)


def _format_month_year(value):
    if not value:
        return None
    if hasattr(value, "strftime"):
        return value.strftime("%b %Y")
    return str(value)


def _split_text_list(value):
    if not value:
        return []

    cleaned = value.replace("\r", "\n")
    if "\n" in cleaned:
        raw_items = cleaned.split("\n")
    elif ";" in cleaned:
        raw_items = cleaned.split(";")
    else:
        raw_items = cleaned.split(",")

    return [item.strip(" -•\t") for item in raw_items if item.strip()]


def _split_csv(value):
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def get_profile_data():
    profile_instance = ProfileModel.objects.first()
    summary = profile_instance.summary if profile_instance else "Summary not available"
    email = profile_instance.email if profile_instance else "Email not available"
    college_email = profile_instance.college_email if profile_instance else "College email not available"
    phone = profile_instance.phone if profile_instance else "Phone not available"
    linkedin = profile_instance.linkedin if profile_instance else "LinkedIn not available"
    profile_picture = profile_instance.profile_picture.url if profile_instance and profile_instance.profile_picture else None

    return {
        "Summary": summary,
        "ProfilePicture": profile_picture,
        "Contact": {
            "Email": email,
            "College email": college_email,
            "Phone": phone,
            "LinkedIn": linkedin,
        },
    }


def get_education_data():
    return [
        {
            "Institution": education.institution,
            "Degree": education.degree,
            "Field": education.field,
            "Status": education.status,
            "StartYear": _format_month_year(education.start_year),
            "EndYear": _format_month_year(education.end_year),
        }
        for education in EducationModel.objects.all()
    ]


def get_experience_data():
    return [
        {
            "Company": experience.company,
            "Role": experience.role,
            "StartDate": experience.start_date.strftime("%Y-%m") if experience.start_date else None,
            "EndDate": experience.end_date.strftime("%Y-%m") if experience.end_date else "Present",
            "Responsibilities": _split_text_list(experience.responsibilities),
            "Tags": _split_csv(experience.tags),
        }
        for experience in ExperienceModel.objects.all()
    ]


def get_skills_data():
    return {
        "Technical": [
            {
                "Name": skill.name,
                "Description": skill.description,
            }
            for skill in SkillsModel.objects.all()
        ],
        "Languages": [
            {
                "Name": language.name,
                "Proficiency": language.proficiency,
            }
            for language in LanguagesModel.objects.all()
        ],
    }


def get_soft_skills_data():
    return [
        {
            "Name": soft_skill.name,
            "Description": soft_skill.description,
        }
        for soft_skill in SoftSkillsModel.objects.all()
    ]


def get_projects_data():
    return {
        f"Project {index}": {
            "Name": project.name,
            "Description": project.description,
            "Technologies": _split_csv(project.technologies),
            "Link": project.link,
            "Image": project.project_image.url if project.project_image else None,
        }
        for index, project in enumerate(ProjectsModel.objects.all(), start=1)
    }


def get_home_context():
    profile_data = get_profile_data()
    return {
        "skills": get_skills_data(),
        "Profile": profile_data,
        "Contact": profile_data["Contact"],
        "Education": get_education_data(),
        "Experience": get_experience_data(),
        "SoftSkills": get_soft_skills_data(),
        "Projects": get_projects_data(),
    }


def get_projects_context():
    profile_data = get_profile_data()
    return {
        "Projects": get_projects_data(),
        "Contact": profile_data["Contact"],
    }
