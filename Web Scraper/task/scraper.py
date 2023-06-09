import requests
import string
import os

from bs4 import BeautifulSoup


def get_number_pages() -> int:
    return int(input())


def get_type_article() -> str:
    return input()


def get_text(url: str, article_type: str) -> dict:
    result = dict()

    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(response.content, "html.parser")

    article_list = soup.find_all('article')

    for article in article_list:
        if article.find('span', {'class': 'c-meta__type'}, text=article_type):
            title = article.find("a").contents[0]
            link = article.find("a")["href"]
            result[f"{link}"] = title.strip()

    return result


def treat_title(articles_list: dict):
    for k, v in articles_list.items():
        for sign in string.punctuation:
            if sign in v:
                x = v.replace(sign, " ")
                v = x.strip()
        word_list = v.split(" ")
        v = "_".join(word_list)
        articles_list[k] = v


def save_content(articles_list: dict) -> list:
    saved_articles = []
    for link, title in articles_list.items():
        response = requests.get("https://nature.com" + link, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(response.content, "html.parser")

        body = soup.find("p", {"class": "article__teaser"}).text.strip()

        filename = f"{title}.txt"
        with open(filename, "wb") as fh:
            fh.write(body.encode("utf-8"))
            fh.close()
        saved_articles.append(filename)

    return saved_articles


def change_directory(new_dir):
    base_cwd = os.getcwd()
    new_path = os.path.join(base_cwd, new_dir)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    os.chdir(new_path)


def main():
    pages: int = get_number_pages()
    article_type: str = get_type_article()
    for page in range(1, pages + 1):
        url_base = f"https://www.nature.com/nature/articles?sort=PubDate&year=2020&page={page}"
        articles_list = get_text(url_base, article_type)
        treat_title(articles_list)
        directory = f"Page_{page}"
        cwd = os.getcwd()
        change_directory(directory)
        if articles_list:
            save_content(articles_list)
        os.chdir(cwd)

    print("Saved all articles.")


if __name__ == "__main__":
    main()
