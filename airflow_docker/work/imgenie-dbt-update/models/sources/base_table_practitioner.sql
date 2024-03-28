{{ config(materialized='view',tags=['provider']) }}
{{   base_table('Practitioner')  }}
