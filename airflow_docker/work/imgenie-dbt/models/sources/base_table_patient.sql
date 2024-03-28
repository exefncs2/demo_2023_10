{{ config(materialized='view') }}  
  {{   base_table('Patient')  }}