{{ config(materialized='view',tags=['procedure_occurrence','device_exposure']) }}  
  {{   base_table('Procedure')  }}