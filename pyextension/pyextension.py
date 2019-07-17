import requests
from bs4 import BeautifulSoup
import argparse

__version__ = "1.0.3"


def prepare():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--ext", dest="extension",
                        help="Extension to get info about")
    args = parser.parse_args()
    return args


def getfileinfo_for_extension(extension):
    r = requests.get(f"https://fileinfo.com/extension/{extension}")
    soup = BeautifulSoup(r.text, 'lxml')
    ahrefs = soup.findAll("span", {"itemprop": "description"})
    for item in ahrefs:
        print(item.text)


def main():
    args = prepare()  # get arguments setup
    getfileinfo_for_extension(args.extension)  # get the extension info


if __name__ == "__main__":
    main()
