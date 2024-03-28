{{ config(materialized='view',tags=['composition']) }}
{{   base_table('Composition')  }}
