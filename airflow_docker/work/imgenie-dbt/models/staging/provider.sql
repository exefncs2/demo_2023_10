{{ config(materialized='table',
  depends_on=['ref("base_table_practitioner")']
  ,unique_key='provider_id') }}
  
select 
substring(meta from '"source": "([^"]+)"') as "provider_id", --不知道取哪個
jsonb_array_elements(name::jsonb) ->> 'text' as "provider_name",
substring(identifier from '"npi": "([^"]+)"') as "npi", --不知道取哪個
'qualification' as "dea", --缺漏
'specialty' as "specialty_concept_id", --缺漏
'location' as "care_site_id", --缺漏
'birthDate' as "year_of_birth", --缺漏
'gender' as "gender_concept_id" --缺漏
, create_time
FROM 
  {{   ref('base_table_practitioner')  }}
