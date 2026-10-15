# Web data tools for AI agents

Five tool sets for Claude, Cursor, VS Code and any other MCP client. Each one is an address of [Apify's hosted MCP server](https://docs.apify.com/integrations/mcp) that loads a fixed list of scrapers, so the agent gets a handful of tools for one job instead of the whole Apify Store.

## Connect

Add one of the addresses below as a remote MCP server (Streamable HTTP):

```json
{"mcpServers": {"reddit-data": {"url": "https://mcp.apify.com/?tools=benthepythondev/reddit-scraper,benthepythondev/reddit-search-scraper,benthepythondev/reddit-comments-scraper,benthepythondev/reddit-archive-scraper"}}}
```

The first connection opens Apify's sign-in page. A client without OAuth sends an Apify API token instead, as the header `Authorization: Bearer <token>`.

## What it costs

The tools run on your own Apify account. Each scraper charges per result, and its page in the Apify Store lists the price per plan. Apify's free plan includes $5 of usage a month, and no scraper here needs a login or cookies for the site it reads.

New to Apify? [Create an account](https://apify.com/?fpr=qolupv). I may earn a commission at no extra cost to you.

## The tool sets

### Reddit Data

Reddit posts, comments, keyword search and historical archives as tools.

```
https://mcp.apify.com/?tools=benthepythondev/reddit-scraper,benthepythondev/reddit-search-scraper,benthepythondev/reddit-comments-scraper,benthepythondev/reddit-archive-scraper
```

- [Reddit Scraper - Posts, Comments, Users & Search](https://apify.com/benthepythondev/reddit-scraper)
- [Reddit Search Scraper - Keyword Posts, Date Range, No Login](https://apify.com/benthepythondev/reddit-search-scraper)
- [Reddit Comments Scraper - Threads & Replies, No Login](https://apify.com/benthepythondev/reddit-comments-scraper)
- [Reddit Archive Scraper — Historical Posts for RAG](https://apify.com/benthepythondev/reddit-archive-scraper)

### Social Media Data

Instagram, TikTok, YouTube and Threads profiles, posts, comments and transcripts.

```
https://mcp.apify.com/?tools=benthepythondev/instagram-profile-scraper,benthepythondev/instagram-posts-scraper,benthepythondev/instagram-comments-scraper,benthepythondev/tiktok-profile-videos-scraper,benthepythondev/tiktok-comments-scraper,benthepythondev/youtube-transcript-scraper,benthepythondev/youtube-comments-scraper,benthepythondev/threads-public-scraper
```

- [Instagram Profile Scraper - Followers, Bio & Links](https://apify.com/benthepythondev/instagram-profile-scraper)
- [Instagram Posts Scraper - Captions, Likes & Media](https://apify.com/benthepythondev/instagram-posts-scraper)
- [Instagram Comments Scraper - Posts & Reels](https://apify.com/benthepythondev/instagram-comments-scraper)
- [TikTok Profile Videos Scraper - Views, Likes & Captions](https://apify.com/benthepythondev/tiktok-profile-videos-scraper)
- [TikTok Comments Scraper - Comments, Replies & Likes](https://apify.com/benthepythondev/tiktok-comments-scraper)
- [YouTube Transcript Scraper - Text, SRT & VTT](https://apify.com/benthepythondev/youtube-transcript-scraper)
- [YouTube Comments Scraper - Comments, Replies & Likes](https://apify.com/benthepythondev/youtube-comments-scraper)
- [Threads Scraper - Posts, Profiles & Replies](https://apify.com/benthepythondev/threads-public-scraper)

### Local Business Leads

Google Maps places with emails, phones and the tech stack of their websites.

```
https://mcp.apify.com/?tools=benthepythondev/google-maps-business-scraper,benthepythondev/google-maps-email-scraper,benthepythondev/website-contact-extractor,benthepythondev/tech-stack-detector
```

- [Google Maps Scraper - Business Contacts & Ratings](https://apify.com/benthepythondev/google-maps-business-scraper)
- [Google Maps Email Extractor - Emails, Phones & Social Links](https://apify.com/benthepythondev/google-maps-email-scraper)
- [Website Contact & Email Extractor - Emails, Phones, Socials](https://apify.com/benthepythondev/website-contact-extractor)
- [Tech Stack Detector - Wappalyzer & BuiltWith Alternative](https://apify.com/benthepythondev/tech-stack-detector)

### Real Estate Data

Zillow homes and rentals, Zumper rentals and Craigslist housing listings as tools.

```
https://mcp.apify.com/?tools=benthepythondev/zillow-scraper,benthepythondev/zillow-detail-scraper,benthepythondev/zillow-rentals-scraper,benthepythondev/zumper-rental-scraper,benthepythondev/craigslist-real-estate-scraper
```

- [Zillow Search Scraper - Homes For Sale & Sold by City or ZIP](https://apify.com/benthepythondev/zillow-scraper)
- [Zillow Detail Scraper - Property Data by URL, ZPID or Address](https://apify.com/benthepythondev/zillow-detail-scraper)
- [Zillow Rentals Scraper - Apartments, Units & Rent Prices](https://apify.com/benthepythondev/zillow-rentals-scraper)
- [Zumper Rental Scraper & Price Change Monitor](https://apify.com/benthepythondev/zumper-rental-scraper)
- [Craigslist Real Estate Scraper - FSBO Listings & Rentals](https://apify.com/benthepythondev/craigslist-real-estate-scraper)

The same listings without Apify or MCP: [Listingrail](https://listingrail.com/) is a REST API over 17 portals (Zillow, Redfin, Rightmove, Idealista, ImmoScout24, Bayut and more) with one key and one listing format.

### Jobs Data

Remote job boards, LinkedIn jobs, company ATS pages and Upwork jobs as tools.

```
https://mcp.apify.com/?tools=benthepythondev/remote-jobs-aggregator,benthepythondev/linkedin-jobs-scraper,benthepythondev/ats-jobs-aggregator,benthepythondev/upwork-jobs-scraper
```

- [Remote Jobs Scraper — 6 Boards, One Feed](https://apify.com/benthepythondev/remote-jobs-aggregator)
- [LinkedIn Jobs Scraper - Full Descriptions & Job Feeds](https://apify.com/benthepythondev/linkedin-jobs-scraper)
- [💼 ATS Jobs Aggregator - Greenhouse, Lever, Ashby & More](https://apify.com/benthepythondev/ats-jobs-aggregator)
- [Upwork Jobs Scraper - Job Search with Client Details](https://apify.com/benthepythondev/upwork-jobs-scraper)

Besides the scrapers, Apify's server adds four helpers to every set: read a run, read its dataset, read a stored record, stop a run.

## Questions

Open an issue here, or on the page of the scraper in the Apify Store.
