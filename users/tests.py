from django.test import TestCase
from django.test import Client


class EndpointTests(TestCase):
    ''' Testing the aut endpoints '''


    def test_user_creation(self):
        cli = Client()
        cli.login(username='ro', password='v123456V')
        body = {
        "username": "user2",
        "password" : "passwrd123",
        "email" : "user2@email.com"
        }        
        response_post = cli.post('/auth/users/',data=body, content_type='application/json')
        print(response_post.content)
        self.assertEqual(response_post.status_code, 201)
        cli.logout()


    def test_user_login(self):
        cli = Client()    
        user = {"username": "ro", "password" : "v123456V",}
        response_get = cli.post(path='/api-auth/login/', data=user )
        print(response_get.cookies)
        self.assertEqual(response_get.status_code, 200)

    # fails at the moment
    def test_user_fetching(self):
        cli = Client()    
        user = {"username": "ro", "password" : "v123456V",}
        response_get = cli.post(path='/api-auth/login/', data=user )
        self.assertEqual(response_get.status_code, 200)
        
   