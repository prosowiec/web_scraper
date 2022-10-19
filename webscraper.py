import requests
from bs4 import BeautifulSoup
import regex as re
from collections import defaultdict
import os
import wget

description_check = []


def find_url_and_prettify_PL(ASIN):
  url = "https://www.amazon.pl/-/dp/{}".format(ASIN)
  agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
  r = requests.get(url, headers=agent)
  soup = BeautifulSoup(r.content, 'html.parser')
  soup.prettify()
  return soup


def find_url_and_prettify_DE(ASIN):
  url = "https://www.amazon.de/-/pl/dp/{}".format(ASIN)
  agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
  r = requests.get(url, headers=agent)
  soup = BeautifulSoup(r.content, 'html.parser')
  soup.prettify()
  return soup

''' #Still in progress
def find_url_and_prettify_FR(ASIN):
  url = "https://www.amazon.pl/-/dp/{}".format(ASIN)
  agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
  r = requests.get(url, headers=agent)
  soup = BeautifulSoup(r.content, 'html.parser')
  soup.prettify()
  return soup
'''

def scrap_description(soup):
  description = soup.find_all("p")
  description = str(description)
  description = re.findall(re.compile('(?<=<span>)(.*?)(?=<\/span>)'), description)
  final_description = ''

  for lines in description:
    description_check.append(lines)
    final_description = final_description + lines + '\n'
  
  return final_description

def scrap_tables(soup):
  s_table = soup.find_all("li")
  line_after_serach= ''

  tables = []
  final_front_page_table = ''

  for line in s_table:
    line = str(line)
    line = re.search('(?<=<li><span class="a-list-item">)(.*)(?=<\/span><\/li>)', line)
    if line is not None:
      line_after_serach = line.group(0)
      line_after_serach = line_after_serach.replace('<div</div>','')
      line_after_serach = line_after_serach.replace('<span class="a-size-base">','\n')
      line_after_serach = line_after_serach.replace('<span>','')
      line_after_serach = line_after_serach.replace('</span>','')
    if line_after_serach is not None and 'class="a-declarative"' not in  line_after_serach and '<div class' not in line_after_serach and "gwarancj"  not in line_after_serach.lower()  and "href"  not in line_after_serach.lower():
      if line_after_serach not in tables and line_after_serach not in description_check:
        tables.append(line_after_serach)
        final_front_page_table= final_front_page_table+ line_after_serach+ '\n'
  
  return final_front_page_table

def scrap_images(soup,ASIN):

  cwd = os.getcwd()
  parent_dir = f"{cwd}"

  try:
    directory = "images"
    mode = 0o666
    path = os.path.join(parent_dir, directory)
    os.mkdir(path, mode)
  except FileExistsError:
    pass
  
  soup = str(soup)
  image_list = re.findall(re.compile('(?<={"hiRes":")(.*?)(?=","thumb")'), soup)

  for image in image_list:
    print(image)

  directory = "images\\{}".format(ASIN)
  mode = 0o666
  path = os.path.join(parent_dir, directory)

  try:
    os.mkdir(path, mode)
  except FileExistsError:
    pass


  for image in image_list:
    image_filename = wget.download(image, out=path)

def tech_spec(soup):
  soup_find_names = soup.find_all("th", class_="a-color-secondary a-size-base prodDetSectionEntry")
  soup_find_values = soup.find_all("td", class_="a-size-base prodDetAttrValue")

  soup_find_names = str(soup_find_names)
  soup_find_names_list = re.findall(re.compile('(?<=<th class="a-color-secondary a-size-base prodDetSectionEntry">)(.*?)(?=<\/th>)'), soup_find_names)

  soup_find_values = str(soup_find_values)
  soup_find_values_list = re.findall(re.compile('(?<=<td class="a-size-base prodDetAttrValue">\n)(.*?)(?=<\/td>)'), soup_find_values)

  final_tech_spec=""
  for value in soup_find_values_list:
    value = str(value)
    value = value.replace("  ",'')

    name = str(soup_find_names_list.pop(0))
    name = name.replace("  ",'')

    text = "{}: {:>15}".format(name,value)
    final_tech_spec = final_tech_spec  +text +"\n"

  return(final_tech_spec)



def summing_everything_up_pl(soup_pl):
  text_ = "AMAZON PL ------------------- \n" "GŁÓWNY OPIS: \n"+ scrap_description(soup_pl) +"\n" + "DOLNY OPIS: \n" + scrap_tables(soup_pl) +"\n" \
    + "WŁAŚCIWOŚCI TECHNICZNE: \n"  +tech_spec(soup_pl) +"\n"
  return text_

def summing_everything_up_de(soup_de):
  text_ = "AMAZON DE ------------------- \n" + "GŁÓWNY OPIS: \n"+ scrap_description(soup_de) +"\n" + "DOLNY OPIS: \n" + scrap_tables(soup_de) +"\n" \
    + "WŁAŚCIWOŚCI TECHNICZNE: \n"  +tech_spec(soup_de) +"\n"
  return text_

if __name__ == '__main__':
  
  ASIN = ''
  soup_pl = find_url_and_prettify_PL(ASIN)
  final_description_PL = scrap_description(soup_pl)
  final_front_page_table_PL = scrap_tables(soup_pl)

  soup_de = find_url_and_prettify_DE(ASIN)
  final_description_PL_DE = scrap_description(soup_de)
  final_front_page_table_PL_DE = scrap_tables(soup_de)
  
  final_tech_spec = tech_spec(soup_pl)

  try:
    scrap_images(soup_pl)
  except FileExistsError:
    pass
  




