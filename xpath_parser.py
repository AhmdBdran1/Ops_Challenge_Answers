import requests
from lxml import html

# Fetch the HTML content
url = "https://support.mozilla.org/en-US/questions/firefox?show=all"
response = requests.get(url)
tree = html.fromstring(response.content)

# Define XPaths
xpaths = {
    "The box ‘Get Help’ from the top bar": ".//a[@class='mzp-c-menu-title sumo-nav--link'][text()='Get Help']",
    "The search box input on the top right of the page": ".//form[@id='support-search-sidebar']/input",
    "The first post on the page": ".//article[@class='forum--question-item'][1]",
    "The first 5 posts at the page": ".//article[@class='forum--question-item'][position()<=5]",
    "The time of publishing of the first post": ".//article[@class='forum--question-item'][1]//p[@class='user-meta-asked-by']/text()[contains(., 'ago')]",
    "all posts that are responded": ".//article[@class='forum--question-item' and .//li[contains(@class, 'thread-solved')]]",
    "all posts that are “1 day ago": ".//article[.//p[@class='user-meta-asked-by']/text()[contains(.,'1 day ago')]]",
    "All posts that '?' in the title": ".//article[.//h2[@class='forum--question-item-heading']/a[contains(text(),'?')]]",
    "All posts that their author name starts with D (D or d)": ".//article[.//p[@class='user-meta-asked-by' and (starts-with(translate(.//strong/a/text(),'d','D'), 'D') )]]",
    #"All posts that they have more then 2 replies": ".//article[.//dl[@class='forum--meta-details replies']//span[@class='forum--meta-val']/text() > 2]",
    "All posts that their title starts with ‘P’ (or p)": ".//article[.//h2[@class='forum--question-item-heading' and .//a[starts-with(translate(text(), 'p', 'P'), 'P')]]]",
    "All posts that their title length is 14 or bigger": ".//article[.//h2[@class='forum--question-item-heading' and .//a[string-length(text())>=14]]]",
    "All the posts that has “Windows 11” tag": ".//article[.//ul[@class='tag-list push-right']/li/a[text()='Windows 11']]",

}


# Function to apply XPath and return the number of elements founded
def count_elements(xpath):
    elements = tree.xpath(xpath)
    return len(elements)


# print the count of found elements for each xpath
for answer, xpath in xpaths.items():
    count = count_elements(xpath)
    print(f"{answer} ---> {count} elements found")
