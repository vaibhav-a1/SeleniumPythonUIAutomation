*** Variables ***
# Application URLs
${env}       QA
${QA_url}    https://qa-vega.agilone.com/login
${CSEU_url}    https://cs-vega.eu.agilone.com/login
${CSGREEN_url}    https://cs-vega-green.agilone.com/login
${CSGCP_url}    https://cs-gcp-vega.agilone.com/login
${PRODEU_url}   https://hub.eu.agilone.com/login
${PRODGREEN_url}   https://hub2.agilone.com/login
${PRODGCP_url}   https://hub8.agilone.com/login

# browsername
${browsername}    Chrome
#Passwords
${QA_password}

# Usernames
#${QA_username}     aruna.boddu@acquia.com
${QA_username}     jenkins@agilone.com
${CSEU_username}     jenkins@agilone.com
${CSgreen_username}     jenkins@agilone.com
${CSGCP_username}     jenkins@agilone.com
${PORDEU_username}     jenkins@agilone.com
${PORDGREEN_username}     jenkins@agilone.com
${PORDGCP_username}     jenkins@agilone.com




${QA_loginpage_name}    Login
${CSEU_loginpage_name}    Login

#wait timings
${MAX_WAIT}    60s
${MIN_WAIT}     3s

#tenant_name
${QA_Regression_tenant_name}   QARegression
