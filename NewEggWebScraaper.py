
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"

# opening up connection to URL and grabbing the page data
uClient = uReq(my_url)
NewEgg_HTML = uClient.read()
uClient.close()

#HTML Parsing
page_soup = soup(NewEgg_HTML, "html.parser")

#parses page HTML
page_soup.h1
page_soup.p
page_soup.body.span

# grabs info from each product
containers = page_soup.findAll("div",{"class":"item-container"})

len(containers)
contain = containers[0]
container = containers[1]
#for container in containers:
#this wont work brand = container.div.div.a.img["title"]

'''brand_container = container.findAll("div",{"class":"title"})'''
filename = "products.xlsx"
f = open(filename,"w")

headers = "product_info, shipping\n"

f.write(headers)


#print(brand_container[0].div.a.img["title"])
for container in containers:
    # get title of product
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    
    # get shipping cost 
    product_shipping = container.findAll("li",{"class":"price-ship"})
    shipping = product_shipping[0].text.strip()
   
    
  
    print(str("product_name: " + product_name))
    print(str("shipping: " + shipping))
    f.write(product_name.replace(",","|") + "," + shipping + "\n")
f.close()
