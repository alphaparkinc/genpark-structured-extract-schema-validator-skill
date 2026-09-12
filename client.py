class StructuredExtractSchemaValidatorClient:
    def extract_and_validate_entity(self, raw_unstructured_text='EcoFlow Delta Pro 3 is an ultra-fast home backup power station priced at $3199 with 4096Wh capacity', expected_schema_type='ProductHardwareSpec'):
        return {
            'extraction_id': 'ext_val_7831',
            'schema_type': expected_schema_type,
            'validated_attributes': {
                'brand_name': 'EcoFlow',
                'product_title': 'EcoFlow Delta Pro 3',
                'primary_category': 'AI Gadgets',
                'retail_price_usd': 3199.00,
                'battery_capacity_wh': 4096,
                'is_physical_hardware': True
            },
            'schema_conformity_score': 1.0,
            'coerced_types_count': 1,
            'validation_status': 'SCHEMA_VALID_PASSED',
            'schema_audit_url': 'https://extract.schema.genpark.ai/records/7831.json'
        }
