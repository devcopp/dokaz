import time
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# def setup_driver():
#     driver = webdriver.Firefox()
#     driver.get('https://www.monitor.co.ug/')
#     return driver

# def get_classes():
#     pdf = FPDF()
#     pdf.add_page()
#     _driver = setup_driver()
#     unorderly_text = _driver.page_source
#     soup = BeautifulSoup(unorderly_text, 'html.parser')

#     # classes = set()
#     for text in soup.find_all(True):
#         if 'class' in text.attrs:

        # pdf.cell(200, 10, txt=element.text, ln=True)
    # pdf.output('webdata.pdf')

ex = """<a class="skip-link" href="#after-header">Skip to content</a>
<header class="header">
            <div class="header__content u--box"
             data-hide-width="1000">
            <div class='header__nav header__nav--left'>
                <button class="header__nav-toggle" title="Show navigation">
                    <svg class="icon">
                        <use xlink:href="#Icon--menu" />
                    </svg>
                </button>
                <ul id="menu-cta" class="header__menu u--box"><li id="menu-item-271412" class="menu-item menu-item-type-custom menu-item-object-custom has-text menu-item-271412"><a href="https://www.omgubuntu.co.uk/tip">Got News?<svg class='icon Icon--envelope'><use xlink:href='#Icon--envelope'></svg></a></li>
</ul>            </div>
            <a class="header__link" href="https://www.omgubuntu.co.uk/">
                <img width="248" height="60" class="header__logo" title="Go to the homepage" src="https://www.omgubuntu.co.uk/wp-content/themes/omgubuntu-theme-2024_04_0/images/logo.svg?v=20231008132257" alt="OMG! Ubuntu">            </a>
            <div class="header__nav">
                <ul id="menu-social" class="header__menu header__socials u--box"><li id="menu-item-237469" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-237469"><a target="_blank" href="https://bsky.app/profile/omgubuntu.co.uk"><svg class='icon Icon--bluesky'><use xlink:href='#Icon--bluesky'></svg></a></li>
<li id="menu-item-222240" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-222240"><a target="_blank" href="https://floss.social/@omgubuntu"><svg class='icon Icon--mastodon'><use xlink:href='#Icon--mastodon'></svg></a></li>
<li id="menu-item-131566" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-131566"><a target="_blank" href="https://twitter.com/omgubuntu"><svg class='icon Icon--twitter'><use xlink:href='#Icon--twitter'></svg></a></li>
<li id="menu-item-264093" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-264093"><a target="_blank" href="https://facebook.com/omgubuntu"><svg class='icon Icon--facebook'><use xlink:href='#Icon--facebook'></svg></a></li>
<li id="menu-item-131593" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-131593"><a target="_blank" href="https://omgubuntu.co.uk/feed"><svg class='icon Icon--feed'><use xlink:href='#Icon--feed'></svg></a></li>
</ul>"""


soup = BeautifulSoup(ex, 'html.parser')
soup = soup.find_all(True)
print(len(soup))

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

classes = set()
for tag in soup:
    if 'class' in tag.attrs:
        text = tag
        pdf.cell(200, 10, txt=tag, ln=True)
        pdf.output('webdata.pdf')
        print(tag.attrs['class'])
    # print(tag.attrs)
# def get_classes():
#     elements = driver.page_source
#     for element in elements:

# get_classes()

# elements = driver.find_elements(By.CLASS_NAME, 'politics')

# for element in elements:
    # print(len(element.text))

# time.sleep(5)   
# driver.quit()