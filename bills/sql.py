# SELECT name, COUNT(name)
# FROM(SELECT *
#      FROM bills_client
#         JOIN bills_organization
#             ON bills_organization.client_name = bills_client.name)
#     GROUP BY name;
#




# SELECT name, SUM(balance)
# FROM bills_client
# JOIN bills_organization
#     ON bills_organization.client_name = bills_client.name
# JOIN bills_bills
#     ON bills_bills.organization_client = bills_organization.organization
# GROUP BY name
