import requests

base_path = "https://graph.facebook.com"
token = "1825924290976649|f4a421b77888587f351418a5aa84762c"
page_ids = ['technologyreview']

for page_id in page_ids:


    feedRequestUrl = base_path + "/" + page_id + "/feed?access_token=" + token
    def do(url):
        r = requests.get(url)
        json_dict = r.json()
        print(json_dict['data'])
        if 'paging' in json_dict.keys():
            # do(url)

    do(feedRequestUrl)
