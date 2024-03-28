{{ config(materialized='view',tags=['care_site']) }}
 {{   base_table('Organization')  }}
