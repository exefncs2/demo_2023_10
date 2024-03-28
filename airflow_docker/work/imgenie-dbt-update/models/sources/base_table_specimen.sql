{{ config(materialized='view',tags=['specimen']) }}  
  {{   base_table('Specimen')  }}