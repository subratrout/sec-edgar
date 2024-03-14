from secedgar import filings, FilingType
from biopharma_tickers import test_biopharma_tickers

# 10Q filings for Apple (ticker "aapl")
my_filings = filings(cik_lookup= test_biopharma_tickers,
                     filing_type=FilingType.FILING_10K,
                     user_agent="Your name (your email)")
my_filings.save('/Users/subratrout/Downloads/python_projects/sec-edgar/downloaded-data')
