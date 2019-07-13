- Activate virtualenvironment (python 3)
- pip install -r requirements.txt
- ./manage.py migrate
- ./manage.py runserver

- API endpoint for providers
http://localhost:8000/api/providers/provider/

GET - Paginated response for all providers
POST - Create a provider

```
curl -X POST \
  http://localhost:8000/api/providers/provider/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -H 'postman-token: 6bd08cd1-b9aa-6199-08a9-0b886d7ab641' \
  -F name=dhruv \
  -F email=dhruvsingh.er@gmail.com \
  -F currency=test \
  -F language=english
```
