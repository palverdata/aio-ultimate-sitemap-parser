from datetime import datetime, timezone

from usp.tree import sitemap_tree_for_homepage


def main():
    urls = [
        "https://www.nytimes.com/",
        "http://globo.com",
    ]

    for url in urls:
        tree = sitemap_tree_for_homepage(
            url,
            cutoff_date=datetime(2023, 12, 31).astimezone(timezone.utc),
        )

        print(tree)
        pages = list(tree.all_pages())

        print(pages)


if __name__ == "__main__":
    main()
