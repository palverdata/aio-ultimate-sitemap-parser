import re


def extract_year_month_from_sitemap(url: str) -> tuple[int, int]:
    pattern = r"(\d{4})[-/](\d{2})|(\d{4})(\d{2})"
    match = re.search(pattern, url)

    year, month = None, None

    if match:
        year, month = (
            match.group(1) or match.group(3),
            match.group(2) or match.group(4),
        )
        year = int(year)
        month = int(month)
    else:
        query = url.split("?")
        if len(query) > 1:
            for param in query[1].split("&"):
                key, value = param.split("=")
                if key == "year":
                    year = int(value)
                elif key == "month":
                    month = int(value)

    if year and month:
        return max(year, 1971), month

    raise ValueError("No valid year and month found in URL")
