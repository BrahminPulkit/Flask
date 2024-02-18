import paralleldots
paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentinal_Analysis(text):
    sentinal_Analysis = paralleldots.sentimental_analysis(text)
    return sentinal_Analysis

def abuse_Deductions(text):
    abuse_Deductions = paralleldots.abuse_Deductions(text)
    return abuse_Deductions

# Note go to comprend.io website to fatch the key 