
from mozscape import Mozscape
from contextlib import closing
import traceback
import time
import pandas as pd

# Imput your member ID and secret key here
client = Mozscape('mozscape-d3909f420d', 'a223a4a9f87f71c8ba7c353598ec43ff')

url = 'https://filecoin.io/'
metrics = client.urlMetrics(url)

# Or if you just need results for one URL
mozMetrics = client.urlMetrics(url)

df = pd.DataFrame(mozMetrics)

# https://moz.com/help/guides/moz-api/mozscape/api-reference/url-metrics
# fmrp: normalized measure of the MozRank of the subdomain of the target URL
# fmrr: raw measure of the MozRank of the subdomain of the target URL
# pda: domain authority of the target URL's paid-level domain
# ueid: The number of external equity links from other root domains to pages on the target URL's root domain
# uid: number of internal and external, equity and non-equity links to the subdomain of the target URL
# umrp: normalized (ten-point, logarithmically-scaled) MozRank of the target URL
# umrr: raw (zero to one, linearly-scaled) MozRank of the target URL
# upa: normalized (zero to one hundred, logarithmically-scaled) page authority of the target URL
# us: HTTP status of the target URL
# ut: title of the target URL, if a title is available
# uu: canonical form of the source URL

df = df.rename(index=str, columns={"fmrp": "Subdomain", "pda": "Domain_Auth", "ueid": 'Ext_Equity_Links', "uid": "Total_Links", "umrp":"Moz_Ranking", "upa": "Page_Autho", 'ut': 'Token_Name', 'uu': 'Website'})
df = df.drop(columns=['fmrr', 'ulc', 'umrr', 'us'], axis=1)
df.set_index("Token_Name")


# links = client.links(url)

# # The links API has more columns to specify, as well as sort, scope, etc.
# links1 = client.links(url, scope='domain_to_domain', sort='domain_authority', filters=['external', 'nofollow'], targetCols=Mozscape.UMCols.url)


