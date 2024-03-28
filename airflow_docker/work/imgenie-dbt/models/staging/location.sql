{{ config(materialized='table',
  depends_on=['ref("base_table_patient")']
  ,unique_key='location_id') }}
SELECT
  jsonb_array_elements(identifier::jsonb) ->> 'value' AS "location_id",
  address::json -> 'address_1' AS "address_1",
  address::json -> 'address_2' AS "address_2",
  address::json -> 'city' AS "city",
  address::json -> 'state' AS "state",
  address::json -> 'zip' AS "zip",
  address::json -> 'country' AS "country"
  ,create_time
FROM  
{{ ref('base_table_patient') }}
 