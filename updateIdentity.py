import json
import requests

#refresh_token = bac21b16f8d7d4803aabf19a2e40f3ebf656b72043730142a5e5569171c27552

url = "https://api.freshbooks.com/auth/api/v1/users/me"
headers = {'Authorization': 'Bearer 1ac622e799b22c1d6b07da0b5fd3f0e6406b1727c79b9af648dffce3fbd907e0', 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
res = requests.get(url, data=None, headers=headers)
jsonData = res.json()

print jsonData


















# {u'response': {u'profile': {u'phone_number': None, u'first_name': u'Shaira', u'last_name': u'Abancio', u'professions': [{u'company': u'Shaira Abancio', u'title': u'Web App Development', u'id': 1346391, u'designation': None, u'business_id': 1039995}, {u'company': u'Shaira Abancio', u'title': u'Software Development', u'id': 1346393, u'designation': None, u'business_id': 1039995}, {u'company': u'Shaira Abancio', u'title': u'Web Services', u'id': 1346395, u'designation': None, u'business_id': 1039995}], u'setup_complete': True, u'address': None}, u'business_memberships': [{u'unacknowledged_change': False, u'role': u'owner', u'id': 4121679, u'business': {u'phone_number': None, u'date_format': u'mm/dd/yyyy', u'business_clients': [], u'account_id': u'6GeAy', u'address': {u'province': u'', u'city': u'', u'country': u'Philippines', u'street': u'', u'postal_code': u'', u'id': 1158769}, u'id': 1039995, u'name': u'Shaira Abancio'}}], u'first_name': u'Shaira', u'last_name': u'Abancio', u'addresses': [None], u'links': {u'me': u'/service/auth/api/v1/users?id=1081625', u'roles': u'/service/auth/api/v1/users/role/1081625'}, u'unconfirmed_email': None, u'confirmed_at': u'2018-06-29T02:21:53Z', u'created_at': u'2018-06-29T02:19:30Z', u'profession': {u'company': u'Shaira Abancio', u'title': u'Web App Development', u'id': 1346391, u'designation': None, u'business_id': 1039995}, u'integrations': {}, u'email': u'abancioshaira1@gmail.com', u'setup_complete': True, u'subscription_statuses': {u'6GeAy': u'active_trial'}, u'roles': [{u'links': {u'destroy': u'/service/auth/api/v1/users/role/1138205'}, u'created_at': u'2018-06-29T02:19:30Z', u'userid': 1, u'systemid': 3515945, u'role': u'admin', u'id': 1138205, u'accountid': u'6GeAy'}], u'groups': [{u'business_id': 1039995, u'role': u'owner', u'identity_id': 1081625, u'active': True, u'group_id': 3027757, u'id': 4121679}], u'phone_numbers': [{u'phone_number': None, u'title': u''}], u'identity_origin': u'magnum', u'id': 1081625, u'permissions': {u'6GeAy': {u'advanced_accounting.access': True, u'auto_bank_import.access': True, u'beta_mobile_create_expense_subcategory.access': True, u'buy_now_pay_later.access': True, u'attachments.access': True, u'helios_sync_throttle.beta.access': True, u'helios_invoice_archive.beta.access': True, u'helios_late_fee_reminder.beta.access': True, u'expense_is_cogs.access': True, u'helios_company_taxes.beta.access': True, u'ios_beta_payment_schedules.access': True, u'BetaHeliosAsyncExpenses.access': True, u'client.limit': -1, u'helios_dashboard.access': True, u'mobile_receipt_rebilling.access': True, u'helios_pushnotifications.beta.access': True, u'rich_proposals.access': True, u'invitation_flow.access': True, u'helios_rebill_time.access': True, u'staff.limit': -1, u'referral_program.access': True, u'esignatures.access': True, u'ExpenseCSVImport.access': True, u'proposals_candidate.access': True, u'helios_async_clients_push.beta.access': True, u'ClientCSVImport.access': True, u'ios_beta_zendesk_widget.access': True, u'new_accept_credit_cards_page.access': True}}}}