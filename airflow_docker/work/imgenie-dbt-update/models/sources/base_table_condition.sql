{{ config(materialized='view',tags=['condition_occurrence']) }}
{{   base_table('Condition')  }}