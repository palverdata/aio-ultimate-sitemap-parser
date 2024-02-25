import asyncio
from datetime import datetime, timezone

import aiohttp

from usp.tree import sitemap_tree_for_homepage


async def main():
    urls = [
        "https://www.nytimes.com/",
        "http://globo.com",
        "http://theepochtimes.com",
        "http://exame.com",
    ]

    conn = aiohttp.TCPConnector(
        limit=None,
        ssl=False,
    )

    client = aiohttp.ClientSession(
        connector=conn, timeout=aiohttp.ClientTimeout(total=60)
    )

    from usp.web_client.aiohttp_client import AioHttpWebClient

    aiohttp_web_client = AioHttpWebClient(client)

    for url in urls:
        tree = await sitemap_tree_for_homepage(
            url,
            web_client=aiohttp_web_client,
            cutoff_date=datetime(2023, 12, 31).astimezone(timezone.utc),
        )

        print(tree)
        pages = list(tree.all_pages())

        print(pages)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
