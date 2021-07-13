from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tweets.models import Comment, Like, Tweet

class TweetTests(APITestCase):
    def test_create_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")

        url = reverse('tweet-list')
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

class TweetTests(APITestCase):
    def test_put_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.put(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.get().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

class TweetTests(APITestCase):
    def test_patch_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TweetTests(APITestCase):
    def test_get_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TweetTests(APITestCase):
    def test_delete_tweet(self):
        
        user = User.objects.create_user(username="seun", password="foran123")
        tweet = Tweet.objects.create(text="testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.delete(url,data,format='json')
        print('done')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class RetweetTests(APITestCase):
    def test_create_retweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RetweetTests(APITestCase):
    def test_put_retweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="this i a", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.put(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class RetweetTests(APITestCase):
    def test_patch_retweet(self):
        user =User.objects.create_user(username='bala',password='murder12')
        tweet = Tweet.objects.create(text='melanin poping',user=user)

        url= reverse('tweet-list')
        data = {'tweet':tweet.id, 'user':user.id}
        response = self.client.patch(url,data,format='json')
        response_data=response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class RetweetTests(APITestCase):
     def test_get_retweet(self):

        user=User.objects.create_user(username='stan',password='wendy23')
        tweet = Tweet.objects.create(text='talking',user=user)

        url= reverse('tweet-list')
        data={'tweet':tweet.id,'user':user.id}
        response= self.client.get(url,data,format='json')
        response_data=response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

class RetweetTests(APITestCase):
     def test_delete_retweet(self):

        user = User.objects.create_user(username='bala',password='thunder')
        tweet = Tweet.objects.create(text='testing microphone',user=user)

        url = reverse('tweet-list')
        data ={'tweet':tweet.id,'user':user.id}
        response=self.client.delete(url,data,)
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)



class LikeTests(APITestCase):
    def test_create_like(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="created tweet", user=user)

        url = reverse('like-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LikeTest(APITestCase):
    def test_get_like(self):

        """test for getting"""
        user = User.objects.create_user(username="segun", password="bela")
        tweet = Tweet.objects.create(text="random",user=user)

        url = reverse("like-list")
        data ={'tweet':tweet.id, "user":user.id}
        response = self.client.get(url,data,format='json')
        print("done")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LikeTest(APITestCase):
    def test_patch_like(self):

        user = User.objects.create_user(username="bola",password="forlan")
        tweet = Tweet.objects.create(text="telcom", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'tweet':tweet.id,"user":user.id}
        response = self.client.patch(url,data,format='json')
        print('done')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LikeTest(APITestCase):
    def test_put_like(self):
        
        user = User.objects.create_user(username='brian',password='fox')
        tweet = Tweet.objects.create(text='py.mongo', user=user)

        url = reverse('tweet-list')
        data = {'tweet':tweet.id,'user':user.id}
        response = self.client.put(url,data,format='json')
        print('done')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LikeTest(APITestCase):
    def test_delete_like(self):

        user = User.objects.create_user(username='best', password='lean')
        tweet = Tweet.objects.create(text='mango',user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data= {'tweet':tweet.id,'user':user.id}
        response = self.client.delete(url,data,format='json')
        print('complete')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CommentTests(APITestCase):
    def test_create_comment(self):
        
        user = User.objects.create_user(username="lloyds", password="forlan123")
        tweet = Tweet.objects.create(text="this is a comment", user=user)

        url = reverse('comment-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.post(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TweetTests(APITestCase):
    def test_patch_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet =Tweet.objects.create(text="baba eleba",user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(Tweet.objects.count(), 1)
        # self.assertEqual(Tweet.objects.delete().text, data['text'])
        # self.assertEqual(response_data['text'], data['text'])

class RetweetTestsP(APITestCase):
    def test_get_retweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

        url = reverse('retweet-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LikeTestsP(APITestCase):
    def test_get_like(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="created tweet", user=user)

        url = reverse('like-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CommentTests(APITestCase):
    def test_get_comment(self):
        
        user = User.objects.create_user(username="lloyds", password="forlan123")
        tweet = Tweet.objects.create(text="this is a comment", user=user)

        url = reverse('comment-list')
        data = {'tweet': tweet.id, "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

# class CommentTests(APITestCase):
#      def test_create_comment(self):
        
#         user = User.objects.create_user(usernsme='lloyds',password='tyu5')
#         tweet = Tweet.objects.create(text='likers plate',user=user)

#         url = reverse('tweet-list')
#         data={'tweet':tweet.id,'user':user.id}
#         response = self.client.post(url, data,format='json')
#         response_data = response.json()
#         print(response_data)

      
