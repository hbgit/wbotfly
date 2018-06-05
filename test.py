from splinter import Browser

# Define the username and password
username2 = '***'
password2 = '***'

# Choose the browser (default is Firefox)
browser2 = Browser()

# Fill in the url
browser2.visit('https://mijn.ing.nl/internetbankieren/SesamLoginServlet')

# Find the username form and fill it with the defined username
browser2.find_by_id('gebruikersnaam').first.find_by_tag('input').fill(username2)

# Find the password form and fill it with the defined password
browser2.find_by_id('wachtwoord').first.find_by_tag('input').fill(password2)

# Find the submit button and click
browser2.find_by_css('.submit').first.click()

# Print the current url
print(browser2.url)

# Print the current browser title
print(browser2.title)

# Print the current html source code
print(browser2.html)
