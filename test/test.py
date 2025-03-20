from requests import get, post, delete
from pprint import pprint

# пустой json
print(post('http://localhost:8080/api/jobs', json={}).json())
# незаполненный до конца json
print(post('http://localhost:8080/api/jobs',
           json={'job': 'Заголовок'}).json())
# неправильный столбец json
print(post('http://localhost:8080/api/jobs',
           json={'title': 'Заголовок'}).json())
print(post('http://localhost:8080/api/jobs',
           json={'job': 'job',
                 'work_size': 12,
                 'team_leader': 1,
                 'collaborators': '1,2',
                 'is_finished': False}).json())

print(delete('http://localhost:8080/api/jobs/999').json())
print(delete('http://localhost:8080/api/jobs/e').json())
print(delete('http://localhost:8080/api/jobs/1').json())

print(get('http://localhost:8080/api/jobs').json())
print(get('http://localhost:8080/api/jobs/1').json())
print(get('http://localhost:8080/api/jobs/999').json())
# новости с id = 999 нет в базе
print(get('http://localhost:8080/api/jobs/q').json())

