Amazon webscraper whole scrapes description, front page images and technical specs of a given product from two difrent amazon domains - polish and german. 
It' s main purpuse is to speed up proces of creating product despriptions in resale stores as outlets etc. Code can be implementet to various purposes like for cloecting data for machine learning ect.


<a href="https://drive.google.com/uc?export=view&id=1vd1_af9n1izTSyIFkO3_-bWZDnyWeAE_"><img src="https://drive.google.com/uc?export=view&id=1vd1_af9n1izTSyIFkO3_-bWZDnyWeAE_" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />


Program it's meant to be helper not executor. Polish text scrapted from Amazon mostly needs to be corected due to poor translation or wrong formating. 

I used Beautifulsoup4 to scrap data from website I added Regex expresions get rid of html language.

GUI was made by using QT-Designer and I have created simple functionality(with in interface) in pyqt5.

In order to get it working you must give it an ASIN number. It is critical that you copied it from amazon link for exaple:
   
    * in https://www.amazon.pl/-/dp/B09TRW5QTX ASIN number is B09TRW5QTX and that need to be an input to the program
   
    * https://www.amazon.pl/Bistro-11160-57EURO-4PL-elektryczny-mlynek-nierdzewna/dp/B07N23V6P1/.../ - ASIN = B07N23V6P1
   
    * https://www.amazon.pl/Led-Lenser-7495TP-LENSER-Stirnlampe/dp/B0018O9KVC/.../ ASIN = B07N23V6P1

   
Currently ASIN copied in diffrent way won't work!! I'm not shure why, but as pandemic thought as "it is what it is...". 

If you have right ASIN copy it to text edditor and press "ZNAJDŹ". 
After those steps you should be able to scroll content in text browser. Text has 3 diffrent indents that tell you wrom which part of the website are they from.
If you want to copy it press "KOPIUJ". 

By pressing "POBIERZ ZDJĘCIA" you download front page pictures from amazon. 
To acces them you need find images folder(in webscraper) and search given ASIN of the product.
Path to pictures dictionary should look something like this "C:\...\web_scraper\images\B0018O9KVC(PRODUCT ASIN)" , where images are saved in folder with 
ASIN name.

<a href="https://drive.google.com/uc?export=view&id=16DpMeTWn0sEH0EC_ACZGRioWdjAqoCTH"><img src="https://drive.google.com/uc?export=view&id=16DpMeTWn0sEH0EC_ACZGRioWdjAqoCTH" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />








