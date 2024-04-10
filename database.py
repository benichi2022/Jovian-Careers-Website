from sqlalchemy import create_engine, text

engine = create_engine(
    "sqlite:////home/runner/Jovian-Careers-Website/jovian.db", echo=True)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    return result.all()
