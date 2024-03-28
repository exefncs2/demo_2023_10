{{ config(materialized='view',tags=['drug_exposure']) }}
{{   base_table('MedicationStatement')  }}
