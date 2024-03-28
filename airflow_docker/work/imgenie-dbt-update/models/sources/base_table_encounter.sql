{{ config(materialized='view',tags=['visit_occurrence']) }}
{{   base_table('Encounter')  }}