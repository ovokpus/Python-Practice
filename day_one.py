import requests


def most_starred_repos(languages, sort="stars", order="desc"):
    url = 'https://api.github.com/search/repositories'

    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(url, params=params)
    status_code = response.status_code

    if status_code == 403:
        raise RuntimeError(
            "Rate limit reached. Please wait a minute and try again.")
    if status_code != 200:
        raise RuntimeError(
            f"An error occured. HTTP Status Code was: {status_code}.")
    else:
        data = response.json()
        records = data["items"]
        return records


def create_query(languages, min_stars=50000):
    # An example search query looks like:
    # stars:>50000 language:python language:javascript
    query = f"stars:>{min_stars} "

    for language in languages:
        query += f"language:{language} "
    return query


if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = most_starred_repos(languages)
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f" -> {name} is a {language} repo with {stars} stars.")
