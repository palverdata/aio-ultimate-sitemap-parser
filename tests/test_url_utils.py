from unittest import TestCase

from usp.util.url import extract_year_month_from_sitemap


class TestUrlUtils(TestCase):
    def test_extract_year_month_from_sitemap(self):
        assert extract_year_month_from_sitemap(
            "https://www.nytimes.com/2020/01/01"
        ) == (
            2020,
            1,
        )
        assert extract_year_month_from_sitemap("https://www.nytimes.com/2020-01") == (
            2020,
            1,
        )
        assert extract_year_month_from_sitemap(
            "https://www.nytimes.com/sitemaps/new/sitemap-2021-04.xml.gz"
        ) == (2021, 4)
        assert extract_year_month_from_sitemap(
            "https://oantagonista.com.br/sitemap-posttype-post.202402.xml"
        ) == (2024, 2)

        additional_examples = [
            "https://example.com/sitemap-2021-04.xml",
            "https://example.com/sitemap-2021-04.xml.gz",
            "https://example.com/sitemaps/news/sitemap-2021-04.xml",
            "https://example.com/sitemaps/news/sitemap-2021-04.xml.gz",
            "https://example.com/sitemaps/2021/04/sitemap.xml",
            "https://example.com/sitemaps/2021/04/sitemap.xml.gz",
            "https://example.com/sitemap-posts-2021-04.xml",
            "https://example.com/sitemap-posts-2021-04.xml.gz",
            "https://oantagonista.com.br/sitemap-posttype-post.202104.xml",
            "https://example.com/sitemap.xml?year=2021&month=04",
            "https://example.com/sitemap.xml.gz?year=2021&month=04",
        ]

        for example in additional_examples:
            assert extract_year_month_from_sitemap(example) == (2021, 4)
