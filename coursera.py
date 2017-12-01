import requests
from lxml import etree
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_courses_url_list():
    url = 'https://www.coursera.org/sitemap~www~courses.xml'
    response = requests.get(url).content
    root = etree.fromstring(response)
    url_list = []
    for url in root.getchildren():
        for loc in url.getchildren():
            url_list.append(loc.text)
    return url_list[:20]


def get_course_info(courses_url_list):
    courses_list = []
    for courses_url in courses_url_list:
        url = '{}'.format(courses_url)
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")

        grade = getattr(soup.find(
            "div", class_="ratings-text"), 'text', '0 stars')
        course_name = getattr(soup.find(
            "h2", class_="course-name-text"), 'text', 'No data')
        startdate = getattr(soup.find(
            "div", class_="startdate"), 'text', 'No data')
        language = soup.find(
            "div", class_="rc-Language").findAllNext(text=True)[1]
        amount_week = len(soup.find_all(
            "div", class_="week-heading"))

        course = [course_name, grade, language, startdate, amount_week]
        courses_list.append(course)
    return courses_list


def output_courses_info_to_xlsx(filepath):
    dest_filename = 'courses_info.xlsx'
    wb = Workbook()
    sheet = wb.active
    name_column = (
        'Course name:',
        'Grade:',
        'Language:',
        'Start date:',
        'Amount week:'
    )
    sheet.append(name_column)
    for row in filepath:
        sheet.append(row)
    wb.save(filename=dest_filename)


if __name__ == '__main__':
    course_info = get_course_info(get_courses_url_list())
    output_courses_info_to_xlsx(course_info)
