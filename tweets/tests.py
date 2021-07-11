from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tweets.models import Comment, Like, Tweet

class TweetTests(APITestCase):
    def test_create_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
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
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.put(url, data, format='json')
        response_data = response.json()
        print("COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(Tweet.objects.count(), 1)
        # self.assertEqual(Tweet.objects.get().text, data['text'])
        # self.assertEqual(response_data['text'], data['text'])

class TweetTests(APITestCase):
    def test_patch_tweet(self):
        """
        Ensure we can create a new tweet object.
        """
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
        """
        Ensure we can create a new tweet object.
        """
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
        """
        Ensure we can create a new tweet object.
        """
        user = User.objects.create_user(username="seun", password="foran123")
        tweet = Tweet.objects.create(text="testing game ", user=user)

        url = reverse('tweet-list')
        # data = {'text': 'DabApps', "user": user.id} payload not needed for delete testcase
        response = self.client.delete(url, format='json')
        response_data = response.json()
        print("DONE")

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class RetweetTests(APITestCase):
#     def test_create_retweet(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="segun", password="forlan123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('retweet-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class LikeTests(APITestCase):
#     def test_create_like(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="segun", password="forlan123")
#         tweet = Tweet.objects.create(text="created tweet", user=user)

#         url = reverse('like-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class CommentTests(APITestCase):
#     def test_create_comment(self):
#         """
#         Ensure we can create a new retweet object.
#         """
#         user = User.objects.create_user(username="lloyds", password="forlan123")
#         tweet = Tweet.objects.create(text="this is a comment", user=user)

#         url = reverse('comment-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.post(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class TweetTests(APITestCase):
#     def test_patch_tweet(self):
#         """
#         Ensure we can DEL a new tweet object.
#         """
#         user = User.objects.create_user(username="segun", password="forlan123")
#         tweet =Tweet.objects.create(text="baba eleba",user=user)

#         url = reverse('tweet-detail',kwargs={"pk":tweet.id})
#         data = {'text': 'DabApps', "user": user.id}
#         response = self.client.patch(url, data, format='json')
#         response_data = response.json()
#         print()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(Tweet.objects.count(), 1)
#         # self.assertEqual(Tweet.objects.delete().text, data['text'])
#         # self.assertEqual(response_data['text'], data['text'])

# class RetweetTestsP(APITestCase):
#     def test_get_retweet(self):
#         """
#         Ensure we can GET a new retweet object.
#         """
#         user = User.objects.create_user(username="segun", password="forlan123")
#         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

#         url = reverse('retweet-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.get(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class LikeTestsP(APITestCase):
#     def test_get_like(self):
#         """
#         Ensure we can GET a new retweet object.
#         """
#         user = User.objects.create_user(username="segun", password="forlan123")
#         tweet = Tweet.objects.create(text="created tweet", user=user)

#         url = reverse('like-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.get(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class CommentTestsP(APITestCase):
#     def test_get_comment(self):
#         """
#         Ensure we can GET a new retweet object.
#         """
#         user = User.objects.create_user(username="lloyds", password="forlan123")
#         tweet = Tweet.objects.create(text="this is a comment", user=user)

#         url = reverse('comment-list')
#         data = {'tweet': tweet.id, "user": user.id}
#         response = self.client.get(url, data, format='json')
#         response_data = response.json()
#         print(response_data)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)

