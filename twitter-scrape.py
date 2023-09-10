import csv
from playwright.sync_api import sync_playwright
import snscrape.modules.twitter  as sntwitter
import json
import codecs
import re
from datetime import datetime




# this for hashtag of scrape library 
query = ['#العالم_يحترم_مصر']
Links = []
# ua = user_agent('chrome')
# search_hash = input("what do you want to search? ")


# with sync_playwright() as p:

#     browser = p.chromium.launch()

#     page = browser.new_page()

#     page.goto('https://twitter.com/', wait_until="domcontentloaded")


#     page.locator('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-tv6buo > div.css-1dbjc4n.r-1777fci.r-1qmwkkh.r-nsbfu8 > div > div.css-1dbjc4n > div.css-1dbjc4n.r-2o02ov > a > div').click()
#     username = page.locator('[name=text]')
#     username.fill('username', force=True)
#     page.keyboard.down('Enter')
#     page.keyboard.up('Enter')
#     password = page.locator('[name="password"]')
#     password.fill('password')
#     page.keyboard.down('Enter')
#     page.keyboard.up('Enter')
#     search = page.locator("input[placeholder='Search Twitter']")
#     search.fill("")
#     search.fill(search_hash)
#     page.wait_for_timeout(3000)
#     hashtag = page.query_selector('//div[@role="listbox"]')
#     hashtagList = hashtag.query_selector_all('//div[@role="option"]')
#     hashtagItem = []
#     for i in hashtagList:
#         hashtagItem.append(i.inner_text())

#     for i in hashtagItem:
#         if (re.match('^#', i)):
#             query.append(i.split('/')[0])
#             if '/' in i :
#                 query.append(re.split('\\', i)[0])  
#         else:
#             if len(query) == 0:
#                 query.append(search_hash)

#     browser.close()


# End playwright

#  functions


# fatch link and edit txt

def fetch_and_edit(tweetTxt):
    global withPhoto
    link = re.search("https://t.co/[a-zA-Z0-9]*$", tweetTxt)
    if link:
        link = link.group(0)
        Links.append(link)
        withPhoto = True
        return tweetTxt.replace(link, '')
    else:
        withPhoto = False
        return tweetTxt





def edit_source(sre):
    return re.split( '>' , sre, maxsplit=1)[1].split('<')[0]

limit = 10
tweets = []
json_opje = []
correlation = []
userId = []
tweetId = []
# search in profile 
profile_det = []

print(len(query))
# circle = limit / len(query)



for hasht in query:
    print(hasht)
    i = 0
    # if len(tweetId) >= limit:
    #     break
  

    
    for tweet in sntwitter.TwitterSearchScraper(hasht).get_items():

        # if i >= round(circle):
        #     break

        # if len(tweetId) >= limit:
        #     break

        i += 1
        tweetId.append(tweet.id)
        userId.append(tweet.user.id)

        data = [hasht, tweet.user.username, fetch_and_edit(tweet.content), str(withPhoto),tweet.id,tweet.url,
        edit_source(tweet.source),str(tweet.date),tweet.replyCount,tweet.retweetCount,tweet.retweetCount,
        tweet.likeCount,tweet.lang,str(datetime.now())]

        json_opje.append(data)

## json file

        # subject =  {hasht : {
        # "Username": tweet.user.username,
        # "Content": fetch_and_edit(tweet.content),
        # "Has Photo": str(withPhoto),
        # "Id of tweet": tweet.id,
        # "Url of tweet": tweet.url,
        # "Source": edit_source(tweet.source),
        # "Date": str(tweet.date),
        # "Count of replies": tweet.replyCount, 
        # "Count of retweet": tweet.retweetCount,
        # "Count of quote tweet": tweet.retweetCount,
        # "Count of likes": tweet.likeCount,
        # "Language of tweet": tweet.lang,
        # "Time of scrape":str(datetime.now())   
        # }}

        # json_opje.append(subject)

        data1 = [tweet.user.username, tweet.user.displayname, tweet.user.id, tweet.user.description,tweet.user.descriptionUrls,
        tweet.user.verified,str(tweet.user.created),tweet.user.followersCount,tweet.user.friendsCount,tweet.user.statusesCount, tweet.user.mediaCount,
        tweet.user.favouritesCount,tweet.user.listedCount,tweet.user.location,tweet.user.protected,tweet.user.linkUrl,str(datetime.now())]

        profile_det.append(data1)

        # search in profile 
        # Profile = {  tweet.user.username : {
        # "profile name": tweet.user.displayname,
        # "Id of user": tweet.user.id,
        # "description": tweet.user.description,
        # "description urls": tweet.user.descriptionUrls,
        # "verified": tweet.user.verified,
        # "created": str(tweet.user.created), 
        # "Count of followers": tweet.user.followersCount,
        # "Count of following": tweet.user.friendsCount,
        # "Count of status": tweet.user.statusesCount,
        # "Count of list": tweet.user.listedCount,
        # "Count of media": tweet.user.mediaCount,
        # "Count of favourites": tweet.user.favouritesCount,
        # "Location":tweet.user.location,
        # "Private":tweet.user.protected,
        # "Linkurl of profile":tweet.user.linkUrl,
        # "Time of scrape":str(datetime.now()),   
        # }}
        # profile_det.append(Profile)

for num in range(0, len(userId)):
    if len(userId) == len(tweetId):
        correlation.append([
        userId[num],tweetId[num]
        ])

header = ['Hashtag', 'Username', 'Content', 'Has Photo','Id of tweet', 'Url of tweet', 'Source',
    'Date','Count of replies', 'Count of retweet', 'Count of quote tweet', 'Count of likes',
    'Language of tweet','Time of scrape']

with codecs.open('hash/subject.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(json_opje)
    f.close()


header1 = ['Username', 'profile name','Id of user', 'description', 'description urls','verified', 'created', 'Count of followers',
    'Count of following','Count of status', 'Count of media', 'Count of favourites', 'Count of list',
    'Location','Private', 'Linkurl of profile', 'Time of scrape']

with codecs.open('hash/profile.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header1)
    writer.writerows(profile_det)
    f.close()
# try:
#     with codecs.open('json/subject.json', 'w', "utf-8") as f:
#         f.write(json.dumps(json_opje, ensure_ascii=False))
# except:
#     print(json_opje)



# with codecs.open('json/profile.json', 'w', "utf-8") as f:
#     f.write(json.dumps(profile_det, ensure_ascii=False))




with codecs.open('hash/correlation.csv', 'w', "utf-8") as File:
    csvwriter  = csv.writer(File)
    csvwriter.writerow(('User ID', 'Tweet ID')) 
    csvwriter.writerows(correlation)
    File.close()

# # loop for preprossing data 
    
# for link in Links:

#     if link :
#         while True:
#         try:
#             element = page.locator('//div[@data-testid="tweetPhoto"]')
#             break
#         except:
#             element = page.locator('//div[@data-testid="videoPlayer"]')

#         if element
        
#     else:
#         print(False)

        







            




        




