{{ config(materialized='view',tags=['observation','measurement']) }}
 {{   base_table('Observation')  }}
