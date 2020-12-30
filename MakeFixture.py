import requests, json

api_key = 'a9bd9cd14c809bdfc48543a946872d8b'
language = 'ko-KR'
URL = 'https://api.themoviedb.org/3/movie/popular'

params = {'api_key': api_key, 'language': language}
data = {'page' : 5}
result = []
pk = 1
for page in range(1,4):
    data['page'] = page
    res = requests.post(URL,params=params,data=data)
    # print('---')
    items = res.json()['results']
    for each in items:
        temp,fields = dict(),dict()
        temp['model'] = 'movies.movie'
        temp['pk'] = pk
        pk += 1
        fields['poster_path'] = each['poster_path']
        fields['title'] = each['title']
        fields['vote_average'] = each['vote_average']
        fields['overview'] = each['overview']
        fields['release_date'] = each['release_date']
        fields['movie_id'] = each['id']
        temp['fields'] = fields
        result.append(temp)

# print(result[0])
with open('movies.json', 'w', encoding='utf-8') as make_file:
    json.dump(result,make_file,ensure_ascii=False, indent = '\t')