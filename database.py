from sqlalchemy import create_engine, text

engine = create_engine(
    "sqlite:////home/runner/Jovian-Careers-Website/jovian.db", echo=True)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    return result.all()


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    return rows

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience,resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    result = conn.execute(query,{
      "job_id": job_id,
      "full_name": data["full_name"],
      "email": data["email"],
      "linkedin_url": data["linkedin_url"],
      "education": data["education"],
      "work_experience": data["work_experience"],
      "resume_url": data["resume_url"]
    })