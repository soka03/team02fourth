from django.shortcuts import render

# Create your views here.






import requests
from .models import Movie
from member.models import Actor
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def init_db(request):
    url = "https://port-0-minihackathon-12-lyec0qpi97716ac6.sel5.cloudtype.app/movie"
    res = requests.get(url)
    movies = res.json()['movies']

    flag=True
    for movie in movies:
        data={}
        for i in movie:
            if i=='actors':
                data['actors']=movie[i]

            elif i=='title_kor':
                data['title_kor']=movie[i]
            elif i=='title_eng':
                data['title_eng']=movie[i]
            elif i=='poster_url':
                data['poster_url']=movie[i]

            elif i=='genre':
                data['genre']=movie[i]
            elif i=='showtime':
                data['showtime']=movie[i]
            elif i=='release_date':
                data['release_date']=movie[i]
            elif i=='plot':
                data['plot']=movie[i]
            elif i=='rating':
                data['rating']=movie[i]
            elif i=='director_name':
                data['director_name']=movie[i]
            elif i=='director_image_url':
                data['director_image_url']=movie[i]


        serializer=MovieSerializer(data=data)
        if serializer.is_valid():
            post=serializer.save()



            # [{'name': '에런 엑하트', 'character': 'Adam', 'image_url': 'https://image.tmdb.org/t/p/original/6rI3cYhdxOaOFSRB4C29MalpwDC.jpg'}, 
            # {'name': '이본 스트러호브스키', 'character': 'Terra', 'image_url': 'https://image.tmdb.org/t/p/original/giUmbTd2Kw5BSWHHSFLgVjJqIGl.jpg'}, 
            # {'name': '빌 나이', 'character': 'Naberius', 'image_url': 'https://image.tmdb.org/t/p/original/ixFI2YCGNGJfwlpI8iyhvVZRg8C.jpg'}, 
            # {'name': 'Jai Courtney', 'character': 'Gideon', 'image_url': 'https://image.tmdb.org/t/p/original/6vEaNwbOKov6yzQx15CdtrqfK3L.jpg'}, 
            # {'name': '미란다 오토', 'character': 'Leonore', 'image_url': 'https://image.tmdb.org/t/p/original/szME1IBVTLgiKrO5D5wvOGnvUDW.jpg'}, 
            # {'name': 'Caitlin Stasey', 'character': 'Keziah', 'image_url': 'https://image.tmdb.org/t/p/original/xbSKSiUtPKiUcRZyFXD8rIxhT4a.jpg'}, 
            # {'name': 'Penny Higgs', 'character': 'Sargon', 'image_url': 'https://image.tmdb.org/t/p/original/lqnB5JH7f2lH1mJm1mqZwXlrRyo.jpg'}, 
            # {'name': 'Aden Young', 'character': 'Dr. Frankenstein', 'image_url': 'https://image.tmdb.org/t/p/original/y7YoyvmNEJWZZP4UiDzPhz4zaPP.jpg'}]


            for actor in data['actors']:
                # {'name': '에런 엑하트', 'character': 'Adam', 'image_url': 'https://image.tmdb.org/t/p/original/6rI3cYhdxOaOFSRB4C29MalpwDC.jpg'}
                # for j in actor:
                #     if j=='name':
                #         print('name')
                secondserializer=ActorSerializer(data=actor)
                # secondserializer=ActorSerializer(data=actor)

                if secondserializer.is_valid():
                    secondserializer.save(movies=post)

            
            # response=MovieSerializer(post)
    return Response(serializer.data,status=status.HTTP_201_CREATED)
# return Response(status=status.HTTP_400_BAD_REQUEST)
            

'''

    # for i in movie:
actors
title_kor
title_eng
poster_url
genre
showtime
release_date
plot
rating
director_name
director_image_url


'''


'''
    
    # movie
{'actors': 
[{'name': '에런 엑하트', 'character': 'Adam', 'image_url': 'https://image.tmdb.org/t/p/original/6rI3cYhdxOaOFSRB4C29MalpwDC.jpg'}, 
{'name': '이본 스트러호브스키', 'character': 'Terra', 'image_url': 'https://image.tmdb.org/t/p/original/giUmbTd2Kw5BSWHHSFLgVjJqIGl.jpg'}, 
{'name': '빌 나이', 'character': 'Naberius', 'image_url': 'https://image.tmdb.org/t/p/original/ixFI2YCGNGJfwlpI8iyhvVZRg8C.jpg'}, 
{'name': 'Jai Courtney', 'character': 'Gideon', 'image_url': 'https://image.tmdb.org/t/p/original/6vEaNwbOKov6yzQx15CdtrqfK3L.jpg'}, 
{'name': '미란다 오토', 'character': 'Leonore', 'image_url': 'https://image.tmdb.org/t/p/original/szME1IBVTLgiKrO5D5wvOGnvUDW.jpg'}, 
{'name': 'Caitlin Stasey', 'character': 'Keziah', 'image_url': 'https://image.tmdb.org/t/p/original/xbSKSiUtPKiUcRZyFXD8rIxhT4a.jpg'}, 
{'name': 'Penny Higgs', 'character': 'Sargon', 'image_url': 'https://image.tmdb.org/t/p/original/lqnB5JH7f2lH1mJm1mqZwXlrRyo.jpg'}, 
{'name': 'Aden Young', 'character': 'Dr. Frankenstein', 'image_url': 'https://image.tmdb.org/t/p/original/y7YoyvmNEJWZZP4UiDzPhz4zaPP.jpg'}], 
'title_kor': '프랑 
켄슈타인: 불멸의 영웅', 'title_eng': 'I, Frankenstein', 'poster_url': 'https://image.tmdb.org/t/p/original/uilDKaZb81a6L1gG8XJ4M4XNfVu.jpg', 'genre': '공포, 스릴러', 'showtime': '92', 'release_date': '2014-01-22', 'plot': '인간세계를 두고 200년간 계속된 ‘가고 
일’(선)과 ‘데몬’(악)의 전쟁. 인간이 창조해낸 ‘아담’(프랑켄슈타인)을 통해 영생을 얻고 인간세계를 파괴하려는 ‘데몬’의 무차별한 공격 
은 더욱 거세지고, ‘아담’은 자신의 목숨을 위협하는 ‘데몬’에게 반격
을 가하며 그들을 하나씩 처단한다. 더욱 치열해진 전쟁, 인간세계를 
지키려는 ‘가고일’은 ‘아담’과 함께 ‘데몬’ 군단을 없애려 하지만 ‘아
담’의 비밀이 담긴 연구일지가 ‘데몬’의 손에 넘어가면서 더 큰 위기 
가 닥치게 된다. 이를 막으려는 ‘아담’은 홀로 ‘데몬’ 군단의 근거지 
로 침입하고, 최후의 결전을 치르던 중 자신의 거대한 비밀과 강력한 
힘을 깨닫게 되는데…', 'rating': '5.356', 'director_name': 'Stuart Beattie', 'director_image_url': 'https://image.tmdb.org/t/p/original/mgR1jZAECtmvQ67iuZixlI3xFn6.jpg'}
    
    

'''






'''
    
    if i=='actors':
        print(movie[i])
    
    [{'name': 'Son Woo-hyuk', 'character': 'Cheol-i (철이)', 'image_url': 'https://image.tmdb.org/t/p/original/xjGgFPos4A4pUTDLxjidVmqc1us.jpg'}, 
    {'name': 'Jeong Yoo-jin', 'character': 'Ae-ri (애리)', 'image_url': 'https://image.tmdb.org/t/p/original/hHTEJDmariFtfJHtENZVRyXAFvm.jpg'}, 
    {'name': 'Shin Yu-ju', 'character': 'Shin-yeong (신영)', 'image_url': 'https://image.tmdb.org/t/p/original/ez3GVJXwLQ9PJxG1TbsrhMetqiM.jpg'}, {'name': 'Jeon Hyeon-soo', 'character': 'Tae-seong (태성)', 'image_url': 'https://image.tmdb.org/t/p/original/lZpFuEwTjIdNoV7sg6ZG7vWFqxU.jpg'}, {'name': 'Baek In-Kwon', 'character': 'Joon-ho (준호)', 'image_url': 'https://image.tmdb.org/t/p/original/ezUDswvslf45EE5hf2bzFEOy2e1.jpg'}, {'name': 'Kim Dae-hyeon', 'character': 'Min-gi  (민기)', 'image_url': 
'https://image.tmdb.org/t/p/original/f4aK4YxVyzJnOYfTXevLF6PGZrW.jpg'}, {'name': 'Joo In-cheol', 'character': 'Jeong-soo (정수)', 
'image_url': 'https://image.tmdb.org/t/p/original/goM2kiw6kRjao3EAzBEhiG0z1Qa.jpg'}, {'name': 'Kim Soo-yeon', 'character': 'Hwa-seon (화선)', 'image_url': 'https://image.tmdb.org/t/p/original/hTNXwRYSwhj5r7AqnRHEuulPNOj.jpg'}]



'''


# [{'name': '야마자키 켄토', 'character': 'Saichi Sugimoto', 'image_url': 'https://image.tmdb.org/t/p/original/nUWXgjDfRxFJ3P20lyMJr8qDIJ0.jpg'}, 
#  {'name': 'Anna Yamada', 'character': 'Asirpa', 'image_url': 'https://image.tmdb.org/t/p/original/2cCWdsCpZbG67HJ96QdI9VVvh0G.jpg'}, 
#  {'name': 'Gordon Maeda', 'character': 'Hyakunosuke Ogata', 'image_url': 'https://image.tmdb.org/t/p/original/qy7Ucl1zXXAvjxKxbFloGK06eEt.jpg'}, 
#  {'name': 'Yuma Yamoto', 'character': 'Yoshitake Shiraishi', 'image_url': 'https://image.tmdb.org/t/p/original/c777kEmb9D7jhY2TdhjsELSQcTT.jpg'}, 
#  {'name': '오타니 료 헤이', 'character': 'Genjiro Tanigaki', 'image_url': 'https://image.tmdb.org/t/p/original/2Nn3Dlnc6I6kvI5HT5yWP7tz1O2.jpg'}, 
#  {'name': 'Shuntaro Yanagi', 'character': 'Yohei / Kohei Nikaido', 'image_url': 'https://image.tmdb.org/t/p/original/z9sPHsSAxpKFt0s4QyTdLepT3qB.jpg'}, 
#  {'name': 'Katsuya', 'character': 'Tatsuma Ushiyama', 'image_url': 'https://image.tmdb.org/t/p/original/109uhWtQoevcJahrXCshEo5Xs7o.jpg'}, 
#  {'name': '木場勝己', 'character': 'Shinpachi Nagakura', 'image_url': 'https://image.tmdb.org/t/p/original/jXeuuLA2fcFhHPXCVhMCpz1e7PX.jpg'}]




'''


{'actors': 
[{'name': '에이미 폴러', 'character': 'Joy (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/rwmvRonpluV6dCPiQissYrchvSD.jpg'}, 
{'name': '마야 호크', 'character': 'Anxiety (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/zv9RlbPcG5Xle1LUp0Q7vyHrPK2.jpg'}, 
{'name': 'Kensington Tallman', 'character': 'Riley (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/tBqawwg2VJq1V4mZjAOFQ7fnXNW.jpg'}, 
{'name': 'Liza Lapira', 'character': 'Disgust (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/o3jvQAGWtxi5rEycslhC6CY8BWX.jpg'}, 
{'name': '필리스 스미스', 'character': 'Sadness (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/h9w9pQbiderRWAC2mi7spjzuIGz.jpg'}, 
{'name': 'Lewis Black', 'character': 'Anger (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/1Yvp5dwnJ1UI0KtXGNhZ384wTgv.jpg'}, 
{'name': '토니 헤일', 'character': 'Fear (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/ar4uapp4w5wMkThZcqWUNMSTO8z.jpg'}, 
{'name': '아요 에데비리', 'character': 'Envy (voice)', 'image_url': 'https://image.tmdb.org/t/p/original/V9TNVjNkAJIiCHLTzcnHLktnPf.jpg'}], 

'title_kor': '인사이드 아웃 2', 
'title_eng': 'Inside Out 2', 
'poster_url': 'https://image.tmdb.org/t/p/original/pmemGuhr450DK8GiTT44mgwWCP7.jpg', 
'genre': '애니메이션, 가족, 모험, 코미디, 드라마', 
'showtime': '97', 
'release_date': '2024-06-11', 
'plot': '13살이 된 라일리의 행복을 위해 매일 바쁘게 
머릿속 감정 컨트롤 본부를 운영하는 ‘기쁨’, ‘슬픔’, ‘버럭’, ‘까칠’, ‘소심’. 그러던 어느 날, 낯선 감정인 ‘불안’, ‘당황’, ‘따분’, ‘부
럽’이가 본부에 등장하고, 언제나 최악의 상황을 대비하며 제멋대로인
 ‘불안’이와 기존 감정들은 계속 충돌한다. 결국 새로운 감정들에 의 
해 본부에서 쫓겨나게 된 기존 감정들은 다시 본부로 돌아가기 위해  
위험천만한 모험을 시작하는데…', 
'rating': '7.731', 'director_name': 'Kelsey Mann', 'director_image_url': 'https://image.tmdb.org/t/p/original/fK0QGrUmIPmQdyVXY3aFFafFMC0.jpg'}




'''








