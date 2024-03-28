{{ config(materialized='view') }}
{{   base_table('Encounter')  }}