import urllib.request
import json
import time

rest_url = "https://api.tumblr.com/v2/blog/$BLOG_URL/posts/photo?api_key=$API_KEY&notes_info=false&reblog_info=" \
           "false&filter=raw&offset=$OFFSET&limit=50"
blog_url = ""
api_key = "fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4"
starting_offset = 0


def get_urls(url, offset):
    new_rest_url = rest_url.replace("$BLOG_URL", url).replace("$API_KEY", api_key)
    has_content = True
    urls = []

    while has_content:
        rest_response = urllib.request.urlopen(new_rest_url.replace("$OFFSET", offset.__str__()))
        print(new_rest_url.replace("$OFFSET", offset.__str__()))
        content = json.loads(rest_response.read())
        if content['meta']['status'] == 200:
            posts = content['response']['posts']
            total = content['response']['total_posts']
            print(total)
            if total > offset: #len(posts) != 0
                print(total > offset)
                time.sleep(300)
                for index in range(len(posts)):
                    photos = posts[index]['photos']
                    for photo_index in range(len(photos)):
                        print(posts[index]['date'] + ": " + photos[photo_index]['original_size']['url'])
                        urls.append(photos[photo_index]['original_size']['url'])
                offset += 50
            else:
                has_content = False
            time.sleep(1)
        else:
            print("error")
            time.sleep(5)

    return urls

# get_urls(new_rest_url, starting_offset)
