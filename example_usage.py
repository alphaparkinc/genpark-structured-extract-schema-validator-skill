from client import StructuredExtractSchemaValidatorClient

def main():
    client = StructuredExtractSchemaValidatorClient()
    res = client.extract_and_validate_entity()
    print('Schema Extractor: ' + res['extraction_id'] + ' (' + res['schema_type'] + ')')
    print('Status: ' + res['validation_status'] + ' | Conformity: ' + str(res['schema_conformity_score']))
    print('Extracted Data: ' + str(res['validated_attributes']))
    print('Audit URL: ' + res['schema_audit_url'])

if __name__ == '__main__':
    main()
