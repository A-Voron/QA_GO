import json


# JSON данные
json_data = '''
{
    "configs": {
        "ab-poligon-sc": {
            "config": "e30=",
            "experiments": [
                {
                    "ID": "11567",
                    "variantID": "29882",
                    "alias": "control-12214"
                }
            ]
        },
        "bot-gateway-sc": {
            "config": "e30=",
            "experiments": [
                {
                    "ID": "11302",
                    "variantID": "29097",
                    "alias": "control-11960"
                },
                {
                    "ID": "12335",
                    "variantID": "32099",
                    "alias": "control-12895"
                }
            ]
        },
        "complain-price-service": {
            "config": "eyJjb21wbGFpbnNfb2ZmIjp0cnVlLCJzZW5kX2NvbXBsYWluc19yZXN1bHQiOnRydWV9",
            "experiments": [
                {
                    "ID": "11381",
                    "variantID": "27678",
                    "alias": "complains_off"
                },
                {
                    "ID": "12495",
                    "variantID": "32357",
                    "alias": ""
                }
            ]
        },
        "content-validation": {
            "config": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0=",
            "experiments": [
                {
                    "ID": "9487",
                    "variantID": "24609",
                    "alias": ""
                }
            ]
        },
        "logistic-service": {
            "config": "eyJhdXRvX2Fzc2VtYmx5Ijp0cnVlLCJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0=",
            "experiments": [
                {
                    "ID": "9487",
                    "variantID": "24609",
                    "alias": ""
                },
                {
                    "ID": "11891",
                    "variantID": "30924",
                    "alias": "auto_assembly"
                }
            ]
        },
        "messenger-custom-blocks-sc": {
            "config": "eyJIaWRlQW5kTXV0ZUNoYXQiOnRydWV9",
            "experiments": [
                {
                    "ID": "11734",
                    "variantID": "30282",
                    "alias": ""
                }
            ]
        },
        "messenger-seller-facade": {
            "config": "eyJIaWRlQW5kTXV0ZUNoYXQiOnRydWUsIlRyYW5zbGF0ZUN1c3RvbWVyTWVzc2FnZXMiOnRydWUsIlRyYW5zbGF0ZVN1cHBvcnRNZXNzYWdlcyI6dHJ1ZX0=",
            "experiments": [
                {
                    "ID": "10078",
                    "variantID": "26135",
                    "alias": ""
                },
                {
                    "ID": "10080",
                    "variantID": "26136",
                    "alias": ""
                },
                {
                    "ID": "11734",
                    "variantID": "30282",
                    "alias": ""
                }
            ]
        },
        "premium-mailings": {
            "config": "eyJtYWlsaW5nQXVkaWVuY2VSYW5raW5nTW9kZSI6InVwbGlmdFNjb3JlIn0=",
            "experiments": [
                {
                    "ID": "12647",
                    "variantID": "32750",
                    "alias": "control-13186"
                },
                {
                    "ID": "12677",
                    "variantID": "32839",
                    "alias": "control-13212"
                },
                {
                    "ID": "12895",
                    "variantID": "33337",
                    "alias": "upliftScore"
                }
            ]
        },
        "seller-actions-api": {
            "config": "eyJBbGxvd0JpZ1Byb21vRXhjZWwiOnRydWUsIlNob3dNUFNQIjp0cnVlLCJTaG93U2FsZXMiOnRydWUsIlNob3dXaWRnZXRHTVYiOnRydWV9",
            "experiments": [
                {
                    "ID": "10721",
                    "variantID": "27627",
                    "alias": "widget_gmv"
                },
                {
                    "ID": "12048",
                    "variantID": "31449",
                    "alias": "excel_one"
                },
                {
                    "ID": "12050",
                    "variantID": "31452",
                    "alias": "seller_actions_show_sales"
                }
            ]
        },
        "seller-assortment": {
            "config": "eyJtb2RlbF9hcmNoaXZpbmciOnRydWV9",
            "experiments": [
                {
                    "ID": "10622",
                    "variantID": "27393",
                    "alias": "model_archiving"
                }
            ]
        },
        "seller-center": {
            "config": "eyJCYW9mdU9mZmVyZWRFbmFibGVkIjp0cnVlLCJDaG91emhvdU9mZmVyZWRFbmFibGVkIjpmYWxzZSwiTExQT2ZmZXJlZEVuYWJsZWQiOnRydWUsIkxvZ09uYm9hcmRpbmdWMSI6dHJ1ZSwiTWFzc0Rvd25sb2FkTGFiZWxzQW5kQXNzZW1ibHlMaXN0Ijp0cnVlLCJNYXNzU2hpcEFzeW5jQXZhaWxhYmxlIjp0cnVlLCJOYW1lVGVtcGxhdGVFbmFibGVkIjp0cnVlLCJOYXZpZ2F0aW9uQ29tcGxhaW50cyI6dHJ1ZSwiTmV3X1ByZW1pdW1fTGFuZGluZyI6dHJ1ZSwiUFNQTXVsdGlDb25uZWN0aW9uTmV3Rmxvd0F2YWlsYWJsZSI6dHJ1ZSwiUGluZ1BvbmdPZmZlcmVkRW5hYmxlZCI6dHJ1ZSwiUHJlbWl1bV9DaXMiOnRydWUsIlByZW1pdW1fYmlsbGluZyI6dHJ1ZSwiUHJvbW9SZXZpZXdzRW5hYmxlZCI6dHJ1ZSwiUmVnaXN0cmF0aW9uU2VydmljZU9mZiI6dHJ1ZSwiV0JfY3JlYXRpb24iOnRydWUsIldoYWxldE9mZmVyZWRFbmFibGVkIjpmYWxzZSwiYWRtaW5fY2Fyb3VzZWxfYmFubmVycyI6dHJ1ZSwiYXR0cmlidXRlc19zdWdnZXN0aW9uc19lbmFibGVkIjp0cnVlLCJhdXRvX2Fzc2VtYmx5Ijp0cnVlLCJhdmFpbGFibGVfYmFua19sYW5kaW5nIjp0cnVlLCJhdmFpbGFibGVfY2hhbmdlX3JlcXVpc2l0ZXNfYmxvY2siOnRydWUsImF2YWlsYWJsZV9jaGFuZ2VfcmVxdWlzaXRlc19ibG9ja19sZWdhbCI6dHJ1ZSwiYmFsYW5jZVBhZ2VfbmV3RGVzaWduX2ZsYWciOnRydWUsImJhbmtfZGV0YWlsX2VkaXRfQ05ISyI6ZmFsc2UsImNhdGVnb3J5X3ByZWRpY3Rpb24yX2VuYWJsZSI6dHJ1ZSwiY25hcHNfQ05fcmVxdWlyZWQiOmZhbHNlLCJkaXNwb3Nlc19mZWVfZW5hYmxlIjp0cnVlLCJmYnBfYWNjZXNzaWJpbGl0eV9keW5hbWljX2F2YWlsIjp0cnVlLCJmYnBfYXZhaWwiOnRydWUsImZicF9zdG9ja3NfYXZhaWwiOnRydWUsImlzTmV3SXNzdWVDcmVhdGlvbkF2YWlsYWJsZSI6dHJ1ZSwiaXNfc2VsbGVyX2hpZ2hsaWdodHNfYm9vc3Rpbmdfc2hvd24iOnRydWUsImlzX3NlbGxlcl9oaWdobGlnaHRzX3Nob3duIjp0cnVlLCJpc19zZWxsZXJfaGlnaGxpZ2h0c19zdGF0aWNfc2hvd24iOnRydWUsImlzX3N0b2Nrc190dXJub3Zlcl9hdmFpbCI6ZmFsc2UsIml0ZW0tdG9nZ2xlLW5hbWUtdGVtcGxhdGUiOnRydWUsIm1haW5fZGViaXQiOnRydWUsIm1sX2Fubm90YXRpb25fZW5hYmxlZCI6dHJ1ZSwibXBtdF9jbG90aGVzX2VuYWJsZSI6dHJ1ZSwibmV3X2FkZGl0aW9uYWxfaW5mb19sb2dpY19lbmFibGVkIjp0cnVlLCJuZXdfc3RvY2tzX2J5X3dhcmVob3VzZV9lbmFibGVkIjp0cnVlLCJwcmVtaXVtX2V4aXRfdGVzdCI6dHJ1ZSwicmtvX2FjY2VwdGVkX29mZmVyX2VuYWJsZWQiOnRydWUsInJrb19hdmFpbGFibGVfb2ZmZXJfZW5hYmxlZCI6dHJ1ZSwicmtvX2Nhcm91c2VsX2Jhbm5lcnNfZW5hYmxlZCI6dHJ1ZSwicmtvX2ZpbmFuY2VfYmFubmVyc19lbmFibGVkIjp0cnVlLCJya29fZ2d2X2VuYWJsZWQiOnRydWUsInJrb19zdG9yaWVzX2VuYWJsZWQiOmZhbHNlLCJzaG93X3N1cGVyX2FuYWx5dGljcyI6dHJ1ZSwic3VwZXJfZWNvbm9tX2VuYWJsZWQiOnRydWUsInVucGFpZF9sZWdhbF9vcmRlcl9wcm9kdWN0X2xpc3QiOnRydWV9",
            "experiments": [
                {
                    "ID": "3913",
                    "variantID": "10239",
                    "alias": ""
                },
                {
                    "ID": "5417",
                    "variantID": "14257",
                    "alias": "is_new_issue_creation_available_5"
                },
                {
                    "ID": "8237",
                    "variantID": "21509",
                    "alias": ""
                },
                {
                    "ID": "8687",
                    "variantID": "22621",
                    "alias": "ml_annotation"
                },
                {
                    "ID": "9487",
                    "variantID": "24609",
                    "alias": ""
                },
                {
                    "ID": "9650",
                    "variantID": "25066",
                    "alias": ""
                },
                {
                    "ID": "10124",
                    "variantID": "24336",
                    "alias": ""
                },
                {
                    "ID": "10340",
                    "variantID": "26754",
                    "alias": ""
                },
                {
                    "ID": "10369",
                    "variantID": "24020",
                    "alias": "new_stocks_by_warehouse_enabled_true"
                },
                {
                    "ID": "10409",
                    "variantID": "26922",
                    "alias": ""
                },
                {
                    "ID": "10516",
                    "variantID": "27142",
                    "alias": "category_prediction2_enable"
                },
                {
                    "ID": "10535",
                    "variantID": "27192",
                    "alias": ""
                },
                {
                    "ID": "10545",
                    "variantID": "27223",
                    "alias": ""
                },
                {
                    "ID": "10665",
                    "variantID": "27503",
                    "alias": ""
                },
                {
                    "ID": "10744",
                    "variantID": "27689",
                    "alias": ""
                },
                {
                    "ID": "10746",
                    "variantID": "27693",
                    "alias": ""
                },
                {
                    "ID": "10864",
                    "variantID": "27952",
                    "alias": ""
                },
                {
                    "ID": "10865",
                    "variantID": "27954",
                    "alias": "canSeeHighlights"
                },
                {
                    "ID": "11118",
                    "variantID": "28550",
                    "alias": ""
                },
                {
                    "ID": "11124",
                    "variantID": "28562",
                    "alias": "attributes_suggestions_enabled"
                },
                {
                    "ID": "11195",
                    "variantID": "27414",
                    "alias": ""
                },
                {
                    "ID": "11211",
                    "variantID": "28872",
                    "alias": "WB_creation"
                },
                {
                    "ID": "11244",
                    "variantID": "28944",
                    "alias": "canSeeHighlightsBoosting"
                },
                {
                    "ID": "11247",
                    "variantID": "28952",
                    "alias": ""
                },
                {
                    "ID": "11404",
                    "variantID": "29359",
                    "alias": "control-12057"
                },
                {
                    "ID": "11405",
                    "variantID": "29361",
                    "alias": "control-12058"
                },
                {
                    "ID": "11499",
                    "variantID": "29713",
                    "alias": ""
                },
                {
                    "ID": "11631",
                    "variantID": "30033",
                    "alias": ""
                },
                {
                    "ID": "11640",
                    "variantID": "30055",
                    "alias": ""
                },
                {
                    "ID": "11667",
                    "variantID": "30118",
                    "alias": ""
                },
                {
                    "ID": "11682",
                    "variantID": "30146",
                    "alias": ""
                },
                {
                    "ID": "11807",
                    "variantID": "30580",
                    "alias": "unpaid_legal_order_product_list"
                },
                {
                    "ID": "11891",
                    "variantID": "30924",
                    "alias": "auto_assembly"
                },
                {
                    "ID": "11924",
                    "variantID": "30931",
                    "alias": "fbp_availability"
                },
                {
                    "ID": "11944",
                    "variantID": "31027",
                    "alias": "banner-sc-performance"
                },
                {
                    "ID": "11974",
                    "variantID": "31135",
                    "alias": "disposes_fee_enable"
                },
                {
                    "ID": "12139",
                    "variantID": "28940",
                    "alias": "balancePage_newDesign"
                },
                {
                    "ID": "12142",
                    "variantID": "31661",
                    "alias": ""
                },
                {
                    "ID": "12432",
                    "variantID": "32274",
                    "alias": "control-12987"
                },
                {
                    "ID": "12520",
                    "variantID": "32415",
                    "alias": "fbp_stocks_avail"
                },
                {
                    "ID": "12639",
                    "variantID": "32727",
                    "alias": "fbp_accessibility_dynamic_avail"
                },
                {
                    "ID": "12686",
                    "variantID": "32862",
                    "alias": "control-13221"
                },
                {
                    "ID": "12784",
                    "variantID": "33124",
                    "alias": "is_stocks_turnover_avail"
                },
                {
                    "ID": "12803",
                    "variantID": "32494",
                    "alias": ""
                },
                {
                    "ID": "12862",
                    "variantID": "33261",
                    "alias": ""
                },
                {
                    "ID": "12875",
                    "variantID": "33288",
                    "alias": "control-13399"
                },
                {
                    "ID": "12881",
                    "variantID": "33305",
                    "alias": ""
                },
                {
                    "ID": "12893",
                    "variantID": "33334",
                    "alias": "control-13417"
                }
            ]
        },
        "supplier-drafts": {
            "config": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0=",
            "experiments": [
                {
                    "ID": "9487",
                    "variantID": "24609",
                    "alias": ""
                }
            ]
        },
        "sx-mobile-business-platform": {
            "config": "eyJucHNfcG9sbF9sdF90b2dnbGUiOnRydWV9",
            "experiments": [
                {
                    "ID": "9991",
                    "variantID": "25921",
                    "alias": "nps_on"
                }
            ]
        },
        "sx-mobile-growth": {
            "config": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0=",
            "experiments": [
                {
                    "ID": "9487",
                    "variantID": "24609",
                    "alias": ""
                }
            ]
        },
        "sx-mobile-products": {
            "config": "e30=",
            "experiments": [
                {
                    "ID": "11404",
                    "variantID": "29359",
                    "alias": "control-12057"
                },
                {
                    "ID": "11405",
                    "variantID": "29361",
                    "alias": "control-12058"
                }
            ]
        },
        "ui-modal-helper": {
            "config": "eyJtcG10X2Nsb3RoZXNfZW5hYmxlIjp0cnVlfQ==",
            "experiments": [
                {
                    "ID": "9650",
                    "variantID": "25066",
                    "alias": ""
                }
            ]
        },
        "xls-processor": {
            "config": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0=",
            "experiments": [
                {
                    "ID": "9487",
                    "variantID": "24609",
                    "alias": ""
                }
            ]
        }
    },
    "binaryKey": "Ba6AgA8pY8AAEAAAAAIAAAAAAAQAQAERAEAAACihAIEBQAKAAKKoWAFIQAAVQIQAAEoSAAAAACEkik1AIFPEASA="
}
'''

# Парсинг JSON
data = json.loads(json_data)

# Извлечение ключей из configs
keys = list(data['configs'].keys())

# Формирование строки с ключами
config_string = '|'.join(keys)

# Подсчет количества элементов
count = len(config_string.split('|'))
print("----")
print(config_string)
print(f"Количество сервисов: {count}")
print("----")

ids = []
variant_ids = []

for config_name, config_data in data['configs'].items():
    experiments = config_data.get('experiments', [])
    ids.extend([exp['ID'] for exp in experiments])
    variant_ids.extend([exp['variantID'] for exp in experiments])


# Сортируем числа
ids.sort(key=int)
variant_ids.sort(key=int)

id_count = len(ids)
variant_id_count = len(variant_ids)
print("IDs:", "|".join(ids))
print(f"Количество ID: {id_count}")
print("-----")
print("Variant IDs:", "|".join(variant_ids))
print(f"Количество variantID: {variant_id_count}")

"returns-fbs-to-fbo|seller-returns|ab-poligon-sc|seller-center"