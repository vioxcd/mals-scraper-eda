# MALs Scraper and EDA

Interesting stuff is in the EDA notebook

## Scraper Usage

1. user-link-scraper: get 20 online users links from ```/users```
2. user-link-deduplication: online users last longer than scraping session, so there's possible chance of duplication in scraping. deduplication erases duplicated record.
3. extract-profile: extract anime and manga stats from user profile
4. check-list-access: checks whether anime and manga list could be accessed. case when it can't include badresult (private list) or incompatible data table

data flow (in csv):

```link (dedup) -> all profile -> filtered profile (anime & manga days > 1) -> username -> access (inaccessible marked) -> offset -> lists```

etc

- extract-online-users: manual javascript extractor
