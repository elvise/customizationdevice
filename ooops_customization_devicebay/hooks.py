# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ooops_customization_devicebay"
app_title = "Ooops Customization Devicebay"
app_publisher = "Syed Abdul Qadeer"
app_description = "Ooops Customizations for the customer - Devicebay"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sdqadeer44@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ooops_customization_devicebay/css/ooops_customization_devicebay.css"
# app_include_js = "/assets/ooops_customization_devicebay/js/ooops_customization_devicebay.js"

# include js, css files in header of web template
# web_include_css = "/assets/ooops_customization_devicebay/css/ooops_customization_devicebay.css"
# web_include_js = "/assets/ooops_customization_devicebay/js/ooops_customization_devicebay.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ooops_customization_devicebay.utils.get_home_page"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": {
            "fieldname": [
                "in", [
                    "prezzo_consigliato_al_rivenditore"
                ]
            ]
        }
    }
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ooops_customization_devicebay.install.before_install"
# after_install = "ooops_customization_devicebay.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ooops_customization_devicebay.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ooops_customization_devicebay.tasks.all"
# 	],
# 	"daily": [
# 		"ooops_customization_devicebay.tasks.daily"
# 	],
# 	"hourly": [
# 		"ooops_customization_devicebay.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ooops_customization_devicebay.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ooops_customization_devicebay.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ooops_customization_devicebay.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ooops_customization_devicebay.event.get_events"
# }

