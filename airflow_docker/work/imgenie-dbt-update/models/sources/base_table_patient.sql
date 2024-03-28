{{ config(materialized='view',tags=['person','location']) }}  
  {{   base_table('Patient')  }}