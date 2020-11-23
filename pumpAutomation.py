from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://192.168.0.33/')

def activateButton(url):
	button_element = driver.find_element_by_xpath('//a[@href="'+url+'"]')
	button_element.click()


def main():
	activateButton("sw?sw=on")
	time.sleep(8300)
	activateButton("sw?sw=off")

if __name__ == "__main__":
    main()