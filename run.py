# -*- coding: utf-8 -*-

import time
import database
import requests
from bs4 import BeautifulSoup
import playsound
import datetime
import configparser

config = configparser.ConfigParser()


def home():
    while True:
        config.read("config.ini")
        sql = """SELECT * FROM search"""
        results = database.select(sql)
        datetime_now = datetime.datetime.now().strftime("%H:%M:%S")
        print("\n======== {} ========\n".format(datetime_now))
        for result in results:
            parse(result)
        time.sleep(int(config["DEFAULT"]["cooldown_scraping"]))


def parse(result):
    if result[1] == "Pole-Emploi":
        ep(result)
    elif result[1] == "Linkedin":
        lk(result)
    elif result[1] == "Leboncoin":
        lb(result)
    else:
        print("Error")


def ep(result):
    req = requests.get(result[3])
    soup = BeautifulSoup(req.content, "html.parser")
    ads = soup.find_all('li', class_="result")
    conn = database.connection()
    for ad in ads:
        link = "{}{}".format(result[4], ad.a['href'])
        title = ad.h2.text.replace("\n", "")
        location = ad.find('p', class_="subtext").text.replace("\n", "")
        description = ad.find('p', class_="description").text
        sql = """INSERT INTO ad (site_id, title, description, location, link) VALUES ({}, "{}", "{}", "{}", "{}")"""\
            .format(result[0], title, description, location, link)
        injection_sql(conn, sql, link, title, location, description, result)
    close(conn)


def lk(result):
    req = requests.get(result[3])
    soup = BeautifulSoup(req.content, "html.parser")
    ads = soup.find_all('li', class_="result-card")
    conn = database.connection()
    for ad in ads:
        link = ad.a['href'].split("?")[0]
        title = ad.h3.text
        location = ad.find('span', class_="job-result-card__location").text
        sql = """INSERT INTO ad (site_id, title, location, link) VALUES ({}, "{}", "{}", "{}")"""\
            .format(result[0], title, location, link)
        injection_sql(conn, sql, link, title, location, None, result)
    close(conn)


def injection_sql(conn, sql, link, title, location, description, result):
    try:
        data = conn.cursor()
        data.execute(sql)
        playsound.playsound("sound/alert.mp3", False)
        print("\n----- {} / {} -----".format(result[1], result[2]))
        print("Lien : {}\nTitre : {}\nLieu : {}\nDescription : {}".format(link, title, location, description))
        print("----------------------------")
        time.sleep(int(config["DEFAULT"]["cooldown_ad"]))
    except conn.IntegrityError:
        pass
    except conn.Error as e:
        print(e)


def close(conn):
    try:
        conn.commit()
        conn.close()
    except conn.Error as e:
        print(e)