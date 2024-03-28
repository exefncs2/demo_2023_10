{{ config(materialized='view') }}
{{   base_table('AdverseEvent')  }}