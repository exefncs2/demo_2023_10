{{ config(materialized='table',
  depends_on=['ref("base_table_specimen")']
  ,unique_key='visit_occurence_id'
  ) }}
select 
substring(identifier from '"value": "([^"]+)"') as "specimen_id",
subject::jsonb ->> 'reference' as "person_id", --值名與官網不同
substring(type from '"code": "([^"]+)"') as "specimen_concept_id",
substring(collection from '"collectedDateTime": "([^"]+)"') as "specimen_date", --重複時間
substring(collection from '"collectedDateTime": "([^"]+)"') as "specimen_datetime" , --重複時間
collection::jsonb -> 'quantity' as "quantity", --缺漏 quantity
collection::jsonb -> 'quantity' ->> 'unit' as "unit_concept_id", --缺漏 quantity.unit
(collection::jsonb ->> 'bodySite')::jsonb ->> 'text' as "anatomic_site_concept_id" --位置與官網不同 
,create_time
FROM 
  {{   ref('base_table_specimen')  }}
