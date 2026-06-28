"""
  fb login method by CURL-XD
"""



import requests

headers = {
    'host': 'b-graph.facebook.com',
    'x-fb-request-analytics-tags': '{"network_tags":{"product":"350685531728","request_category":"graphql","purpose":"fetch","retry_attempt":"0"},"application_tags":"graphservice"}',
    'x-fb-rmd': 'state=URL_ELIGIBLE',
    'priority': 'u=0',
    'content-encoding': 'gzip',
    'x-zero-eh': '664c0faaac849cb891d0a261fbb72a12',
    'user-agent': '[FBAN/FB4A;FBAV/566.0.0.48.73;FBBV/997672775;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/ROG;FBBD/ROG;FBPN/com.facebook.katana;FBDV/ASUS_AI2401_A;FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]',
    'x-fb-friendly-name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'x-zero-f-device-id': '51ccbf1e-fa5b-45c1-ac16-a1b9777c7799',
    'x-graphql-request-purpose': 'fetch',
    'x-fb-device-group': '8080',
    'x-tigon-is-retry': 'False',
    'x-graphql-client-library': 'graphservice',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-net-hni': '310005',
    'x-fb-sim-hni': '310005',
    'authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'x-zero-state': 'unknown',
    'x-meta-zca': 'empty_token',
    'app-scope-id-header': '51ccbf1e-fa5b-45c1-ac16-a1b9777c7799',
    'x-fb-connection-type': 'WIFI',
    'x-meta-usdid': 'e58423e5-6ccc-486e-9aa8-32c3817cd6e7.1782655293.MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEVVEwCi58rGtRIOrQdrSaZiPBijC-ApZlraG2PyWF65t5uCkcH0KLNglRNcxXSjOJMcxDEHs4zyE6hQeA6T-kvA.MEUCIHRMX5IIC8_JZ5UWanjdJQybiSiEIIfbJcg2h8vAQvoEAiEA1lEbrjQ3z8f4wtqP02Zd7gVw6urJtvEKB9UcPMv2PQQ',
    # 'accept-encoding': 'gzip, deflate',
    'x-fb-http-engine': 'Tigon/Liger',
    'x-fb-client-ip': 'True',
    'x-fb-server-cluster': 'True',
    'x-fb-conn-uuid-client': 'FAB606Gg7ffUzrTCCC+pZg==',
}

data = {
    'method': 'post',
    'format': 'json',
    'server_timestamps': 'true',
    'locale': 'en_US',
    'purpose': 'fetch',
    'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
    'fb_api_caller_class': 'graphservice',
    'client_doc_id': '119940804215128529807076522688',
    'fb_api_client_context': '{"is_background":false}',
    'variables': '{"params":{"params":"{\\"params\\":\\"{\\\\\\"client_input_params\\\\\\":{\\\\\\"blocked_uids\\\\\\":[],\\\\\\"aac\\\\\\":\\\\\\"{\\\\\\\\\\\\\\"aac_init_timestamp\\\\\\\\\\\\\\":1782651685,\\\\\\\\\\\\\\"aacjid\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"96ebd275-31b4-4a45-8d79-ea1d65490aaf\\\\\\\\\\\\\\",\\\\\\\\\\\\\\"aaccs\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"Z7R3ThqCJnhkJvyEmwECsb1CEkM5WffP5QAqpBmysyU\\\\\\\\\\\\\\"}\\\\\\",\\\\\\"sim_phones\\\\\\":[],\\\\\\"aymh_accounts\\\\\\":[{\\\\\\"profiles\\\\\\":{\\\\\\"id\\\\\\":{\\\\\\"is_derived\\\\\\":0,\\\\\\"credentials\\\\\\":[],\\\\\\"account_center_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"profile_picture_url\\\\\\":\\\\\\"\\\\\\",\\\\\\"small_profile_picture_url\\\\\\":null,\\\\\\"notification_count\\\\\\":0,\\\\\\"token\\\\\\":\\\\\\"\\\\\\",\\\\\\"last_access_time\\\\\\":0,\\\\\\"has_smartlock\\\\\\":0,\\\\\\"credential_type\\\\\\":\\\\\\"none\\\\\\",\\\\\\"password\\\\\\":\\\\\\"\\\\\\",\\\\\\"from_accurate_privacy_result\\\\\\":0,\\\\\\"dbln_validated\\\\\\":0,\\\\\\"user_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"name\\\\\\":\\\\\\"\\\\\\",\\\\\\"nta_eligibility_reason\\\\\\":null,\\\\\\"username\\\\\\":\\\\\\"\\\\\\",\\\\\\"account_source\\\\\\":\\\\\\"\\\\\\"}},\\\\\\"id\\\\\\":\\\\\\"\\\\\\"}],\\\\\\"network_bssid\\\\\\":null,\\\\\\"secure_family_device_id\\\\\\":\\\\\\"e231c77e-3cc7-420b-8e00-0495e5bd1958\\\\\\",\\\\\\"attestation_result\\\\\\":{\\\\\\"keyHash\\\\\\":\\\\\\"6e8b4f0ba8af406afd3a2b5620ab0c5487c2cd6fc794b4857e844cbe1d8fcd6c\\\\\\",\\\\\\"data\\\\\\":\\\\\\"eyJjaGFsbGVuZ2Vfbm9uY2UiOiJXT2xuOGpLMHFQUWVUNUZyNTZIcElNSFQxcXV2bE9zZ05GRy9YenpBOGNzPSIsInVzZXJuYW1lIjoiY3VybC54ZCJ9\\\\\\",\\\\\\"signature\\\\\\":\\\\\\"MEUCIGBo3l53lITVo70m3Hm4J4DMl9Oi2CjOt6HxpEb2mr4CAiEA3bAEzGsiZALdDB83xZLlcLdqOvFCO4D4i1tMYQtu+x0=\\\\\\"},\\\\\\"has_granted_read_contacts_permissions\\\\\\":0,\\\\\\"auth_secure_device_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"has_whatsapp_installed\\\\\\":0,\\\\\\"si_device_param_network_info\\\\\\":{\\\\\\"active_subscriptions_info\\\\\\":null,\\\\\\"default_subscription_info\\\\\\":{\\\\\\"network_type\\\\\\":null,\\\\\\"is_data_roaming\\\\\\":1,\\\\\\"is_esim\\\\\\":null,\\\\\\"is_gsm_roaming\\\\\\":0,\\\\\\"is_sim_sms_capable\\\\\\":null,\\\\\\"is_mobile_data_enabled\\\\\\":1,\\\\\\"sim_carrier_id\\\\\\":-1,\\\\\\"sim_carrier_id_name\\\\\\":null,\\\\\\"sim_state\\\\\\":5,\\\\\\"sim_operator\\\\\\":\\\\\\"310005\\\\\\",\\\\\\"sim_operator_name\\\\\\":\\\\\\"Verizon+Wireless\\\\\\",\\\\\\"signal_strength\\\\\\":null,\\\\\\"group_id_level_1\\\\\\":null,\\\\\\"network_operator\\\\\\":\\\\\\"310005\\\\\\"},\\\\\\"is_airplane_mode\\\\\\":0,\\\\\\"is_active_network_cellular\\\\\\":0,\\\\\\"is_device_sms_capable\\\\\\":1,\\\\\\"sim_count\\\\\\":1,\\\\\\"is_wifi\\\\\\":1},\\\\\\"password\\\\\\":\\\\\\"#PWD_FB4A:2:1782651767:AcWUG0xNJgilNNVSRFAAAcNdo20XQs3hVRGWJrb5Iob8+1bnMwSsktWkriA+7wn1dCyP1sZcwC\\\\/ywgFt+cEwnc1Ievl2z4yL33h68\\\\/XAxVBX\\\\/YJKj24JlM3RaBkKPS5Jzfr2vF64fdNqS\\\\/2bDQVNgTo1M8UCTP3psRcLUMv485qicAFD6\\\\/ZN0tA9ljtiYML1jUAinaUbU\\\\/QD4iMG7QpVGlJe0s3gFWTvdxMhhWyBkYTJjmEI6h3oNq0THDiCPv5bn06dtanPkQTJvBxlxGbi\\\\/DEdOubMJsBFw6XBBVbrQ\\\\/9D75O+fl0x9Mw98fzZTvBp\\\\/FgP0khZgQr+Iu7rFVr1bnyQeujqC+P6VtMmPJ+QQgQh9pOLkaM\\\\/D5LL73Ox\\\\/RtGbCNKOnY=\\\\\\",\\\\\\"sso_token_map_json_string\\\\\\":\\\\\\"\\\\\\",\\\\\\"block_store_machine_id\\\\\\":null,\\\\\\"cloud_trust_token\\\\\\":null,\\\\\\"event_flow\\\\\\":\\\\\\"login_manual\\\\\\",\\\\\\"password_contains_non_ascii\\\\\\":\\\\\\"false\\\\\\",\\\\\\"sim_serials\\\\\\":[],\\\\\\"client_known_key_hash\\\\\\":\\\\\\"\\\\\\",\\\\\\"sso_accounts_auth_data\\\\\\":[],\\\\\\"encrypted_msisdn\\\\\\":\\\\\\"\\\\\\",\\\\\\"has_granted_read_phone_permissions\\\\\\":0,\\\\\\"app_manager_id\\\\\\":\\\\\\"null\\\\\\",\\\\\\"should_show_nested_nta_from_aymh\\\\\\":0,\\\\\\"device_id\\\\\\":\\\\\\"51ccbf1e-fa5b-45c1-ac16-a1b9777c7799\\\\\\",\\\\\\"zero_balance_state\\\\\\":\\\\\\"init\\\\\\",\\\\\\"login_attempt_count\\\\\\":1,\\\\\\"machine_id\\\\\\":\\\\\\"\\\\\\",\\\\\\"flash_call_permission_status\\\\\\":{\\\\\\"READ_PHONE_STATE\\\\\\":\\\\\\"DENIED\\\\\\",\\\\\\"READ_CALL_LOG\\\\\\":\\\\\\"DENIED\\\\\\",\\\\\\"ANSWER_PHONE_CALLS\\\\\\":\\\\\\"DENIED\\\\\\"},\\\\\\"accounts_list\\\\\\":[],\\\\\\"gms_incoming_call_retriever_eligibility\\\\\\":\\\\\\"not_eligible\\\\\\",\\\\\\"family_device_id\\\\\\":\\\\\\"51ccbf1e-fa5b-45c1-ac16-a1b9777c7799\\\\\\",\\\\\\"fb_ig_device_id\\\\\\":[],\\\\\\"device_emails\\\\\\":[],\\\\\\"try_num\\\\\\":1,\\\\\\"lois_settings\\\\\\":{\\\\\\"lois_token\\\\\\":\\\\\\"\\\\\\"},\\\\\\"event_step\\\\\\":\\\\\\"home_page\\\\\\",\\\\\\"headers_infra_flow_id\\\\\\":\\\\\\"a932073a-7bb5-4a41-a830-af8d4c93ddd4\\\\\\",\\\\\\"openid_tokens\\\\\\":{},\\\\\\"contact_point\\\\\\":\\\\\\"curl.xd\\\\\\"},\\\\\\"server_params\\\\\\":{\\\\\\"should_trigger_override_login_2fa_action\\\\\\":0,\\\\\\"is_from_logged_out\\\\\\":0,\\\\\\"should_trigger_override_login_success_action\\\\\\":0,\\\\\\"login_credential_type\\\\\\":\\\\\\"none\\\\\\",\\\\\\"server_login_source\\\\\\":\\\\\\"login\\\\\\",\\\\\\"waterfall_id\\\\\\":\\\\\\"dd857e52-5e3f-40f6-b85c-e94fb92c8b06\\\\\\",\\\\\\"two_step_login_type\\\\\\":\\\\\\"one_step_login\\\\\\",\\\\\\"login_source\\\\\\":\\\\\\"Login\\\\\\",\\\\\\"is_platform_login\\\\\\":0,\\\\\\"pw_encryption_try_count\\\\\\":1,\\\\\\"login_entry_point\\\\\\":\\\\\\"logged_out\\\\\\",\\\\\\"INTERNAL__latency_qpl_marker_id\\\\\\":36707139,\\\\\\"is_from_aymh\\\\\\":0,\\\\\\"offline_experiment_group\\\\\\":\\\\\\"caa_iteration_v6_perf_fb_2\\\\\\",\\\\\\"is_from_landing_page\\\\\\":0,\\\\\\"left_nav_button_action\\\\\\":\\\\\\"BACK\\\\\\",\\\\\\"password_text_input_id\\\\\\":\\\\\\"ssik7k:107\\\\\\",\\\\\\"is_from_empty_password\\\\\\":0,\\\\\\"is_from_msplit_fallback\\\\\\":0,\\\\\\"ar_event_source\\\\\\":\\\\\\"login_home_page\\\\\\",\\\\\\"username_text_input_id\\\\\\":\\\\\\"ssik7k:106\\\\\\",\\\\\\"layered_homepage_experiment_group\\\\\\":null,\\\\\\"device_id\\\\\\":\\\\\\"51ccbf1e-fa5b-45c1-ac16-a1b9777c7799\\\\\\",\\\\\\"login_surface\\\\\\":\\\\\\"login_home\\\\\\",\\\\\\"INTERNAL__latency_qpl_instance_id\\\\\\":174094817600776,\\\\\\"reg_flow_source\\\\\\":\\\\\\"lid_landing_screen\\\\\\",\\\\\\"is_caa_perf_enabled\\\\\\":1,\\\\\\"credential_type\\\\\\":\\\\\\"password\\\\\\",\\\\\\"is_from_password_entry_page\\\\\\":0,\\\\\\"caller\\\\\\":\\\\\\"gslr\\\\\\",\\\\\\"family_device_id\\\\\\":\\\\\\"51ccbf1e-fa5b-45c1-ac16-a1b9777c7799\\\\\\",\\\\\\"is_from_assistive_id\\\\\\":0,\\\\\\"access_flow_version\\\\\\":\\\\\\"pre_mt_behavior\\\\\\",\\\\\\"is_from_logged_in_switcher\\\\\\":0}}\\"}","bloks_versioning_id":"4cc1d89f4d2a83c174a0fca9c88a20a627697a72842fafb8febc50da3d902438","app_id":"com.bloks.www.bloks.caa.login.async.send_login_request"},"scale":"3","nt_context":{"using_white_navbar":true,"styles_id":"a07b73c926a84224348806e6cd486365","pixel_ratio":3,"is_push_on":true,"debug_tooling_metadata_token":null,"is_flipper_enabled":false,"theme_params":[{"value":["three_neutral_gray"],"design_system_name":"XMDS"},{"value":[],"design_system_name":"FDS"}],"bloks_version":"4cc1d89f4d2a83c174a0fca9c88a20a627697a72842fafb8febc50da3d902438"}}',
    'fb_api_analytics_tags': '["GraphServices"]',
    'client_trace_id': 'adfdfff3-3860-42b8-b16e-9a7c67fd13f0',
}

response = requests.post('https://b-graph.facebook.com/graphql', headers=headers, data=data)