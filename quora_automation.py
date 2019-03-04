#all cats are yellow
from selenium import webdriver
from bs4 import BeautifulSoup
import time


#Quora Login Information
email=""
passy=""

# File With Questions Here
filey = ""

#Read File ,strip new lines ,return question list
def readFile(filey):
    with open(filey, "r") as f:
        q = f.readlines()
    qlist = [x.strip() for x in q]
    # qlist=reversed(qlist) #Will reverse the question list if needed
    print len(qlist), "Total Questions Loaded"
    return qlist

#Login to Quora
def login(email, passy):
    print "Logging in..."
    driver.get("http://quora.com")

    # Create Soup Object and find all form_column classes
    forms = BeautifulSoup(driver.page_source, "lxml").find_all(class_="form_column")

    # Iterate through forms
    # Find polymorphic id string,append a hashtag(#) to create css_selector
    for form in forms:
        try:
            # This is for email/password entry box
            data = form.find("input")["name"]
            if data == "email":
                email_css = "#" + form.find("input")["id"]
            if data == "password":
                password_css = "#" + form.find("input")["id"]
        except:
            pass

        try:
            # This is for the Login Button
            data = form.find("input")["value"]
            if data == "Login":
                button_css = "#" + form.find("input")["id"]
        except:
            pass

    driver.find_element_by_css_selector(email_css).send_keys(email)
    driver.find_element_by_css_selector(password_css).send_keys(passy)
    time.sleep(2)
    driver.find_element_by_css_selector(button_css).click()
    time.sleep(2)
    # LOGIN FINISHED


#Create Question List
qlist = readFile(filey)

#Create Webdriver Vroom Vroom
driver = webdriver.Chrome()

#Total Questions Posted Counter
county=0

# Iterate through qlist ask questions till no more
for question in qlist:
    try:
        print question
        driver.get("http://quora.com")
        soup=BeautifulSoup(driver.page_source,"lxml")

        # Find all text areas
        blox = soup.find_all("textarea")

        # Find polymorphic id string for Ask Question entry field
        for x in blox:
            try:
                placeholder = x["placeholder"]
                if placeholder.__contains__("Ask or Search Quora"): # Fix this later
                    askbar_css = "#" + x["id"]
                    print askbar_css
            except:
                pass


        askbutton = "#" + soup.find(class_="AskQuestionButton")["id"]# Fix this later

        # Type out Question
        driver.find_element_by_css_selector(askbar_css).send_keys(question)

        # Wait for askbutton to become clickable
        time.sleep(.2) # Fix later
        try:
            driver.find_element_by_css_selector(askbutton).click()
        except:
            #Click Failed # Fix later
            pass

        # Find the popup
        while True:
            try:
                soup = BeautifulSoup(driver.page_source, "lxml")
                popExists = soup.find(class_="Modal AskQuestionModal")
                break
            except:
                pass
        soup = BeautifulSoup(driver.page_source,"lxml")
        popup = "#" + soup.find(class_="submit_button modal_action")["id"]
        driver.find_element_by_css_selector(popup).click()

        for x in range(0,17):
            time.sleep(.1)
            try:
                soup = BeautifulSoup(driver.page_source, "lxml")
                popExists = soup.find(class_="PMsgContainer") #Found Popup

                if str(popExists).__contains__("You asked"): #big no no
                    county += 1
                    break
            except:
                pass
        print "county=>",county


    except Exception,e:
        print e
        print "ERROR"
        pass
