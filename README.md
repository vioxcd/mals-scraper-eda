# Prototyping Cross-domain recommendation

usage:

1. user-link-scraper: get 20 online users links from ```/users```
2. user-link-deduplication: online users last longer than scraping session, so there's possible chance of duplication in scraping. deduplication erases duplicated record.
3. extract-profile: extract anime and manga stats from user profile
4. check-list-access: checks whether anime and manga list could be accessed. case when it can't include badresult (private list) or incompatible data table

etc

- extract-online-users: manual javascript extractor
