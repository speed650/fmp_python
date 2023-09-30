from fmp_python.fmp import FMP


fmp = FMP(api_key='b818bb72d0efccf4d0d47dfd329e54ef')

print(fmp.get_company_profile('aapl'))
