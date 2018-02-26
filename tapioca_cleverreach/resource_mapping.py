# coding: utf-8

RESOURCE_MAPPING = {
    'login': {
        'resource': 'login.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/login-v2/login_post',
        'methods': ['POST'],
    },
    'login_refresh': {
        'resource': 'login/refresh.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/login-v2/refresh_post',
        'methods': [''],
    },
    'clients': {
        'resource': 'clients.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/list_get',
        'methods': ['GET'],
    },
    'client': {
        'resource': 'clients.json/{id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/retrieve_get',
        'methods': ['GET'],
    },
    'client_active_receiver_count': {
        'resource': 'clients.json/{id}/activereceivercount',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/activereceivercount_get',
        'methods': ['GET'],
    },
    'client_invoice_address': {
        'resource': 'clients.json/{id}/invoiceaddress',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/invoiceaddress_get',
        'methods': ['GET'],
    },
    'client_payment_methods': {
        'resource': 'clients.json/{id}/paymentmethods',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/paymentmethods_get',
        'methods': ['GET'],

    },
    'client_plan_info': {
        'resource': 'clients.json/{id}/position',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/plan__get',
        'methods': ['GET'],
    },
    'client_plan': {
        'resource': 'clients.json/{id}/rate',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/plan_get',
        'methods': ['GET'],
    },
    'client_receiver_count ': {
        'resource': 'clients.json/{id}/receivercount',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/receivercount_get',
        'methods': ['GET'],
    },
    'client_jwt_token': {
        'resource': 'clients.json/{id}/token',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/retrieveJWT_get',
        'methods': {'GET': {'params': ['ONE', 'TWO'], 'optional_params': ['Onee']}},
    },
    'client_user_list': {
        'resource': 'clients.json/{id}/users',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/userlist_get',
        'methods': ['GET'],
    },
    'whoami': {
        'resource': 'clients/whoami.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/whoami_get',
        'methods': ['GET'],
    },
    'authcode': {
        'resource': 'clients/authcode.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/clients-v2/retrieveAuthCode_post',
        'methods': ['POST'],
    },
    'my_content_add': {
        'resource': 'mycontent.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/mycontent-v2/registerMyContent_post',
        'methods': ['POST'],
    },
    'my_content_delete': {
        'resource': 'mycontent.json/{id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/mycontent-v2/removeMyContent_delete',
        'methods': ['DELETE'],
    },
    'blacklist': {
        'resource': 'blacklist.json',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/blacklist-v2/list_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/blacklist-v2/create_post',
                 'https://rest.cleverreach.com/explorer/v2/#!/blacklist-v2/remove_delete'],
        'methods': ['GET', 'POST', 'DELETE'],
    },
    'groups': {
        'resource': 'groups.json',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/create_post'],
        'methods': ['GET', 'POST'],
    },
    'groups_attributes': {
        'resource': 'groups.json/attributes',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list__get',
        'methods': ['GET'],
    },
    'group_attributes': {
        'resource': 'groups.json/{group_id}/attributes',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list__get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/create__post'],
        'methods': ['GET', 'POST'],
    },
    'group_attribute': {
        'resource': 'groups.json/{groups_id}/attributes/{attribute_id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/update__put',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/remove__delete'],
        'methods': ['PUT', 'DELETE'],
    },
    'group_blacklist': {
        'resource': 'groups.json/{group_id}/blacklist',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/groupBlacklist_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/groupBlacklistAdd_post'],
        'methods': ['GET', 'POST'],
    },
    'group_blacklist_remove': {
        'resource': 'groups.json/{group_id}/blacklist/{id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/groupBlacklistRemove_delete',
        'methods': ['DELETE'],
    },
    'group_filters': {
        'resource': 'groups.json/{group_id}/filters',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list___get',
        'methods': ['GET'],
    },
    'group_filter': {
        'resource': 'groups.json/{group_id}/filters/{filter_id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/retrieve__get',
        'methods': ['GET'],
    },
    'group_filter_receivers': {
        'resource': 'groups.json/{group_id}/filters/{filter_id}/receivers',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list____get',
        'methods': ['GET'],
    },
    'group_filter_stats': {
        'resource': 'groups.json/{group_id}/filters/{filter_id}/stats',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/filterStats_get',
        'methods': ['GET'],
    },
    'group_receivers': {
        'resource': 'groups.json/{group_id}/receivers',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list_____get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/insert_post'],
        'methods': ['GET', 'POST'],
    },
    'group_receivers_delete': {
        'resource': 'groups.json/{group_id}/receivers/deletemultiple',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/removeMultiple_post',
        'methods': ['POST'],
    },
    'group_receivers_add': {
        'resource': 'groups.json/{group_id}/receivers/insert',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/insert__post',
        'methods': ['POST'],
    },
    'group_receivers_upsert': {
        'resource': 'groups.json/{group_id}/receivers/upsert',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/upsert_post',
        'methods': ['POST'],
    },
    'group_receivers_valid': {
        'resource': 'groups.json/{group_id}/receivers/isvalid',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/isvalid_post',
        'methods': ['POST'],
    },
    'group_receiver': {
        'resource': 'groups.json/{group_id}/receivers/{id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/retrieve___get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/update___put',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/remove___delete'],
        'methods': ['GET', 'PUT', 'DELETE'],
    },
    'group_receiver_events': {
        'resource': 'groups.json/{group_id}/receivers/{id}/events',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list______get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/create___post'],
        'methods': ['GET', 'POST'],
    },
    'group_receiver_orders': {
        'resource': 'groups.json/{group_id}/receivers/{id}/orders',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/list_______get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/create____post'],
        'methods': ['GET', 'POST'],
    },
    'group_receiver_attributes': {
        'resource': 'groups.json/{group_id}/receivers/{id}/attributes',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/retrievePoolAttributes_get',
        'methods': ['GET'],
    },
    'group_receiver_attribute_value': {
        'resource': 'groups.json/{group_id}/receivers/{id}/attributes/{attribute_id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/savePoolAttribute_put',
        'methods': ['PUT'],
    },
    'group': {
        'resource': 'groups.json/{group_id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/groups-v2/retrieve_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/update_put',
                 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/remove_delete'],
        'methods': ['GET', 'PUT', 'DELETE'],
    },
    'group_truncate': {
        'resource': 'groups.json/{group_id}/truncate',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/truncate_delete',
        'methods': ['DELETE'],
    },
    'group_advanced_stats': {
        'resource': 'groups.json/{group_id}/advancedstats',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/advstats_get',
        'methods': ['GET'],
    },
    'group_forms': {
        'resource': 'groups.json/{group_id}/forms',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/forms_get',
        'methods': ['GET'],
    },
    'group_stats': {
        'resource': 'groups.json/{group_id}/stats',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/stats_get',
        'methods': ['GET'],
    },
    'group_filter_add': {
        'resource': 'groups.json/{group_id}/filters/new',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/createFilter_post',
        'methods': ['POST'],
    },
    'group_import_csv': {
        'resource': 'groups.json/{group_id}/importcsv',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/importcsv_post',
        'methods': ['POST'],
    },
    'group_receiver_tags': {
        'resource': 'groups.json/{group_id}/receivers/{id}/tags',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/addTags_post',
        'methods': ['POST'],
    },
    'group_receiver_activate': {
        'resource': 'groups.json/{group_id}/receivers/{id}/setactive',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/setActive_put',
        'methods': ['PUT'],
    },
    'group_receiver_deactivate': {
        'resource': 'groups.json/{group_id}/receivers/{id}/setinactive',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/groups-v2/setInactive_put',
        'methods': ['PUT'],
    },
    'forms': {
        'resource': 'forms.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/forms-v2/list_get',
        'methods': ['GET'],
    },
    'form': {
        'resource': 'forms.json/{id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/forms-v2/retrieve_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/forms-v2/remove_delete'],
        'methods': ['GET', 'DELETE'],
    },
    'form_code': {
        'resource': 'forms.json/{id}/code',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/forms-v2/retrieveCode_get',
        'methods': ['GET'],
    },
    'form_mail': {
        'resource': 'forms.json/{id}/send/{type}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/forms-v2/sendMail_post',
        'methods': ['POST'],
    },
    'attributes': {
        'resource': 'attributes.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/attributes-v2/list_get',
        'methods': ['GET', 'POST'],
    },
    'attribute': {
        'resource': 'attributes.json/{id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/attributes-v2/retrieve_get',
        'methods': ['GET', 'PUT', 'DELETE'],
    },
    'receivers_filter': {
        'resource': 'receivers/filter.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/runtimeFilter_post',
        'methods': ['POST'],
    },
    'receivers_valid': {
        'resource': 'receivers/isvalid.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/isvalid_post',
        'methods': ['POST'],
    },
    'receivers_tags': {
        'resource': 'receivers/tags.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/retrieveTagsList_get',
        'methods': ['GET'],
    },
    'receivers_delete': {
        'resource': 'receivers/deletemultiple.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/removeMultiple_post',
        'methods': ['POST'],
    },
    'receiver': {
        'resource': 'receivers.json/{id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/retrieve_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/remove_delete'],
        'methods': ['GET', 'DELETE'],
    },
    'receiver_events': {
        'resource': 'receivers.json/{id}/events',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/list_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/create_post'],
        'methods': ['GET', 'POST'],
    },
    'receiver_orders': {
        'resource': 'receivers.json/{id}/orders',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/list__get',
                 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/create__post'],
        'methods': ['GET', 'POST'],
    },
    'receiver_tags': {
        'resource': 'receivers.json/{id}/tags',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/retrieveTags_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/addTags_post'],
        'methods': ['GET', 'POST'],
    },
    'receiver_tag_remove': {
        'resource': 'receivers.json/{id}/tags/{tag}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/removeTag_delete',
        'methods': ['DELETE'],
    },
    'receiver_attributes': {
        'resource': 'receivers.json/{id}/attributes',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/retrievePoolAttributes_get',
        'methods': ['GET'],
    },
    'receiver_attribute': {
        'resource': 'receivers.json/{id}/attributes/{attribute_id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/receivers-v2/savePoolAttribute_put',
        'methods': ['PUT'],
    },
    'reports': {
        'resource': 'reports.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/list_get',
        'methods': ['GET'],
    },
    'report': {
        'resource': 'reports.json/{id}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/retrieve_get',
        'methods': ['GET'],
    },
    'report_orders': {
        'resource': 'reports.json/{id}/orders',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/retrieveByMailing_get',
        'methods': ['GET'],
    },
    'report_receivers': {
        'resource': 'reports.json/{id}/receivers',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/userReceived_get',
        'methods': ['GET'],
    },
    'report_receivers_state': {
        'resource': 'reports.json/{id}/receivers/{state}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/userReceived__get',
        'methods': ['GET'],
    },
    'report_stats': {
        'resource': 'reports.json/{id}/stats',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/stats_get',
        'methods': ['GET'],
    },
    'report_stats_mode': {
        'resource': 'reports.json/{id}/stats/{mode}',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/reports-v2/stats__get',
        'methods': ['GET'],
    },
    'mailings': {
        'resource': 'mailings.json',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/list_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/mailingCreate_post'],
        'methods': ['GET', 'POST'],
    },
    'mailings_channels': {
        'resource': 'mailings/channel.json',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/list__get',
        'methods': ['GET'],
    },
    'mailings_channel': {
        'resource': 'mailings/channel.json/{id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/retrieve__get',
                 'https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/remove_delete'],
        'methods': ['GET', 'DELETE'],
    },
    'mailing': {
        'resource': 'mailings.json/{id}',
        'docs': ['https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/retrieve_get',
                 'https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/mailingUpdate_put'],
        'methods': ['GET', 'PUT'],
    },
    'mailing_links': {
        'resource': 'mailings.json/{id}/links',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/retrieveLinks_get',
        'methods': ['GET'],
    },
    'mailing_orders': {
        'resource': 'mailings.json/{id}/orders',
        'docs': 'https://rest.cleverreach.com/explorer/v2/#!/mailings-v2/retrieveByMailing_get',
        'methods': ['GET'],
    },
}
