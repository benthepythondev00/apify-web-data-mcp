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

- [Reddit Scraper: Posts & Full Comment Threads, Excel Rows, MCP](https://apify.com/benthepythondev/reddit-scraper)
- [Reddit Search Scraper - Keyword Posts, Date Range, No Login](https://apify.com/benthepythondev/reddit-search-scraper)
- [Reddit Comments Scraper - Threads & Replies to CSV, No Login](https://apify.com/benthepythondev/reddit-comments-scraper)
- [Reddit Archive Scraper — Historical Posts and Comments by Date](https://apify.com/benthepythondev/reddit-archive-scraper)

### Social Media Data

Instagram, TikTok, YouTube and Threads profiles, posts, comments and transcripts.

```
https://mcp.apify.com/?tools=benthepythondev/instagram-profile-scraper,benthepythondev/instagram-posts-scraper,benthepythondev/instagram-comments-scraper,benthepythondev/tiktok-profile-videos-scraper,benthepythondev/tiktok-comments-scraper,benthepythondev/youtube-transcript-scraper,benthepythondev/youtube-comments-scraper,benthepythondev/threads-public-scraper
```

- [Instagram Profile Scraper - Bio Links, Follower Count, No Login](https://apify.com/benthepythondev/instagram-profile-scraper)
- [Instagram Posts Scraper - Captions, Likes, Media, No Login](https://apify.com/benthepythondev/instagram-posts-scraper)
- [Instagram Comments Scraper - Posts & Reels, No Login](https://apify.com/benthepythondev/instagram-comments-scraper)
- [TikTok Profile & User Videos Scraper - All Videos, No Login](https://apify.com/benthepythondev/tiktok-profile-videos-scraper)
- [TikTok Comments Scraper - Replies, Likes, No Login](https://apify.com/benthepythondev/tiktok-comments-scraper)
- [YouTube Transcript Scraper - Text, SRT & VTT](https://apify.com/benthepythondev/youtube-transcript-scraper)
- [YouTube Comments Scraper — Replies, Shorts & Live](https://apify.com/benthepythondev/youtube-comments-scraper)
- [Threads Scraper - Posts, Profiles, Replies, No Login](https://apify.com/benthepythondev/threads-public-scraper)

### Local Business Leads

Google Maps places with emails, phones and the tech stack of their websites.

```
https://mcp.apify.com/?tools=benthepythondev/google-maps-business-scraper,benthepythondev/google-maps-email-scraper,benthepythondev/website-contact-extractor,benthepythondev/tech-stack-detector
```

- [Google Maps Scraper - Business Leads by City: Phone & Website](https://apify.com/benthepythondev/google-maps-business-scraper)
- [Google Maps Email Extractor - Emails, Phones & Social Links](https://apify.com/benthepythondev/google-maps-email-scraper)
- [Website Contact & Email Extractor - Emails, Phones, Socials](https://apify.com/benthepythondev/website-contact-extractor)
- [Tech Stack Detector - Wappalyzer & BuiltWith Alternative](https://apify.com/benthepythondev/tech-stack-detector)

### Real Estate Data

Zillow homes and rentals, Zumper rentals and Craigslist housing listings as tools.

```
https://mcp.apify.com/?tools=benthepythondev/zillow-scraper,benthepythondev/zillow-detail-scraper,benthepythondev/zillow-rentals-scraper,benthepythondev/zumper-rental-scraper,benthepythondev/craigslist-real-estate-scraper
```

- [Zillow Search Scraper - Homes For Sale & Sold by City or ZIP](https://apify.com/benthepythondev/zillow-scraper)
- [Zillow Detail Scraper: Property Details by URL, ZPID, Address](https://apify.com/benthepythondev/zillow-detail-scraper)
- [Zillow Scraper: Apartments for Rent + Rent Change Monitor](https://apify.com/benthepythondev/zillow-rentals-scraper)
- [Zumper Scraper: Apartments for Rent + Rent Change Monitor](https://apify.com/benthepythondev/zumper-rental-scraper)
- [Craigslist Real Estate Scraper - FSBO Listings & Rentals](https://apify.com/benthepythondev/craigslist-real-estate-scraper)

The same listings without Apify: [Listingrail](https://listingrail.com/) is a REST API over 22 portals in 13 countries (Zillow, Redfin, Rightmove, Idealista, ImmoScout24, Bayut and more) with one key and one listing format, and the same search as an MCP server at `https://listingrail.com/mcp` (send the key as `Authorization: Bearer re_...`).

### Jobs Data

Remote job boards, LinkedIn jobs, company ATS pages and Upwork jobs as tools.

```
https://mcp.apify.com/?tools=benthepythondev/remote-jobs-aggregator,benthepythondev/linkedin-jobs-scraper,benthepythondev/ats-jobs-aggregator,benthepythondev/upwork-jobs-scraper
```

- [Remote Jobs Scraper: Worldwide vs US-only Filter, 7 Boards](https://apify.com/benthepythondev/remote-jobs-aggregator)
- [LinkedIn Jobs Scraper - Full Descriptions, No Login](https://apify.com/benthepythondev/linkedin-jobs-scraper)
- [ATS Jobs Aggregator - Greenhouse, Lever, Ashby & More](https://apify.com/benthepythondev/ats-jobs-aggregator)
- [Upwork Jobs Scraper - Job Alerts & Client Details, No Login](https://apify.com/benthepythondev/upwork-jobs-scraper)

Besides the scrapers, Apify's server adds four helpers to every set: read a run, read its dataset, read a stored record, stop a run.

## Hosted servers

Eight hosted servers run on our side behind [MCPize](https://mcpize.com), which handles keys and billing: a free plan with 100 calls a month, then paid tiers for higher volume. Get a key on the server's page and send it as `Authorization: Bearer <key>`.

### [SocialBlade Creator Stats](https://mcpize.com/mcp/socialblade-creator-stats)

YouTube, TikTok, Instagram and Twitch growth history and 7/30/90-day gains from SocialBlade.

```
https://socialblade-creator-stats.mcpize.run/mcp
```

### [Ad Library Intelligence](https://mcpize.com/mcp/ad-library-intelligence)

Competitor ads from Meta Ads, Google Ads Transparency and LinkedIn Ad Library plus ads.txt.

```
https://ad-library-intelligence.mcpize.run/mcp
```

### [Business Data: Open Data, Crypto & Startups](https://mcpize.com/mcp/business-open-data-crypto)

Government open-data search, crypto prices, Fear & Greed, Bitcoin stats, FX rates, startups.

```
https://business-open-data-crypto.mcpize.run/mcp
```

### [Reddit: Posts, Search, Comments & History](https://mcpize.com/mcp/reddit-posts-search-comments)

Reddit posts, nested Reddit comments, date-range search and archive history back to 2008.

```
https://reddit-posts-search-comments.mcpize.run/mcp
```

### [Jobs Data Intelligence](https://mcpize.com/mcp/jobs-data-intelligence)

Live remote, ATS and startup job listings from 18 boards including Greenhouse, Ashby and Wellfound.

```
https://jobs-data-intelligence.mcpize.run/mcp
```

### [Real Estate Listings](https://mcpize.com/mcp/real-estate-listings)

Live sale and rental listings from Zillow, Realtor, Zumper, Craigslist and EU property portals.

```
https://real-estate-listings.mcpize.run/mcp
```

### [Reddit Archive: Historical Posts & Comments](https://mcpize.com/mcp/reddit-archive-history)

Historical Reddit posts, threads and comments by UTC date window back to 2008 from public archives.

```
https://reddit-archive-history.mcpize.run/mcp
```

### [Reviews & Travel Data](https://mcpize.com/mcp/reviews-and-travel-data)

Google Play, App Store and Tripadvisor reviews, flight fares, airport status, METAR and transit.

```
https://reviews-and-travel-data.mcpize.run/mcp
```

## Questions

Open an issue here, or on the page of the scraper in the Apify Store.
