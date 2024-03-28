
  {{ config(materialized='incremental',
  depends_on=['ref("base_table_observation")']
  ,unique_key='observation_id',tags=['observation']) 
   }}
SELECT
'identifier' as "observation_id",  --缺漏
'valueQuantity' as "unit_concept_id",  --缺漏
substring(performer from '"reference": "([^"]+)"')  as "provider_id",
substring(encounter from '"reference": "([^"]+)"') as "visit_occurrence_id",
substring(subject from '"reference": "([^"]+)"') as "person_id",
substring(code from '"code": "([^"]+)"')  as "observation_concept_id", --不知道取哪個 
"effectiveDateTime" as "observation_date",
"effectiveDateTime" as "observation_datetime",
'valueInt' as "value_as_number",  --缺漏
'valueString' as "value_as_string",  --缺漏
'valueCodeableConcept' as "value_as_concept_id"  --缺漏
,create_time
FROM  
 {{   ref('base_table_observation')  }}
  {% if is_incremental() %}
where  create_time > (select max(create_time) from {{ this  }}  LIMIT 1)
{% endif %}