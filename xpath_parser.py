import requests
from lxml import html

# Fetch the HTML content
url = "https://support.mozilla.org/en-US/questions/firefox?show=all"
response = requests.get(url)
tree = html.fromstring(response.content)
# Define XPaths
xpaths = {
    "get_help_box_xpath": ".//a[@class='mzp-c-menu-title sumo-nav--link'][text()='Get Help']",
    "search_box_input_xpath": ".//form[@id='support-search-sidebar']/input",
    "first_post_page_xpath": ".//article[@class='forum--question-item'][1]",
    "first_5_pages_xpath": ".//article[@class='forum--question-item'][position()<=5]",
    "time_of_publishing_first_post_xpath": ".//article[@class='forum--question-item'][1]//p[@class='user-meta-asked-by']/text()[contains(., 'ago')]",
    "posts_that_responded_xpath": ".//article[@class='forum--question-item' and .//li[contains(@class, 'thread-solved')]]",
    "one_day_ago_posts_xpath": ".//article[.//p[@class='user-meta-asked-by']/text()[contains(.,'1 day ago')]]",
    "posts_contain_question_marx_xpath": ".//article[.//h2[@class='forum--question-item-heading']/a[contains(text(),'?')]]",
    "posts_author_name_start_with_d_xpath": ".//article[.//p[@class='user-meta-asked-by' and (starts-with(translate(.//strong/a/text(),'d','D'), 'D') )]]",
    # "posts_with_more_than_tow_replies_xpath": ".//article[.//dl[@class='forum--meta-details replies']//span[@class='forum--meta-val']/text() > 2]",
    "posts_with_title_start_with_p_xpath": ".//article[.//h2[@class='forum--question-item-heading' and .//a[starts-with(translate(text(), 'p', 'P'), 'P')]]]",
    "posts_with_specific_title_length_xpath": ".//article[.//h2[@class='forum--question-item-heading' and .//a[string-length(text())>=14]]]",
    "posts_contain_Windows11_tag_xpath": ".//article[.//ul[@class='tag-list push-right']/li/a[text()='Windows 11']]",

}

# Function to apply XPath and return the number of elements founded
def count_elements(xpath):
    elements = tree.xpath(xpath)
    return len(elements)


# print the count of found elements for each xpath
for answer, xpath in xpaths.items():
    count = count_elements(xpath)
    print(f"{answer} ---> {count} elements found")
