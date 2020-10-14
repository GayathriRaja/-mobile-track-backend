# -mobile-track-backend
Steps:
1. Clone the repo
2. Create virtual environment
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

APIs:
1. http://127.0.0.1:8000/api/v1/register/ 
  POST: body: {username:"test", password:"pass@123", email:"test@gmail.com"}
  
2. http://127.0.0.1:8000/token/ 
  POST: body: {username:"test", password:"pass@123"}
  
3.http://127.0.0.1:8000/api/v1/categories/

4. http://127.0.0.1:8000/api/v1/services-list/

5. http://127.0.0.1:8000/api/v1/following-services/


Admin access:  http://127.0.0.1:8000/admin/
creds: username: admin, password: admin
