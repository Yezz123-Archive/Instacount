# Instagram Automatic Account Creator Bot

- This small piece of code will create an account automatically by randomizing names. You need Selenium library installed. This is an ongoing work. Beware that Instagram has security measures to prevent bot usage. Do not forget to change the Web driver you use from the part of the code:

- first install the Requirements :

```sh
$ pip install -r requirements.txt
```

- Then install the [WebDriver for Chrome](https://chromedriver.chromium.org/).
- then, Start by putting the path for you webDriver, you can change it if you use Firefox.

```Python
browser = webdriver.Chrome("your chrome driver path here")
```

```Python
#Another browser
browser = webdriver.Firefox("your firefox driver path here")
```
