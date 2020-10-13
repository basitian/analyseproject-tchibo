# Tchibo Kaffeevollautomat »Esperto Caffè« review scrapers

This project contains [Scrapy](https://scrapy.org) spiders to retrieve review data for Tchibo coffe maker [Tchibo Kaffeevollautomat »Esperto Caffè«](https://www.tchibo.de/tchibo-kaffeevollautomat-esperto-caffe-p400167658.html?x=H4sIAAAAAAAAAAGyAE3_ETMsDgAAAXUjl_SVABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEG4bAOjLlUNnOrgTNB-N5UEAAABg55DeNbrLA_mu0gedRQcCxlmo7aCfuK9PLzz1ZGX7YMko18PCZOw3ZxQS8vl2_jXmGGioO4cHJXH4cQdiJc-wdFfPx6h08LTD-gS4-zSMN9xHXKJPPSfLwWfp42GAqg3ZABTpFQCClMV8DGfQBm46910yCaCJs3V9GqeyAAAA) from different online shopping web pages.

Currently the following scrapers are implemented:
* [Otto](https://www.otto.de/p/tchibo-kaffeevollautomat-esperto-caffe-fuer-espresso-cafe-crema-americano-898416526-kundenbewertungen/#variationId=898416603)

## Configuration

Configuration can be done via the standard Scrapy configuration files (`scrapy.cfg`, `spiders/settings.py`)

## Starting Scrapers
A scraper can be started via the console command: `scrapy crawl [scraper_name]`.
Adding the flag `-L WARN` suppresses the log output and restricts the output to warnings.
If you want to save the output to a file, add the `-o [output_filename]`option.

### Full example
The command `scrapy crawl otto_reviews -L WARN -o otto_new.json` starts the `otto_reviews`scraper and saves it outputs to a file `otto_new.json` in the current working directory. No additional logs will be written to the console.