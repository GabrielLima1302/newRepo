import requests #used to open URL in python
import lxml.html #

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

#->
"""we take [0] (the first element) bcz we know that only one div on the page has this ID"""

#->
"""the // tell lxml that we want to search for all tags in the HTML document which match our requirements/filters"""

#->
""" 'div' tells lxml that we are searching for div tags in the HTML page"""


#->
"""[@id="tab_releases_content"] tells lxml that we are only interested in
 those divs which have an id of tab_releases_content
"""

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')

#->
""" this gives us the titles of all of the games in the "Popular New Releases"""

#->
""" the game's titles are in a div with a class of "tab_item_name" """

#->
""" . tells lxml that we are only interested in the tags which are the children of the "new_releases" tag"""

#->
"""@class="tab_item_name"] pretty similar to the filter that we made before,
 but here we are filtering based on the class name
"""
#->
"""/text() tells lxml that we want the text contained within the tag we just extracted.
 In this case it returns the tittle contained in the div with the tab_item_name class name
"""

prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')
prices_original = new_releases.xpath('.//div[@class="discount_original_price"]/text()')

tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags=[]

for div in tags_divs:
    tags.append(div.text_content()) #

#->
"""
.text_content() returns the text contained within and HTML tag without the HTML markup
"""

tags = [tag.split(', ') for tag in tags] #separate the tags from each game

platform_div = new_releases.xpath('.//div[@class="tab_item_details"]')
# Extracting the "tab_item_details" div

total_platforms = []

for game in platform_div:

    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    # "[contains(@class, "platform_img")]" return the content which have the "platform_img" class
    # it doesn't matter whether it is the only class or if there are more classes associated with that tag


    platforms = [t.get('class').split(' ')[-1] for t in temp]

    # get() extract an attribute of the classes, example of an attribute: "platform_img win"
    # so we split the string based on the whitespace, and then we store the last part, example: "win"

    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')

    #we are removing "hmd_separator" from the list if it exists
    #"hmd_separator" is just a vertical separator bar used to separate actual platforms from VR/AR hardware

    total_platforms.append(platforms)

output = []

for info in zip(titles, prices, tags, total_platforms):

    resp = {}

    resp['title'] = info[0]

    resp['price'] = info[1]

    resp['tag'] = info[2]

    resp['platforms'] = info[3]

    output.append(resp)

for each in range (len(output)):
    for i in ['title','price','tag','platforms']:
        print(i,": ",output[each][i])
    print('='*30)























































