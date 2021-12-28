#!/usr/bin/env python
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

frame = Tk()
frame.title("Color Kit Activation")
frame.geometry('600x200')

def activateKit():
    inp = inputtxt.get(1.0, "end-1c").split(" ")
    barcode, accession = inp[0], inp[1]

    strEmail = 'brentju@stanford.edu'
    pWord = 'Fzj3011825'

    driver = webdriver.Chrome()
    driver.get('https://home.color.com/sign-in?next=%2Fcovid%2Factivation')

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()

    email_form = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-id"]')))
    email_form.click()
    email_form.send_keys(strEmail)

    password_form = driver.find_element(By.XPATH, '//*[@id="password-id"]')
    password_form.click()
    password_form.send_keys(pWord)

    sign_in_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div/form/button')
    sign_in_button.click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select-participant"]/div/button'))).click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[1]/button[1]'))).click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[2]/div/div/div/a'))).click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/a'))).click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/button'))).click()
    cont = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/button')
    cont.click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="primaryConsentIsAccepted-id"]'))).click()
    list = ['//*[@id="additionalConsents[0]-id"]', '//*[@id="additionalConsents[1]-id"]']
    for xPath in list:
        check = driver.find_element(By.XPATH, xPath)
        check.click()
    cont = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/button')
    cont.click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/button'))).click()
    confirm = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]')
    confirm.click()

    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="CovidBarcodeField"]'))).click()
    bar = driver.find_element(By.XPATH, '//*[@id="CovidBarcodeField"]')
    bar.send_keys(barcode)
    access = driver.find_element(By.XPATH, '//*[@id="AccessionNumberField"]')
    access.click()
    access.send_keys(accession)
    cont = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/button').click()
    confirm = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]').click()

# TextBox Creation
inputtxt = Text(frame,
                   height = 5,
                   width = 20)

inputtxt.pack()

# Button Creation
printButton = Button(frame,
                        text = "Activate Kit",
                        command = activateKit)
printButton.pack()

# Label Creation
lbl = Label(frame, text="Enter the barcode followed by the accession code, separated by a space.")
lbl.pack()
frame.mainloop()

