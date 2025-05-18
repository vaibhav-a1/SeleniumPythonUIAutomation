from symtable import Class


class LocatorsLoginPage:
    USERNAME_FIELD = 'username'
    PASSWORD_FIELD = 'password'
    LOGIN_BUTTON = 'button[name="login-submit"]'


class GeneralLocators:
    PROFILE_BUTTON = 'button[id="right-nav-toggle"]'
    CAMPAIGNS_PLUS_BUTTON = 'a[href="/actions/campaign"]'
    LOADING_BAR = 'loading-bar'
    LOADING_BAR_SPINNER = 'loading-bar-spinner'
    BUTTON_360 = 'a[href="/360profiles"]'
    ANALYTICS_BUTTON = 'button[aria-controls="docs-menu-Analytics"]'
    BUTTON_METRICS = 'a[href="/metrics"]'
    CDP_STUDIO= '//span[normalize-space(text())="CDP Studio"]'
    EXEC_CAL='/html/body/div[2]/div/div/md-sidenav/aside/div/ul/li[1]/ul/li[9]/menu-link/a'

class CustomAttribute:
    Launch='//button[normalize-space(text())="Launch Custom Attributes"]'
    TABLE_SELECT = '//div[@data-test-id="table"]'
    ATTRIBUTE_SELECT = '//div[@data-test-id="attribute"]'
    FORM_FIELD_2 = '//dxp-web-ui-form-field[2]'

class LocatorsMetrics:
    MODEL_SELECT = '//ul[@aria-label="Field Picker, Search Results"]/div/div/ul/div/div/div/ul/li/div/div/div/span/div/div/span/span/span/span'
    FRAMEID = "looker"
    METRICS_DATA_FRAME = "looker-embed"
    RUN_BTN = 'button[aria-label="Run"]'
    AUDIENCE_COUNT_SELECT = "//span[@class='highlight-label']/span"
    NEW_BUTTON = 'button[aria-label="New"]'
    NEW_LOOK_BUT = '//span[normalize-space(text())="New Look"]'
    SEARCH_FIELD = 'input[placeholder="Search Fields Below"]'
    CLEAR_SEARCH = '//div[normalize-space(text())="Clear Field"]/..'
    TABLE_PRESENT = '//tr/td[normalize-space(text())="1"]'
    QUERY_RAN = "title-stats"
    METRICS_LAUNCHPAD = 'vega-file-tree-itemrow-Metrics Launchpad'
    MACHINELEARNING_DASHBOARD = "//h3[text()=' {}}']"

class Locators360:
    MASTER_CUSTOMERID = "mastercustomerid"
    FIRST_NAME = "firstname"
    LAST_NAME = "customer360-list-lastname"
    EMAIL = "customer360-list-email"
    PHONE="customer360-list-phone"
    SCN="customer360-list-source-customer-number"
    GENDER="customer360-list-Gender"
    CC="customer360-list-CountryCode"
    ADDR="customer360-list-RBDI"
    ZIP="/html/body/div[2]/div/div/md-content/div/div[1]/div/div/div/md-whiteframe/div[2]/md-input-container[5]/input"

    ZIPCODE = "zipcode"
    CITY = "city"
    STATE = "state"
    attribute_dict = {FIRST_NAME: '//tbody/tr/td[2]',
                      LAST_NAME: '//tbody/tr/td[3]',
                      EMAIL: '//tbody/tr/td[4]',
                      ZIPCODE: '//tbody/tr/td[10]',
                      CITY: '//tbody/tr/td[8]',
                      STATE: '//tbody/tr/td[9]'}
    CLEAR_SEARCH = 'button[aria-label="Clear search"]'
    SOURCE_CUSTOMER_NUMBER_FIELD = 'input[name="customer360-list-source-customer-number"]'
    FEATURE_NAMES_ON_CHART = 'g[class*="highcharts-axis-labels highcharts-xaxis-labels"]>text'
    SHAP_VALUES_DATA_ON_CHART = 'g[class*="highcharts-data-label"]>text>tspan:nth-child(2)'
    MACHINE_LEARNING_NAV = 'button[name="360overview-details-OVERVIEW-ML"]'
    SECOND_MOST_LIKELY_CLUSTER = f'//div[text()="Second Most Likely Cluster"]/../../md-card-content//div/div/span'
    BACK = 'button[aria-label="Back"]'
    HELP_BUTTON = "a[href='https://docs.acquia.com/customer-data-platform/machine-learning/explainable-predictions/']"
    GRAPH_DESC = "span[class = 'graph_desc ng-binding']"
    X_AXIS_LABEL = "g[class='highcharts-axis-labels highcharts-yaxis-labels ']>text"
    CLOSE_SHAP_WINDOW = "context-copy-dialog-close"
    FIRSTNAME="customer360-list-firstname"
    FN='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/md-whiteframe[1]/div[1]/md-input-container[1]/input[1]'
    USERSELECT='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]'
    USER='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/div[1]/div[2]/div[1]/md-table-container[1]/table[1]/tbody[1]/tr[1]/td[2]'
    PROFILE = '/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[2]/span[1]'
    JOURNEY='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[3]/span[1]'
    TRANS='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[4]'
    ML='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[5]/span[1]'
    IDENTITIES='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[6]'
    SUBS='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[7]/span[1]'
    HOUSEHOLD='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[8]/span[1]'
    MC='/html[1]/body[1]/div[2]/div[1]/div[1]/md-content[1]/customer360-component[1]/div[1]/md-tabs[1]/md-tabs-wrapper[1]/md-tabs-canvas[1]/md-pagination-wrapper[1]/md-tab-item[9]/span[1]'
class GoogleLocators:
    APP_LIST = 'a[aria-label="Google apps"]'
    COUNTRY = 'uU7dJb'
    SEARCH_BOX = 'q'
    SEARCH_BY_VOICE = 'div[aria-label="Search by voice"]'


class CampaignPlusLocators:
    SEND_NOW_BUTTON = 'button[aria-label="send now"]'
    LAST_PRODUCT_BROWSED = '//span[normalize-space(text())="Last Products Browsed"]'
    APPLY_BUTTON = 'button[aria-label="Apply"]'
    NEW_BUTTON = 'button[aria-label="New"]'
    TEST_STPF_CONNECTOR_SELECT = '//div[normalize-space(text())="Test_SFTP"]'
    AVAILABILITY_STATUS = '//div[normalize-space(text())="Availability Status"]'
    ADD_FOLDER_BUTTON = 'button[name="add-folder-btn"]'
    NEW_CAMPAIGN_BUTTON = 'button[name = "file-list-create"]'
    NEW_CAMPAIGN_NAME_FIELD = 'campNewName'
    NEW_FOLDER_NAME_FIELD = 'input[placeholder="New folder name"]'
    NEW_FOLDER_SAVE_BUTTON = 'button[name="folder-dialog-save-button"]'
    AUTO_CONTENT_FOLDER = '//div[normalize-space(text())="Auto_Content"]'
    NEW_CAMPAIGN_NEXT_BUTTON = 'campaignSetupNext'
    CAMPAIGN_BUILDER_NEXT = 'campaignBuilderNext'
    CAMPAIGN_CONTENT_NEXT = 'campaignContentNext'
    CAMPAIGN_DESTINATION_NEXT = 'campaignDestinationNext'
    CAMPAIGNS_AUDIENCE_NEXT = 'campaignAudienceNext'
    INCLUDE_BUTTON = 'button[aria-label="add group of customers to include"]'
    CUSTOMER_ATTRIBUTES = '//div[normalize-space(text())="Customer Attributes"]'
    CITY = '//div[normalize-space(text())="City"]'
    SEARCH_FIELD = 'input[name = "dataset-selection-search-text"]'
    SELECT_CARD = 'div[name="ruleCardContentSelected-Machine Learning Segments"]'
    FILTER_TYPE_DROP_DOWN = 'span[class="md-select-icon"]'
    FILTER_TYPE_SELECT = 'md-option[value="IN"]'
    MULTI_INPUT_HOVER_BUTTON = 'button[name="multi-input-bttn"]'
    MULTI_INPUT_BUTTON = 'button[name="open-audience-multi-select-dialog"]'
    MULTI_INPUT_BUTTON_MANUAL = 'button[aria-label="Manually enter multiple values"]'
    VALUE_INPUT_FIELD = 'textarea[aria-label="Enter values here"]'
    VALUE_INPUT_FIELD_MANUAL = 'textarea[name="rawInput"]'
    VALUE_INPUT_CONFIRM_BUTTON = 'button[aria-label="confirm"]'
    REFRESH_AUDIENCE_COUNT = 'button[name = "refresh-audience-count"]'
    AUDIENCE_COUNT = 'span[class="md-caption ng-binding"]'
    REMOVE_VALUE = 'button[class="md-chip-remove ng-scope"]'
    MAKE_PAGE_INTERACTABLE = 'div[name="header-route-field"]'
    ADD_CONTENT = 'button.ng-scope[name="content-model-group-select-include'


class ElementFunction:
    SWITCH_FRAME = "frame"
    CLEAR_FIELD = "clear_field"
    GET_COUNT = "count"
    CLICK_BUTTON = "button"
    ENTER_TEXT_IN_FIELD = "field"
    ELEMENT_TEXT = "text"
    HOVER_OVER_ELEMENT = "hover"
    ACTIONS_ON_LIST = "list"


class LocatorType:
    XPATH = "XPATH"
    CSS = "CSS"
    NAME = "NAME"
    ID = "ID"
    CLASS = "CLASS"
