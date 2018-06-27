# -*- coding=utf-8 -*-
# Como usar special characters
SPECIAL_CHARACTERS = ['¿']
SPECIAL_CHARACTERS = [c.decode('utf-8') for c in SPECIAL_CHARACTERS]

# All valid selector types
# "id": 	find by id
# "n": 		find by name
# "x":		find by xpath
# "lt": 	find by link text
# "plt": 	find by partial link text
# "tn": 	find by tag name
# "cn":  	find by class name
# "cs": 	find by css selector
SELECTOR_TYPES = "(id|n|x|lt|plt|tn|cn|cs)"


SEARCH_TYPES = {
    "id": "find_element_by_id",
    "x":  "find_element_by_xpath",
    "n":  "find_element_by_name",
    "lt": "find_element_by_link_text",
    "plt": "find_element_by_partial_link_text",
    "tn": "find_element_by_tag_name",
    "cn": "find_element_by_class_name",
    "cs": "find_element_by_css_selector",
}

MULTIPLE_SEARCH_TYPES = {
    "x":  "find_elements_by_xpath",
    "n":  "find_elements_by_name",
    "lt": "find_elements_by_link_text",
    "plt": "find_elements_by_partial_link_text",
    "tn": "find_elements_by_tag_name",
    "cn": "find_elements_by_class_name",
    "cs": "find_elements_by_css_selector",
}

EMAIL_ACCOUNT = "automatedtests@mobomo.com"
PASSWORD = "mobomo2017"
