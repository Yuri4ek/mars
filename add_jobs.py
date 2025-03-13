from data import db_session
from data.jobs import Jobs

db_session.global_init("db/blogs.db")

job = Jobs()
job.team_leader = 1
job.job = "123"
job.work_size = 12
job.collaborators = '1, 2'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job.team_leader = 2
job.job = "1234"
job.work_size = 10
job.collaborators = '1, 2'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

db_sess = db_session.create_session()
jobs = db_sess.query(Jobs).all()

for job in jobs:
    print(job)