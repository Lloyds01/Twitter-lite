from django.contrib.auth.models import User
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tweets.models import Comment, Like, Tweet,Retweet

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

    def test_patch_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet =Tweet.objects.create(text="baba eleba",user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tweet.objects.count(), 1)
        self.assertEqual(Tweet.objects.delete().text, data['text'])
        self.assertEqual(response_data['text'], data['text'])

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


    def test_patch_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.patch(url, data, format='json')
        response_data = response.json()
        print(response_data,"COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_tweet(self):
        
        user = User.objects.create_user(username="segun", password="forlan123")
        tweet = Tweet.objects.create(text="azad testing game ", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'text': 'DabApps', "user": user.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data,"COMPLETE")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


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


    def test_get_retweet(self):

        user=User.objects.create_user(username='stan',password='wendy23')
        tweet = Tweet.objects.create(text='talking',user=user)

        url= reverse('retweet-list')
        data={'tweet':tweet.id,'user':user.id}
        response= self.client.get(url,data,format='json')
        response_data=response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_delete_retweet(self):

        user = User.objects.create_user(username='bala',password='thunder')
        tweet = Tweet.objects.create(text='testing microphone',user=user)

        url = reverse('retweet-list')
        data ={'tweet':tweet.id,'user':user.id}
        response=self.client.delete(url,data,)
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_one_retweet(self):

        user=User.objects.create_user(username='tunde',password='tesla')
        tweet=Tweet.objects.create(text="bingo come", user=user)
        retweet = Retweet.objects.create(user=user,tweet=tweet)

        url = reverse('retweet-detail',kwargs={'pk':retweet.id})
        data = {'tweet':tweet.id, 'user':user.id, 'retweet':retweet.id}
        response = self.client.get(url, data, format='json')
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        # self.assertEqual(response_data,tweet)

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


    def test_get_like(self):

        """test for getting"""
        user = User.objects.create_user(username="segun", password="bela")
        tweet = Tweet.objects.create(text="random",user=user)

        url = reverse("like-list")
        data ={'tweet':tweet.id, "user":user.id}
        response = self.client.get(url,data,format='json')
        print("done")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_patch_like(self):

        user = User.objects.create_user(username="bola",password="forlan")
        tweet = Tweet.objects.create(text="telcom", user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data = {'tweet':tweet.id,"user":user.id}
        response = self.client.patch(url,data,format='json')
        print('done')

        self.assertEqual(response.status_code, status.HTTP_200_OK)



    def test_delete_like(self):

        user = User.objects.create_user(username='best', password='lean')
        tweet = Tweet.objects.create(text='mango',user=user)

        url = reverse('tweet-detail',kwargs={"pk":tweet.id})
        data= {'tweet':tweet.id,'user':user.id}
        response = self.client.delete(url,data,format='json')
        print('complete')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_one_like(self):

        
        user = User.objects.create_user(username="segun", password="bela")
        tweet = Tweet.objects.create(text="random",user=user)
        like = Like.objects.create(tweet=tweet,user=user)


        url = reverse("like-detail",kwargs={'pk':like.id})
        data ={'tweet':tweet.id, "user":user.id,'like':like.id}
        response = self.client.get(url,data,format='json')
        response_data =response.json()
        print("done")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Like.objects.count(), 1)
        # self.assertEqual(response_data[0],tweet.id)



class CommentTests(APITestCase):
     def test_create_comment(self):
        
        user = User.objects.create_user(username="lloyds",password='tyu5')
        tweet = Tweet.objects.create(text='likers plate',user=user)

        url = reverse('comment-list')
        data={'tweet':tweet.id,'user':user.id}
        response = self.client.post(url, data,format='json')
        response_data = response.json()
        print(response_data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

     def test_patch_comment(self):
        
        user = User.objects.create_user(username='brian',password="talkers")
        tweet = Tweet.objects.create(text = "party animal",user=user)
        comment =Comment.objects.create(text = "counter", user=user, tweet=tweet)

        url = reverse('comment-detail',kwargs={"pk":comment.id})
        data= {'tweet':tweet.id,'user':user.id, 'text':comment.id}
        response = self.client.patch(url,data,)
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
      
     def test_get_comment(self):

        user= User.objects.create_user(username='follow', password='real')
        tweet= Tweet.objects.create(text='indiana girl', user=user)
        comment = Comment.objects.create(text='igconfig',tweet=tweet,user=user)

        url = reverse('comment-detail',kwargs={'pk':comment.id})
        response= self.client.get(url)
        response_data = response.json()
        print(response_data)
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)

     def test_put_comment(self):
        
        user = User.objects.create_user(username='brian',password="talkers")
        tweet = Tweet.objects.create(text = "party animal",user=user)
        comment =Comment.objects.create(text = "counter", user=user, tweet=tweet)

        url = reverse('comment-detail',kwargs={"pk":comment.id})
        data= {'tweet':tweet.id,'user':user.id, 'text':comment.id}
        response = self.client.put(url,data,)
        response_data = response.json()
        print(response_data)

        self.assertEqual(response.status_code,status.HTTP_200_OK)

     def test_delete_comment(self):
        
        user =User.objects.create_user(username='band', password= 'maine')
        tweet = Tweet.objects.create(text = 'complain args', user=user)
        comment = Comment.objects.create(text ="bakers are loving",tweet=tweet,user=user)

        url = reverse('comment-detail', kwargs={'pk':comment})
        data= {'tweet':tweet.id,'user':user.id, 'text':comment.id}
        response = self.client.delete(url,data)
        response_data = response.json()
        print(response_data, "love and light")

        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)


     def test_get_one_comment(self):

        user= User.objects.create_user(username='follow', password='real')
        tweet= Tweet.objects.create(text='indiana girl', user=user)
        comment = Comment.objects.create(text='igconfig',tweet=tweet,user=user)

        url = reverse('comment-detail',kwargs={'pk':comment.id})
        data= {'tweet':tweet.id,'user':user.id, 'text':comment.id}
        response= self.client.get(url,data)
        response_data = response.json()
        print(response_data)
        
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Comment.objects.count(), 1)
        # self.assertEqual(Comment.objects.get().text, data['text'])
        # self.assertEqual(response_data[0]['text'],comment.text)













"""# # # class TweetTests(APITestCase):
# # #     

# # # class RetweetTestsP(APITestCase):
# # #     def test_get_retweet(self):
        
# # #         user = User.objects.create_user(username="segun", password="forlan123")
# # #         tweet = Tweet.objects.create(text="this is a simple tweet", user=user)

# # #         url = reverse('retweet-list')
# # #         data = {'tweet': tweet.id, "user": user.id}
# # #         response = self.client.get(url, data, format='json')
# # #         response_data = response.json()
# # #         print(response_data)

# # #         self.assertEqual(response.status_code, status.HTTP_200_OK)

# # # class LikeTestsP(APITestCase):
# # #     def test_get_like(self):
        
# # #         user = User.objects.create_user(username="segun", password="forlan123")
# # #         tweet = Tweet.objects.create(text="created tweet", user=user)

# # #         url = reverse('like-list')
# # #         data = {'tweet': tweet.id, "user": user.id}
# # #         response = self.client.get(url, data, format='json')
# # #         response_data = response.json()
# # #         print(response_data)

# # #         self.assertEqual(response.status_code, status.HTTP_200_OK)"""