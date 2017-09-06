import urllib
import json
import time


def get_urls(url, offset):
    has_content = True
    while has_content:

        rest_response = urllib.urlopen(url.replace("$OFFSET", offset.__str__()))
        content = json.loads(rest_response.read())
        if content['meta']['status'] == 200:
            posts = content['response']['posts']
            if len(posts) != 0:
                for index in range(len(posts)):
                    photos = posts[index]['photos']
                    for photo_index in range(len(photos)):
                        print posts[index]['date'] + ": " + photos[photo_index]['original_size']['url']
                offset += 20
            else:
                has_content = False
        else:
            print "error"
            time.sleep(5)


rest_url = "https://api.tumblr.com/v2/blog/$BLOG_URL/posts/photo?api_key=$API_KEY&notes_info=false&reblog_info=false&filter=raw&offset=$OFFSET"

blog_url = ""
api_key = "fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4"
starting_offset = 0

new_rest_url = rest_url.replace("$BLOG_URL", blog_url).replace("$API_KEY", api_key)

get_urls(new_rest_url, starting_offset)
