from bs4 import BeautifulSoup

html_doc = """
<html>
  <body>
    <h1>My Awesome Website</h1>
    <a href="/about-us.html" class="nav-link">About Us</a>
    <img src="/images/logo.png" alt="Company Logo" id="logo">
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# 1. Find the <a> tag
link_tag = soup.find('a')

# 2. Use .attrs to get its attributes
link_attributes = link_tag.attrs

# 3. Print the full dictionary of attributes
print(f"Link attributes: {link_attributes}")
print("-" * 20)

# 4. Access a specific attribute value
link_href = link_tag.attrs['href']
print(f"The 'href' value is: {link_href}")

print("-" * 20)

# 5. Find the <img> tag
img_tag = soup.find('img')

# 6. Access its attributes
img_src = img_tag.attrs['src']
img_alt = img_tag.attrs['alt']

print(f"The image source is: {img_src}")
print(f"The image alt text is: {img_alt}")