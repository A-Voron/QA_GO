import json

json_data = '''
{"abgroup.experiments.configs_base64": {
            "kind": "VALUE_KIND_MAP",
            "mapValue": {
                "fields": {
                    "ab-poligon-sc": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJUaXRsZSI6ImFiLVBvbC1TYyJ9"
                    },
                    "bot-gateway-sc": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJTeE5ld0ZCU01vZGVsIjp0cnVlfQ=="
                    },
                    "complain-price-service": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJjb21wbGFpbnNfb2ZmIjp0cnVlLCJzZW5kX2NvbXBsYWluc19yZXN1bHQiOnRydWV9"
                    },
                    "content-validation": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0="
                    },
                    "logistic-service": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJhdXRvX2Fzc2VtYmx5Ijp0cnVlLCJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0="
                    },
                    "messenger-custom-blocks-sc": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJIaWRlQW5kTXV0ZUNoYXQiOnRydWV9"
                    },
                    "messenger-seller-facade": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJIaWRlQW5kTXV0ZUNoYXQiOnRydWUsIlRyYW5zbGF0ZUN1c3RvbWVyTWVzc2FnZXMiOnRydWUsIlRyYW5zbGF0ZVN1cHBvcnRNZXNzYWdlcyI6dHJ1ZX0="
                    },
                    "premium-mailings": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJidVJhbmtlckVuYWJsZWQiOnRydWUsIm1haWxpbmdBdWRpZW5jZVJhbmtpbmdNb2RlIjoidXBsaWZ0U2NvcmUiLCJzZWxsZXJBdWRpZW5jZVdpdGhvdXRSZWNlbnRPcmRlciI6dHJ1ZX0="
                    },
                    "seller-actions-api": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJBbGxvd0JpZ1Byb21vRXhjZWwiOnRydWUsIlNob3dNUFNQIjp0cnVlLCJTaG93U2FsZXMiOnRydWUsIlNob3dXaWRnZXRHTVYiOnRydWV9"
                    },
                    "seller-assortment": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJtb2RlbF9hcmNoaXZpbmciOnRydWV9"
                    },
                    "seller-center": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJCYW9mdU9mZmVyZWRFbmFibGVkIjp0cnVlLCJDaG91emhvdU9mZmVyZWRFbmFibGVkIjpmYWxzZSwiTExQT2ZmZXJlZEVuYWJsZWQiOnRydWUsIkxvZ09uYm9hcmRpbmdWMSI6dHJ1ZSwiTWFzc0Rvd25sb2FkTGFiZWxzQW5kQXNzZW1ibHlMaXN0Ijp0cnVlLCJNYXNzU2hpcEFzeW5jQXZhaWxhYmxlIjp0cnVlLCJOYW1lVGVtcGxhdGVFbmFibGVkIjp0cnVlLCJOYXZpZ2F0aW9uQ29tcGxhaW50cyI6dHJ1ZSwiTmV3X1ByZW1pdW1fTGFuZGluZyI6dHJ1ZSwiUFNQTXVsdGlDb25uZWN0aW9uTmV3Rmxvd0F2YWlsYWJsZSI6dHJ1ZSwiUGluZ1BvbmdPZmZlcmVkRW5hYmxlZCI6dHJ1ZSwiUHJlbWl1bV9DaXMiOnRydWUsIlByZW1pdW1fYmlsbGluZyI6dHJ1ZSwiUHJvbW9SZXZpZXdzRW5hYmxlZCI6dHJ1ZSwiUmVnaXN0cmF0aW9uU2VydmljZU9mZiI6dHJ1ZSwiV0JfY3JlYXRpb24iOnRydWUsIldoYWxldE9mZmVyZWRFbmFibGVkIjpmYWxzZSwiYWRtaW5fY2Fyb3VzZWxfYmFubmVycyI6dHJ1ZSwiYXR0cmlidXRlc19zdWdnZXN0aW9uc19lbmFibGVkIjp0cnVlLCJhdXRvX2Fzc2VtYmx5Ijp0cnVlLCJhdmFpbGFibGVfYmFua19sYW5kaW5nIjp0cnVlLCJhdmFpbGFibGVfY2hhbmdlX3JlcXVpc2l0ZXNfYmxvY2siOnRydWUsImF2YWlsYWJsZV9jaGFuZ2VfcmVxdWlzaXRlc19ibG9ja19sZWdhbCI6dHJ1ZSwiYmFsYW5jZVBhZ2VfbmV3RGVzaWduX2ZsYWciOnRydWUsImJhbmtfZGV0YWlsX2VkaXRfQ05ISyI6ZmFsc2UsImNhdGVnb3J5X3ByZWRpY3Rpb24yX2VuYWJsZSI6dHJ1ZSwiY25hcHNfQ05fcmVxdWlyZWQiOmZhbHNlLCJkaXNwb3Nlc19mZWVfZW5hYmxlIjp0cnVlLCJmYnBfYWNjZXNzaWJpbGl0eV9keW5hbWljX2F2YWlsIjp0cnVlLCJmYnBfYXZhaWwiOnRydWUsImZicF9zdG9ja3NfYXZhaWwiOnRydWUsImlzR2VuZXJhbEZCU0luZGV4QXZhaWxhYmxlT25seSI6dHJ1ZSwiaXNOZXdJc3N1ZUNyZWF0aW9uQXZhaWxhYmxlIjp0cnVlLCJpc19zZWxsZXJfaGlnaGxpZ2h0c19ib29zdGluZ19zaG93biI6dHJ1ZSwiaXNfc2VsbGVyX2hpZ2hsaWdodHNfc2hvd24iOnRydWUsImlzX3NlbGxlcl9oaWdobGlnaHRzX3N0YXRpY19zaG93biI6dHJ1ZSwiaXNfc3RvY2tzX3R1cm5vdmVyX2F2YWlsIjpmYWxzZSwiaXRlbS10b2dnbGUtbmFtZS10ZW1wbGF0ZSI6dHJ1ZSwibWFpbl9kZWJpdCI6dHJ1ZSwibWxfYW5ub3RhdGlvbl9lbmFibGVkIjp0cnVlLCJtcG10X2Nsb3RoZXNfZW5hYmxlIjp0cnVlLCJuZXdfYWRkaXRpb25hbF9pbmZvX2xvZ2ljX2VuYWJsZWQiOnRydWUsIm5ld19zdG9ja3NfYnlfd2FyZWhvdXNlX2VuYWJsZWQiOnRydWUsInByZW1pdW1fZXhpdF90ZXN0Ijp0cnVlLCJya29fYWNjZXB0ZWRfb2ZmZXJfZW5hYmxlZCI6dHJ1ZSwicmtvX2F2YWlsYWJsZV9vZmZlcl9lbmFibGVkIjp0cnVlLCJya29fY2Fyb3VzZWxfYmFubmVyc19lbmFibGVkIjp0cnVlLCJya29fZmluYW5jZV9iYW5uZXJzX2VuYWJsZWQiOnRydWUsInJrb19nZ3ZfZW5hYmxlZCI6dHJ1ZSwicmtvX3N0b3JpZXNfZW5hYmxlZCI6ZmFsc2UsInNob3dfc3VwZXJfYW5hbHl0aWNzIjp0cnVlLCJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZSwidW5wYWlkX2xlZ2FsX29yZGVyX3Byb2R1Y3RfbGlzdCI6dHJ1ZX0="
                    },
                    "supplier-drafts": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0="
                    },
                    "sx-mobile-business-platform": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJucHNfcG9sbF9sdF90b2dnbGUiOnRydWV9"
                    },
                    "sx-mobile-growth": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0="
                    },
                    "sx-mobile-products": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "e30="
                    },
                    "ui-modal-helper": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJtcG10X2Nsb3RoZXNfZW5hYmxlIjp0cnVlfQ=="
                    },
                    "xls-processor": {
                        "kind": "VALUE_KIND_BYTES",
                        "bytesValue": "eyJzdXBlcl9lY29ub21fZW5hYmxlZCI6dHJ1ZX0="
                    }
                }
            }
        }
    }
'''




# Парсим JSON
data = json.loads(json_data)

# Извлекаем все ключи уровня "fields"
keys = data['abgroup.experiments.configs_base64']['mapValue']['fields'].keys()

# Формирование строки с ключами
config_string = '|'.join(keys)

# Подсчет количества элементов
count = len(config_string.split('|'))
print("----")
print(config_string)
print(f"Количество конфигураций: {count}")
print("----")

