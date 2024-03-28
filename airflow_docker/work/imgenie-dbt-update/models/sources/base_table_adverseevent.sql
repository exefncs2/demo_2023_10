{{ config(materialized='view',tags=['death']) }}
{{   base_table('AdverseEvent')  }}